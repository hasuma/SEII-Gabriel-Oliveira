# TCP/IP - SERVER

import argparse
import os
import socket
import sys

import tqdm

host = 'localhost'
backlog = 5
BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"


def echo_server(port, filename):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)

    # Listen to clients, backlog argument specifies the max no.
    # of queued connections
    sock.listen(backlog)
    client_socket, address = sock.accept()
    print(f"Connecting to {address}")

    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename_input, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    # filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)
    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize),
                         f"Receiving {filename}",
                         unit="B",
                         unit_scale=True,
                         unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the client socket
    client_socket.close()
    # close the server socket
    sock.close()
    # end connection


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server')
    parser.add_argument('--port',
                        action="store",
                        dest="port",
                        type=int,
                        required=True)
    parser.add_argument('--filename',
                        action="store",
                        dest="filename",
                        type=str,
                        required=True)
    given_args = parser.parse_args()
    port = given_args.port
    filename = given_args.filename

    echo_server(port, filename)
