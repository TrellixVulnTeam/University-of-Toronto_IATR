#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>


#ifndef PORT
  #define PORT 30000
#endif
#define BUF_SIZE 128

int main(void) {
    // Create the socket FD.
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0) {
        perror("client: socket");
        exit(1);
    }

    // Set the IP and port of the server to connect to.
    struct sockaddr_in server;
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    if (inet_pton(AF_INET, "127.0.0.1", &server.sin_addr) < 1) {
        perror("client: inet_pton");
        close(sock_fd);
        exit(1);
    }

    // Connect to the server.
    if (connect(sock_fd, (struct sockaddr *)&server, sizeof(server)) == -1) {
        perror("client: connect");
        close(sock_fd);
        exit(1);
    }

    //let user provide name
    char buf[BUF_SIZE +1];
    printf("Please enter a username\n");
    fflush(stdout);
    int num_read = read(STDIN_FILENO, buf, BUF_SIZE);
    buf[num_read-1] = '\0'; // don't reaaly need this but it makes it a string

    fprintf(stderr,"I read the name %s\n", buf);
    write(sock_fd, buf, num_read);


    // Read input from the user, send it to the server, and then accept the
    // echo that returns. Exit when stdin is closed.
    // char buf[BUF_SIZE + 1];
    fd_set all_set;
    FD_ZERO(&all_set);
    FD_SET(STDIN_FILENO,&all_set);
    FD_SET(sock_fd,&all_set);

    while (1) {
        fd_set listenfd = all_set;

        select(sock_fd +1, &listenfd, NULL,NULL,NULL);

        //if it was the STDIN_FILENO that was Set
        num_read = read(STDIN_FILENO,buf,BUF_SIZE);
        if(num_read == 0){
          break;
        }
        buf[num_read] = '\0'; //just beacause i am paranoid

        //if it was the sock_fd that was set
        int num_written = write(sock_fd,buf,num_read);
        if (num_written != num_read){
          perror("client:write");
          close(sock_fd);
          exit(1);
        }
    }

    close(sock_fd);
    return 0;
}
