#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv) {
  int i;
  int iterations;
  int factor_1 = 0;
  int factor_2 = 0;

  if (argc != 2) {
      fprintf(stderr, "Usage:\n\tpfact n\n");
      exit(1);
  }

  iterations = strtol(argv[1], NULL, 10);

  if (iterations < 0){
      fprintf(stderr, "Usage:\n\tpfact n\n");
      exit(1);
  }

  int fd[iterations][2];

  //populate pipe_1
  if(pipe(fd[1]) == -1){
    perror("pipe_1");
    exit(1);
  }

  for (i = 1; i < iterations+1; i++) {
    int n = fork();
    if (n < 0) {
        perror("fork");
        exit(1);
    }else if (n == 0){ //child process
      if (i != iterations){
      //populate pipe_(i+1)
      if(pipe(fd[i+1]) == -1){
        perror("pipe");
        exit(1);
      }

      //close write end of pipe_i
      if (close(fd[i][1]) == -1) {
        perror("close writing end of pipe in parent");
      }
      //read from pipe_i and write to pipe_(i+1)
      int content;
      while (read(fd[i][0], &content,sizeof(int)) == sizeof(int)) {
        printf("Successfully read int %d\n", content);
        if(write(fd[i+1][1],&content,sizeof(int)) != sizeof(int)){
          perror("write");
          exit(1);
        }
      }
      //close read end of pipe_i
      if (close(fd[i][0]) == -1) {
        perror("close writing end of pipe in parent");
      }
      }else{// i = iterations
        //close write end of pipe_i
        if (close(fd[i][1]) == -1) {
          perror("close writing end of pipe in parent");
        }
        //only read from pipe_i
        int content;
        while (read(fd[i][0], &content,sizeof(int)) == sizeof(int)) {
          printf("Successfully read int %d\n", content);
        }
        //close read end of pipe_i
        if (close(fd[i][0]) == -1) {
          perror("close writing end of pipe in parent");
        }
        }
    }else{ //parent process
      if(i==1){
        //close read end for pipe_1
        if (close(fd[1][0]) == -1) {
          perror("close reading end of pipe in parent");
        }

        //write input to pipe_1
        for (int j=2; j < iterations+1; j++){
          if(write(fd[i][1],&j,sizeof(int)) != sizeof(int)){
            perror("write");
            exit(1);
          }
        }

        // close the write end of pipe_1
        if (close(fd[1][1]) == -1) {
          perror("close writing end of pipe in parent");
        }


        // exit parent process
        int status;
        if (wait(&status) != -1)  {
            if (WIFEXITED(status)) {
                printf("number of process is: %d\n", WEXITSTATUS(status)+1);

            } else {
                printf("[%d] Child_1 exited abnormally\n", getpid());
                exit(1);
            }
        }
        exit(0);
      }
      else if (i==iterations){
        if (close(fd[i][0]) == -1) {
          perror("close read end of pipe in parent");
        }
        // close the write end of pipe_(i)
        if (close(fd[i][1]) == -1) {
          perror("close writing end of pipe in parent");
        }
        exit(0);
      }else{
        // close the read end of pipe_(i)
        if (close(fd[i][0]) == -1) {
          perror("close read end of pipe in parent");
        }
        // close the write end of pipe_(i)
        if (close(fd[i][1]) == -1) {
          perror("close writing end of pipe in parent");
        }

        //get the exit code from it's child process and  exit with 1 plus it.
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
