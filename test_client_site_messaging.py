# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:12:08 2024

@author: Rafli (20115423)
Part C: Unittest for Client_site_messaging
"""

import unittest # Import unittest library for testing
from unittest.mock import patch, MagicMock 
import client_site_messaging  # Import the client module

class TestClientSiteMessaging(unittest.TestCase):
    
    @patch('client_site_messaging.socket.socket')
    def test_client_site_connection(self, mock_socket):
        # Create a mock socket instance to simulate a real socket
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance  # Set mock socket as the return value
        
        # Mock the connect and recv methods on the socket instance
        mock_socket_instance.connect.return_value = None  # Pretend connect() works fine
        mock_socket_instance.recv.return_value = b'Hello from server!'  # Server response simulation

        # Use patch to simulate user input for the messages "Hello" and "exit"
        with patch('builtins.input', side_effect=['Hello', 'exit']):
            client_site_messaging.client_site()  # Run the client function to test connection

        # Verify connect was called with the right server address and port
        mock_socket_instance.connect.assert_called_with(('localhost', 1234))

        # Check if messages "Hello" and "exit" were sent to the server
        mock_socket_instance.sendall.assert_any_call(b'Hello')  # Check "Hello" message
        mock_socket_instance.sendall.assert_any_call(b'exit')   # Check "exit" message

        # Confirm that the client closed the socket at the end
        mock_socket_instance.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
