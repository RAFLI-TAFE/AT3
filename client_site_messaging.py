# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:05:12 2024

@author: Rafli (20115423)
Part C: Client_site_messaging
"""

import socket  # Import the socket library

def client_site(): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Make a new TCP/IP socket
    
    client_socket.connect(('localhost', 1234)) # Connect to the server at localhost and port 1234
    print("Client is connected to the server at localhost:1234.")
    

    # Keep the conversation going until someone says 'exit'
    while True: 
        message = input("Type message for server (or 'exit' to quit): ") # Type and send a message to the server
        client_socket.sendall(message.encode('utf-8'))
        
        if message.lower() == 'exit': # If client says 'exit', stop
            print("Client is ending the connection.")
            break
        
        response = client_socket.recv(1024).decode('utf-8') # Get a reply from the server
        
        if response.lower() == 'exit': # If server says 'exit', stop
            print("Server ended the connection.")
            break
        
        print(f"Server replies: {response}") # Print server's reply
    
    client_socket.close() # Close the client connection
    print("Client is disconnected.")

def play():
    # Start the server
    print("Starting the server...")
    client_site()

# Run the main function
if __name__ == "__main__":
    play()
