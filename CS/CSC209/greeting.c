#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
char * name;

void sing(int code) {
    printf("Happy birthday to you,\n" );
    printf("Happy birthday to you,\n" );
    sleep(10);
    printf("Happy birthday dear %s,\n", name);
    printf("Happy birthday to you,\n" );

}


int main(int argc, char **argv) {

  name = argv[1];

  struct sigaction newact;
  newact.sa_handler = sing;
  newact.sa_flags = 0;
  sigemptyset(&newact.sa_mask);

  sigaddset(&newact.sa_mask, SIGINT);
  sigaddset(&newact.sa_mask,SIGUSR2);

  sigaction(SIGUSR1,&newact, NULL);



  int i=0;
  for (;;){
    if ((i++ % 50000000) == 0) {
            fprintf(stderr, ".");
        }
  }
}
