"""
MFF Protocol:

1-Hello   -> f"H:{name}"
2-Accept  -> f"A"
3-Refuse  -> f"R"
4-Send    -> f"S:{dest}:{mssg}"
"""

import socket
import sqlite3
import threading

# MFF protocol statements
HELLO_CODE = "H"
ACCEPT_CODE = "A"
REFUSE_CODE = "R"
SEND_CODE = "S"

SEPARATOR_CODE = ":"

BUFFER_SIZE = 4096
#------------------------

# Specials users code ----------
BROADCAST_CODE = "$broadcast"
SELF_CODE = "$self"
#-------------------------------

# Server access parameters
SERVER_IP = "0.0.0.0"
SERVER_PORT = 2118
#-------------------------

# Server management commands -------------------------------------------
serverCmds = {
    "HELP": ["$help", "Lists all server commands."],
    "LIST_ONLINE_USERS": ["$lsusr", "Lists all online users"],
    "SHOW_DATABASE": ["$showdb", "Lists all records in the database."],
    "STOP_SERVICE": ["$stop", "Ends the server process."]
}
#-----------------------------------------------------------------------

# Global variables -------------------------
dbConnection = None # Database connections
connections = {} # Connections dict
#-------------------------------------------

# Management of the connections
class AcceptManager(threading.Thread):
    def __init__(self, server):
        super().__init__(daemon=True)

        self.server = server # Socket server

    def run(self):
        # listen loop
        while True:
            self.server.listen()
            conn, addr = self.server.accept() # Connection accepted

            # Loading connection into the connections dict
            connections[f"{addr[0]}:{addr[1]}"] = ConnectionManager(conn, addr)
            # Start ConnectionManager thread
            connections[f"{addr[0]}:{addr[1]}"].start()

class ConnectionManager(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__(daemon=True)

        self.conn = conn # Client connection
        self.addr = addr # Client address (ip:port)
        self.name = ""   # Client username

    def run(self):
        # Communications loop
        while True:
            try:
                # Waiting messages from client
                mssg = self.conn.recv(BUFFER_SIZE).decode().split(SEPARATOR_CODE)
            except ConnectionError:
                # Client has disconnected

                # Open db connection
                dbConnection = sqlite3.connect("./data.db")
                # Execute query for delete client's ip address and port
                dbConnection.execute(f"UPDATE users SET ip_address='', port='' WHERE name='{self.name}';")
                dbConnection.commit()
                # Close db connecrtion
                dbConnection.close()

                # Remove connection from connections dict
                del connections[f"{self.addr[0]}:{self.addr[1]}"]

                # Exit from current loop
                break

            # Case -> HELLO message from client
            if mssg[0] == HELLO_CODE:
                # Search ip address and port of connected client from db
                dbConnection = sqlite3.connect("./data.db")
                data = list(dbConnection.execute(f"SELECT name, ip_address FROM users WHERE name='{mssg[1]}';"))
                dbConnection.close()

                # Case -> Client name is missing from db -> client has never connected
                if data == []:
                    self.name = mssg[1] # Extract client name

                    # Insert client name, ip and port into the db
                    dbConnection = sqlite3.connect("./data.db")
                    dbConnection.execute(f"INSERT INTO users VALUES ('{self.name}', '{self.addr[0]}', '{self.addr[1]}');")
                    dbConnection.commit()
                    dbConnection.close()

                    self.conn.sendall(ACCEPT_CODE.encode())
                # Case -> Only client ip and port are missing from db -> client has already connected
                elif data[0][1] == '':
                    self.name = mssg[1] # Extract client name

                    # Update client ip address and port
                    dbConnection = sqlite3.connect("./data.db")
                    dbConnection.execute(f"UPDATE users SET ip_address='{self.addr[0]}', port='{self.addr[1]}' WHERE name='{self.name}';")
                    dbConnection.commit()
                    dbConnection.close()

                    self.conn.sendall(ACCEPT_CODE.encode())
                # Case -> client is already in db -> client is attempting to use another client name
                else:
                    self.conn.sendall(REFUSE_CODE.encode())
            # Case -> SEND message from client
            elif mssg[0] == SEND_CODE:
                # Case Broadcast -> send client message to everyone
                if mssg[1] == BROADCAST_CODE:
                    for c in list(connections.values()):
                        if c.name == self.name:
                            continue
                        c.conn.sendall(f"{SEND_CODE}{SEPARATOR_CODE}{self.name}{SEPARATOR_CODE}{mssg[2]}".encode())
                # Case Self -> send client message to client itself
                elif mssg[1] == SELF_CODE:
                    self.conn.sendall(f"{SEND_CODE}{SEPARATOR_CODE}{self.name} - (my self){SEPARATOR_CODE}{mssg[2]}".encode())
                # Case -> send client message to another client
                else:
                    # Search client ip address and port from db
                    dbConnection = sqlite3.connect("./data.db")
                    data = list(dbConnection.execute(f"SELECT * FROM users WHERE name='{mssg[1]}';"))
                    dbConnection.close()

                    if data != [] and data[0][1] != '':
                        # Send message to destination client
                        connections[f"{data[0][1]}:{data[0][2]}"].conn.sendall(f"{SEND_CODE}{SEPARATOR_CODE}{self.name}{SEPARATOR_CODE}{mssg[2]}".encode())
                    else:
                        # Send error: destination client not found
                        self.conn.sendall(f"{SEND_CODE}{SEPARATOR_CODE}server{SEPARATOR_CODE}Error -> Can't find {mssg[1]}!".encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))

    acceptManager = AcceptManager(server)
    acceptManager.start()

    print(f"Type {serverCmds['HELP'][0]} to list all commands.")

    while True:
        cmd = input("\nroot@serverMFF-$ ")

        if cmd == serverCmds["HELP"][0]:
            print("Server commands:")

            for c in list(serverCmds.values()):
                print(f"{c[0]}\n\t-{c[1]}\n")
        elif cmd == serverCmds["STOP_SERVICE"][0]:
            dbConnection = sqlite3.connect("./data.db")
            dbConnection.execute(f"UPDATE users SET ip_address='', port='';")
            dbConnection.commit()
            dbConnection.close()
            
            print("Termination of the service in progress.")

            break
        elif cmd == serverCmds["LIST_ONLINE_USERS"][0]:
            dbConnection = sqlite3.connect("./data.db")
            data = list(dbConnection.execute(f"SELECT name FROM users WHERE ip_address<>'' ORDER BY port;"))
            dbConnection.close()

            print("Current online users:")
            for rec in data:
                print(f"\t-{rec[0]}")
        elif cmd == serverCmds["SHOW_DATABASE"][0]:
            dbConnection = sqlite3.connect("./data.db")
            data = list(dbConnection.execute(f"SELECT * FROM users ORDER BY name;"))
            dbConnection.close()

            print("Database:\n")
            for rec in data:            
                for fld in rec:
                    print(f"{fld.ljust(20)} ", end="")
                print()
        else:
            print("Bad command. Retry!")

    #acceptManager.join()

    #for c in list(connections.values()):
        #c.join()

    server.close()

if __name__ == "__main__":
    main()