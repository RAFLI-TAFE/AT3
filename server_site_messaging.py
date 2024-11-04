# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:50:23 2024

@author: Rafli (20115423)
Part C: Server_site_messaging
"""

import socket  # Import the socket library

def server_site():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Make a new socket
    
    server_socket.bind(('localhost', 1234)) # Bind it to localhost and port 1234
    
    server_socket.listen(1) # Listen for any incoming connections (1 at a time)
    print("Server is now waiting for a connection on port 1234...")
    
    connection, client_address = server_socket.accept() # Accept a connection when it comes
    print(f"Connected to client at {client_address}")
    
    # Keep the conversation going until someone says 'exit'
    while True: 
        message = connection.recv(1024).decode('utf-8') # Get a message from the client
        
        if message.lower() == 'exit': # If client says 'exit', stop
            print("Client disconnected.")
            break
        
        print(f"Client says: {message}") # Print the client's message
        
        response = input("Reply to client (or type 'exit' to end): ") # Send a response back to the client
        connection.sendall(response.encode('utf-8'))
        
        if response.lower() == 'exit': # If server says 'exit', stop
            print("Server is ending the conversation.")
            break
    
    connection.close() # Close the server connection
    server_socket.close()
    print("Server is shut down.")

def play():
    # Start the server
    print("Starting the server...")
    server_site()

# Run the main function
if __name__ == "__main__":
    play()
