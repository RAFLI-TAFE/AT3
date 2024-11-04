# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:18:18 2024

@author: Rafli (20115423)
Part C: Unittest for Server_site_messaging
"""

import unittest # Import unittest library for testing
import socket # Import socket library to create server and client sockets
import threading # Import threading to run server and client at the same time
import server_site_messaging  # Replace with the actual module name where your server code is located

class TestServerSite(unittest.TestCase):

    def test_server_bind(self):
        # Test if the server can bind to localhost and port 1234
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            server_socket.bind(('localhost', 0))  # Try to bind to the server IP and port
            self.assertTrue(True)  # Passes if no exception is raised
        except Exception as e:
            self.fail(f"Binding failed with error: {e}")  # Fail the test if binding raises an error
        finally:
            server_socket.close()  # Close the server socket after test

    def test_server_accept_connection(self):
        # Test if server can accept a client connection
        def run_server():
            server_site_messaging.server_site()  # Run the server function from your module

        # Start server in a new thread to allow client connection
        server_thread = threading.Thread(target=run_server)
        server_thread.start()

        # Create a client socket to connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 1234))  # Client connects to localhost at port 1234
        
        # Check that the client can successfully connect
        self.assertTrue(client_socket)  # Passes if client_socket is connected
        
        client_socket.sendall(b'exit')  # Send 'exit' to end the connection
        client_socket.close()  # Close client socket
        
        # Join the server thread to ensure it stops
        server_thread.join()

if __name__ == '__main__':
    unittest.main()
