# TCP/IP - CLIENT
import argparse
import random
import socket
from datetime import datetime
from threading import Thread

from colorama import Back, Fore, init

SEPARATOR_TOKEN = "<SEPARATOR>"
# init colors
init()

# set the available colors
colors = [
    Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA,
    Fore.RED, Fore.WHITE, Fore.YELLOW
]
# choose a random color for the client
client_color = random.choice(colors)


def client(port, host, name):
    SERVER_HOST = host
    SERVER_PORT = port  # server's port
    # initialize TCP socket
    s = socket.socket()
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    # connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    def listen_for_messages():
        while True:
            message = s.recv(1024).decode()
            print("\n" + message)
    # make a thread that listens for messages to this client & print them
    t = Thread(target=listen_for_messages)
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

    while True:
        # input message we want to send to the server
        to_send = input()
        # a way to exit the program
        if to_send.lower() == 'q':
            break
        # add the datetime, name & the color of the sender
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        to_send = f"{client_color}[{date_now}] {name}{SEPARATOR_TOKEN}{to_send}{Fore.RESET}"
        # finally, send the message
        s.send(to_send.encode())

    # close the socket
    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client')
    parser.add_argument('--port',
                        action="store",
                        dest="port",
                        type=int,
                        required=True)
    parser.add_argument('--host',
                        action="store",
                        dest="host",
                        type=str,
                        required=True)
    parser.add_argument('--name',
                        action="store",
                        dest="name",
                        type=str,
                        required=True)
    given_args = parser.parse_args()
    port = given_args.port
    host = given_args.host
    name = given_args.name
    client(port, host, name)
