#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <string.h>

int main(int argc, char **argv) {
    int i;
    int iterations;


    if (argc != 2) {
        fprintf(stderr, "Usage: forkloop <iterations>\n");
        exit(1);
    }

    iterations = strtol(argv[1], NULL, 10);
    int fd[iterations][2];

    for (i = 1; i < iterations+1; i++) {
        if (i == 1){
          if(pipe(fd[i]) == -1){
            perror("pipe");
            exit(1);
          }
        }

    //make new pipe fd[i+1]
    if(pipe(fd[i+1]) == -1){
      perror("pipe");
      exit(1);
    }

    int n = fork();

    if (n < 0){
      perror("fork");
      exit(1);
    }else if (n == 0){//child process
      if (i == 1){
        if (close(fd[1][1]) == -1) {
          perror("close writing end of pipe in parent");
        }
      //read from parent process through pipe[i]
      int content;
      while (read(fd[i][0], &content,sizeof(int)) == sizeof(int)) {
        printf("Successfully read int %d\n", content);
        if(write(fd[i+1][1],&content,sizeof(int)) != sizeof(int)){
          perror("write");
          exit(1);
        }
      }
      // close read end of pipe[i]
      if (close(fd[1][0]) == -1) {
        perror("close writing end of pipe in parent");
      }

      if (close(fd[2][0]) == -1) {
        perror("close writing end of pipe in parent");
      }
      if (close(fd[2][1]) == -1) {
        perror("close writing end of pipe in parent");
      }

      }else{
          //close last write end of last pipe


        int content;
        while (read(fd[i][0], &content,sizeof(int)) == sizeof(int)) {
          printf("Successfully read int %d\n", content);

          if(write(fd[i+1][1],&content,sizeof(int)) != sizeof(int)){
            perror("write");
            exit(1);
          }
        }
        // close read end of pipe[i]
        if (close(fd[i][0]) == -1) {
          perror("close reading end of pipe in parent");
        }
        if (close(fd[i][1]) == -1) {
          perror("close writing end of pipe in parent");
        }
        }
        }else{//parent process

        if (i == 1){ // first iteration, write all input to pipe

        //close read end for pipe 1
        if (close(fd[1][0]) == -1) {
          perror("close reading end of pipe in parent");
        }
        for (int j=2; j < iterations+1; j++){
          if(write(fd[i][1],&j,sizeof(int)) != sizeof(int)){
            perror("write");
            exit(1);
          }
        }
        // close the write end of pipe 1
        if (close(fd[1][1]) == -1) {
          perror("close writing end of pipe in parent");
        }

        if (close(fd[2][0]) == -1) {
          perror("close writing end of pipe in parent");
        }
        if (close(fd[2][1]) == -1) {
          perror("close writing end of pipe in parent");
        }
        // exit parent process
        int status;
        if (wait(&status) != -1)  {
            if (WIFEXITED(status)) {
                printf("number of process is: %d\n", WEXITSTATUS(status)+1);

            } else {
                printf("[%d] Child exited abnormally\n", getpid());
                exit(1);
            }
        }
        return 0;
        }
        else if (i == iterations){//last time iteration, exit(0) since no process follow it
          if (close(fd[i][0]) == -1) {
            perror("close writing end of pipe in its child");
          }
          if (close(fd[i][1]) == -1) {
            perror("close writing end of pipe in its child");
          }
          exit(0);
        }else{
          if (close(fd[i][0]) == -1) {
            perror("close writing end of pipe in its child");
          }
          if (close(fd[i][1]) == -1) {
            perror("close writing end of pipe in its child");
          }
          int status;
          if (wait(&status) != -1){
              if (WIFEXITED(status)) {
                  exit(WEXITSTATUS(status)+1);
              }else {
                  printf("[%d] Child exited abnormally\n", getpid());
              }
          }
          }
        }
    }
}
