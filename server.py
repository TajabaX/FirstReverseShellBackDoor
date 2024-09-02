import sys
import socket

#Enter your server
SERVER_IP = ""
#Enter The Port you want it to listen
PORT = 4444

#Creating a socket object
s = socket.socket()

#Configutrating the socket that I just created by making it not waiting for established connection
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Adding the port and server to the socket object
s.bind((SERVER_IP, PORT))

#making sure it will only listen to 1 connection. due to confusion.
s.listen(1)

while True:
    # Print the server's listening status with the IP address and port
    print(f'[+] listening as {SERVER_IP}:{PORT}')

    # Accept a new client connection
    client = s.accept()
    # Print the address of the connected client
    print(f'[+] client connected {client[1]}')

    # Send a connection confirmation message to the client
    client[0].send('connected'.encode())

    while True:
        # Prompt the user to input a command
        cmd = input('>>> ')
        # Send the command to the client
        client[0].send(cmd.encode())

        # If the command is one of the exit commands, break the inner loop
        if cmd.lower() in ['quit', 'exit', 'q', 'x']:
            break

        # Receive and decode the client's response
        result = client[0].recv(1024).decode()
        # Print the client's response
        print(result)

    # Close the connection with the current client
    client[0].close()

    # Ask the user if they want to wait for a new client
    cmd = input('Wait for new client y/n') or 'y'
    # If the user's response indicates they don't want to wait, break the outer loop
    if cmd.lower() in ['n', 'no']:
        break

# Close the server socket
s.close()
