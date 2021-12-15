import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("www.nikmaffi.cloud", 80))
    
    client.sendall("GET /immagine.png HTTP/1.1\nHost: www.nikmaffi.cloud\n\n".encode())
    print(client.recv(2 ** 16).decode())
    
    client.close()
    
if __name__ == "__main__":
    main()