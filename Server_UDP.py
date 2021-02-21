import socket
from datetime import datetime

UDP_IP = "127.0.0.1" # address for loopback adapter
UDP_PORT = 5005      # port number

udpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creates a UDP socket
udpServerSocket.bind((UDP_IP, UDP_PORT)) # associates IP and PORT to the server socket

while True: # infinite loop - whenever requests are recieved, server will process these requests

	data, address = udpServerSocket.recvfrom(4096) # receives data (from the client)

	if (data.decode() != "What is the current date and time?"): # checks for valid request

		message = "Invalid Request"
		udpServerSocket.sendto(message.encode(), address) # if invalid request (from client), send invalid response to the address request was received from (client)

	else: # request (from client) is valid

		currentDateTime = datetime.now() # creates object with date and time
		dateFormatted = currentDateTime.strftime("%m/%d/%Y %H:%M:%S") # formats date and time to specification
		fullData = ("Current Date and Time - " + dateFormatted) # includes beginning part of the string
		udpServerSocket.sendto(fullData.encode(), address) # send date and time response to the address request was received from (client)