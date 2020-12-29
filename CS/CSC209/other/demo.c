#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <string.h>


int main(int argc, char **argv) {
  int iterations;
  int x = 2;
  iterations = strtol(argv[1], NULL, 10);
  int fd[2];

  pipe(fd);

  int n = fork();

  if (n > 0){
    close(fd[0]);
    for (int j=2; j < iterations+1; j++){
      if(write(fd[1],&j,sizeof(int)) != sizeof(int)){
        perror("write");
      }
    }
    close(fd[1]);
  }

  else if (n == 0){//child
    int content;
    
    close(fd[1]);
    while (read(fd[0], &content,sizeof(int)) == sizeof(int)) {
      printf("Successfully read int %d\n", content);
    }

    close(fd[0]);
    exit(0);
  }

  int status;
  if (wait(&status) != -1)  {
      if (WIFEXITED(status)) {
          int res = WEXITSTATUS(status);
          printf("child terminate with status %d\n",res);

      }else {
          printf("[%d] Child exited abnormally\n", getpid());
      }
  }
  return 0;
}
