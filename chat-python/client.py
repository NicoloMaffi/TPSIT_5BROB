"""
Protocollo MFF:

1-Hello   -> f"H:{name}"
2-Accept  -> f"A"
3-Refuse  -> f"R"
4-Send    -> f"S:{dest}:{mssg}"
"""

import socket
import threading

# MFF protocol statements
HELLO_CODE = "H"
ACCEPT_CODE = "A"
REFUSE_CODE = "R"
SEND_CODE = "S"

SEPARATOR_CODE = ":"

BUFFER_SIZE = 4096
#------------------------

# Server access parameters
SERVER_IP = "127.0.0.1"
SERVER_PORT = 2118
#-------------------------

# Client management commands ------
clientCmds = {
    "HELP": ["$help", "Lists all commands."],
    "STOP": ["$stop", "Ends the client app."],
    "BROADCAST": ["$broadcast", "Special user: send message to all users available."],
    "SELFCAST": ["$self", "Special user: send message to yourself."]
}
#----------------------------------

class Listener(threading.Thread):
    def __init__(self, client, name):
        super().__init__(daemon=True)

        self.name = name
        self.client = client

    def run(self):
        while True:
            mssg = self.client.recv(BUFFER_SIZE).decode().split(SEPARATOR_CODE)

            if mssg[0] == SEND_CODE:
                f = open(f"{self.name}.txt", "a")
                f.write(f"Messagge From: {mssg[1]}\n{mssg[2]}\n\n")
                f.close()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    while True:
        name = input("Enter your name: ")
        client.sendall(f"{HELLO_CODE}{SEPARATOR_CODE}{name}".encode())

        mssg = client.recv(BUFFER_SIZE).decode()

        if mssg == REFUSE_CODE:
            print("Please enter a different name!")
        else:
            break;

    listener = Listener(client, name)
    listener.start()

    print(f"Type {clientCmds['HELP'][0]} to list all commands.")

    while True:
        dest = input(f"\nDestination name: ")

        if dest == clientCmds['HELP'][0]:
            print("Commands:")

            for c in list(clientCmds.values()):
                print(f"{c[0]}\n\t-{c[1]}\n")
        elif dest == clientCmds['STOP'][0]:
            print("Termination of the service in progress.")

            break
        else:
            mssg = input("Message: ")

            client.sendall(f"{SEND_CODE}{SEPARATOR_CODE}{dest}{SEPARATOR_CODE}{mssg}".encode())

    #listener.join()

    client.close()

if __name__ == "__main__":
    main()