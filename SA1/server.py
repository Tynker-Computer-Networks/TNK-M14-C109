# Import socket library
import socket

# Create a server using socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create variable ip_address and port and assign them values '127.0.0.1' and 8000 respectively
ip_address = '127.0.0.1'
port = 8000

# Call bind method from server object to assign ip and port to the server
server.bind((ip_address, port))
# Call listen method so that server starts listening to requests
server.listen()

# Print "Server has started..."
print("Server has started...")