# Import socket
import socket

# Create a socket named client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create ip_address and port variables that contains the respective values of the server to be connect to
ip_address = '127.0.0.1'
port = 8000

# Call connect method to connect to the server
client.connect((ip_address, port))

# Print connected to the server
print("Connected with the server...")

# Use recv method to receive response from the server and save the returned value in message variable
message = client.recv(2048).decode('utf-8')

# Print the message
print("Message from server: ", message)

