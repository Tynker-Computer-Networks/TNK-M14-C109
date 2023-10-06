import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []

print("Server has started...")

while True:
    conn, addr = server.accept()
    # Get the count of clients in clientCount variable
    clientCount = len(clients)+1
    # Print count of clients when a new client connects to a server
    print(clientCount ,"Client connected")
    clients.append(conn)

    conn.send("Thank you for connecting".encode())
    conn.close()