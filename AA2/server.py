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
    clientCount = len(clients)+1

    print(clientCount ,"Client connected")
    clients.append(conn)

    # Receive message from client
    message = conn.recv(2048).decode('utf-8')
    print("Message from client: ", message)

    conn.send("Thank you for connecting".encode())
    conn.close()

    