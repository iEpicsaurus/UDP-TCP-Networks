import socket

TCP_IP = '127.0.0.1' # address for loopback adapter
TCP_PORT = 5005      # port number

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a TCP socket
clientSocket.connect((TCP_IP, TCP_PORT)) # client connects to the specified IP/PORT (server)

request = input("Type your request: ") # prompts user for request
clientSocket.sendall(request.encode()) # sends request to server

data = clientSocket.recv(4096) # receives appropriate response from server

print(data.decode()) # prints the response from the server to terminal

clientSocket.close() # client closes its connection to the server