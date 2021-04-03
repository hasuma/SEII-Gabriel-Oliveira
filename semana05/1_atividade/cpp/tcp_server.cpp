// TCP/IP - SERVER
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
#include "Aux.h"

using namespace std;

static const int MAXPENDING = 5; // Maximum outstanding connection requests


void HandleTCPClient(int clntSocket, char *outPathFile) {
    char buffer[BUFSIZE]; // Buffer for echo string
    char msgConfirm[] = "Received file";
    size_t msgConfirmLen = strlen(msgConfirm); // Determine message length
    remove(outPathFile);
    ofstream outFile{outPathFile};
    if (!outFile) {
	cerr << "Output file \"%s\" don\'t created" << outPathFile << endl;
	exit(1);
    }
    
    // Receive message from client
    ssize_t numBytesRcvd; 
    do{
        // See if there is more data to receive
        numBytesRcvd = recv(clntSocket, buffer, BUFSIZE, 0);
        if (numBytesRcvd < 0)
            DieWithSystemMessage("recv() failed");
	else{
    		//printf("From Client - After: %s\n", buffer);
    		outFile.write(buffer,numBytesRcvd);
    	}
    	
    	// Echo message back to client
        ssize_t numBytesSent = send(clntSocket, msgConfirm, msgConfirmLen, 0);
        if (numBytesSent < 0)
            DieWithSystemMessage("send() failed");
        else
    	    printf("Message confirm successfully send to the client...\n");
    }while (numBytesRcvd >= BUFSIZE);// 0 indicates end of stream
    
    outFile.close();
    printf("File Successfully received...\n");
    close(clntSocket); // Close client socket
    exit(1);
}


int main(int argc, char *argv[]) 
{
    if (argc != 3) // Test for correct number of arguments
    DieWithUserMessage("Parameter(s)", "<Server Port> <Output file name>");

    in_port_t servPort = atoi(argv[1]); // First arg:  local port
    char *outPathFile = argv[2];
    // Create socket for incoming connections
    int servSock; // Socket descriptor for server
    if ((servSock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
        DieWithSystemMessage("socket() creation failed...");
    else
    	printf("socket() successfully created...\n");
    	
    // Construct local address structure	
    struct sockaddr_in servAddr;                  // Local address
    memset(&servAddr, 0, sizeof(servAddr));       // Zero out structure
    servAddr.sin_family = AF_INET;                // IPv4 address family
    servAddr.sin_addr.s_addr = htonl(INADDR_ANY); // Any incoming interface
    servAddr.sin_port = htons(servPort);          // Local port

    // Bind to the local address
    if (bind(servSock, (struct sockaddr*) &servAddr, sizeof(servAddr)) < 0)
        DieWithSystemMessage("bind() failed");
    else
    	printf("socket() successfully binded...\n");
    // Mark the socket so it will listen for incoming connections
    if (listen(servSock, MAXPENDING) < 0)
        DieWithSystemMessage("listen() failed");
    else
    	printf("Server listening...\n");
    // Run forever
    for (;;) 
    { 
        struct sockaddr_in clntAddr; // Client address
        // Set length of client address structure (in-out parameter)
        socklen_t clntAddrLen = sizeof(clntAddr);

        // Wait for a client to connect
        int clntSock = accept(servSock, (struct sockaddr *) &clntAddr, &clntAddrLen);
        if (clntSock < 0)
            DieWithSystemMessage("accept() failed");
	else
	    printf("Server accept the client...\n");
        // clntSock is connected to a client!

        char clntName[INET_ADDRSTRLEN]; // String to contain client address
        if (inet_ntop(AF_INET, &clntAddr.sin_addr.s_addr, clntName,
            sizeof(clntName)) != NULL)
            printf("Handling client %s/%d\n", clntName, ntohs(clntAddr.sin_port));
        else
            puts("Unable to get client address");
            
        HandleTCPClient(clntSock, outPathFile);
    }
    
    return 0;
}
