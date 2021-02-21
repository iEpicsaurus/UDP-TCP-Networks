import socket

UDP_IP = "127.0.0.1" # address for loopback adapter
UDP_PORT = 5005      # port number

udpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creates a UDP socket

request = input("Type your request: ") # prompts user for request
udpClientSocket.sendto(request.encode(), (UDP_IP, UDP_PORT)) # sends request to the specified IP/PORT (to the server)

data, address = udpClientSocket.recvfrom(4096) # receives appropriate response from the server (from specified IP/PORT)
print(data.decode()) # prints response (from server) to the terminal