import socket
from datetime import datetime

TCP_IP = '127.0.0.1' # address for loopback adapter
TCP_PORT = 5005      # port server will listen to

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a TCP socket
serverSocket.bind((TCP_IP, TCP_PORT)) # associates/binds servSocket to loopback address & port number

while True: # while loop is used to meet specifications of server being able to service other clients afterwards

	serverSocket.listen(1) # server is listening for connections; allows maxiumum 1
	conn, addr = serverSocket.accept() # server actually accepts connection; new socket (conn) used to send/receive messages
	
	data = conn.recv(4096) # server receives request from the client

	if (data.decode() != "What is the current date and time?"): # check for valid request

		message = "Invalid Request"
		conn.sendall(message.encode()) # if invalid request from client, send invalid response to the client

	else: # request from client is valid
	
		currentDateTime = datetime.now() # creates object with date and time
		dateFormatted = currentDateTime.strftime("%m/%d/%Y %H:%M:%S") # formats date and time to specifications
		fullData = ("Current Date and Time - " + dateFormatted) # includes beginning part of the string
		conn.sendall(fullData.encode()) # send date and time response to the client