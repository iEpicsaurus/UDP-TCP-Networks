# UDP TCP Networks
 Networked date & time server and a client to access the server. UDP and TCP implementations.

 Basic Interaction

- Server listens for incoming client requests.
- Client connects (only for TCP) to server and sends ASCII request “What is the current date and time?”
- Server responds with the current date and time in the format  “Current Date and Time – 09/29/2019 09:00:01”
- Client closes connection (only for TCP), server stays running listening for next connection.

Detailed Requirements

Server

- Only required to handle one client interaction at a time
- Can listen on any port you choose
- Must respond to invalid requests with an error message
- Valid request is “What is the current date and time?”
- Response to valid request must be in the format: “Current Date and Time – MM/DD/YYYY hh:mm:ss”

Client

- Allows user to enter text commands to be sent to the server
- Displays response back from server