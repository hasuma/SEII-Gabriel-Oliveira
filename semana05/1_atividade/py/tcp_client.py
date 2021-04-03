# TCP/IP - CLIENT
import argparse
import os
import socket

import tqdm

SEPARATOR = "<SEPARATOR>"
host = 'localhost'
BUFFER_SIZE = 1024  # send 4096 bytes each time step


def echo_client(port, filename):
    filesize = os.path.getsize(filename)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    try:
        # Send data
        sock.send(f"{filename}{SEPARATOR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize),
                             f"Sending {filename}",
                             unit="B",
                             unit_scale=True,
                             unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # we use sendall to assure transimission in busy networks
                sock.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
        # close the socket
        sock.close()
        # Look for the response

    except socket.error as e:
        print("Socket error: %s" % str(e))

    except Exception as e:
        print("Other exception: %s" % str(e))

    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client')
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
    echo_client(port, filename)
