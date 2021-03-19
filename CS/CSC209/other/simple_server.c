#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>    /* Internet domain header */
#include <arpa/inet.h>     /* only needed on my mac */

#define PORT_NUM 30000
#define MAX_BACKLOG 5

int main() {
    // create socket
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == - 1) {
      perror("server: socket");
      exit(1);
    }

    // Make sure we can reuse the port immediately after the
    // server terminates. Avoids the "address in use" error
    int on = 1;
    if (setsockopt(sock_fd, SOL_SOCKET, SO_REUSEADDR,
           (const char *) &on, sizeof(on)) == -1) {
        perror("setsockopt");
        exit(1);
    }

    //initialize server address    
    struct sockaddr_in server;
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT_NUM);  
    memset(&server.sin_zero, 0, 8);
    server.sin_addr.s_addr = INADDR_ANY;

    // bind socket to an address
    if (bind(sock_fd, (struct sockaddr *) &server, sizeof(struct sockaddr_in)) == -1) {
      perror("server: bind");
      close(sock_fd);
      exit(1);
    } 


    // Set up a queue in the kernel to hold pending connections.
    if (listen(sock_fd, MAX_BACKLOG) < 0) {
        // listen failed
        perror("listen");
        exit(1);
    }
   
    struct sockaddr_in peer;
    unsigned int peer_len = sizeof(struct sockaddr_in);
    peer.sin_family = AF_INET;

    fprintf(stderr, "Waiting for a new connection...\n");
    int client_socket = accept(sock_fd, (struct sockaddr *)&peer, &peer_len);
    if (client_socket == -1) {
        perror("accept");
        return -1;
    } else {
        fprintf(stderr,
            "New connection accepted from %s:%d\n",
            inet_ntoa(peer.sin_addr),
            ntohs(peer.sin_port));
    }

    write(client_socket, "hello\r\n", 8);
    char line[10];
    read(client_socket, &line, 10);
    line[9] = '\0';
    printf("I read %s\n", line);

    return 0;
}


