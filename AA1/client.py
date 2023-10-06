import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

message = client.recv(2048).decode('utf-8')

print("Message from server: ", message)

