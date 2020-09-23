#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>    /* Internet domain header */
#include <arpa/inet.h>     /* only needed on my mac */
#include <netdb.h>         /* gethostname */

#define PORT_NUM 30000

int main(int argc, char **argv) {

    if (argc != 2) {
        fprintf(stderr, "Usage: simple_client hostname\n");
        exit(1);
    }
    char *hostname = argv[1];


    int soc = socket(AF_INET, SOCK_STREAM, 0);
    if (soc < 0) {
        perror("socket");
        exit(1);
    }
    struct sockaddr_in addr;

    // Allow sockets across machines.
    addr.sin_family = AF_INET;

    // The port the server will be listening on.
    addr.sin_port = htons(PORT_NUM);
    
    // Clear this field; sin_zero is used for padding for the struct.
    memset(&(addr.sin_zero), 0, 8);

    // Lookup host IP address.
    struct hostent *hp = gethostbyname(hostname);
    if (hp == NULL) {
        fprintf(stderr, "unknown host %s\n", hostname);
        exit(1);
    }

    addr.sin_addr = *((struct in_addr *) hp->h_addr);

    // Request connection to server.
    if (connect(soc, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("connect");
        exit(1);
    }

    if (write(soc, "Hello Internet\r\n", 17) == -1) {
        perror("write");
        exit(1);
    }

    char buf[10];
    if (read(soc, buf, sizeof(buf)) <= 0) {
        perror("read");
        exit(1);
    }

    printf("Server response: %s\n", buf);

        // Clean up.
    close(soc);
    return 0;
}
