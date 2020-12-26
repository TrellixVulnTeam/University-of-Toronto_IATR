#include <string.h>
#include <stdio.h>

int main(int argc, char **argv) {
    char str[80] = "/This is/www.tutorialspoint.com/website";
    
    char *token;
   
   /* get the first token */
   token = strtok(str, "/");
   
   /* walk through other tokens */
   while( token != NULL ) {
      printf( " %s\n", token );
    
      token = strtok(NULL, "/");
   }

      /* get the first token */
   char *new_token;
   new_token = strtok(str, "/");
   
   /* walk through other tokens */
   while( new_token != NULL ) {
      printf( " %s\n", new_token );
    
      new_token = strtok(NULL, "/");
   }
   
   return(0);
}