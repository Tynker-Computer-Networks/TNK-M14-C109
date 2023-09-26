import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

print("Server has started...")

# Create an infinite while loop
while True:
    # Call server.accept() method ans receive two values in conn and addr variables
    conn, addr = server.accept()
    
    # Use conn.send to send encoded message to a new client
    conn.send("Thank you for connecting".encode())
    # Close the connection
    conn.close()