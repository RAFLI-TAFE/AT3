# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:34:40 2024

@author: Rafli (20115423)

Part A Unittest
"""

import unittest # Importing the unittest module for unit testing
import os # Importing os module to interact with the file system
import time # Importing time module to handle delays
from manage_pdf import merge_pdfs, rotate_page, encrypt_pdf, decrypt_pdf, create_sample_pdf # Importing functions from manage_pdf

class TestPDFManager(unittest.TestCase):

    def setUp(self):
        self.pdf_files = [] # List to store names of generated sample PDF files
        for i in range(2): # Create two sample PDFs for testing
            file_name = f'test_sample_{i + 1}.pdf' # Naming each sample PDF
            create_sample_pdf(file_name, f'This is test sample PDF number {i + 1}.') # Create PDF with specified text
            self.pdf_files.append(file_name) # Add the generated PDF name to the list
 
    def tearDown(self):
        for file in self.pdf_files: # Iterate through the list of test sample PDFs
            for attempt in range(1):  # One attempt for each file
                try:
                    if os.path.isfile(file): # Check if file exists
                        os.remove(file) # Delete the file if it exists
                    break  # Break if successful
                except PermissionError:
                    print(f"PermissionError: could not remove {file}, retrying...") # Print error message if deletion fails
                    time.sleep(0.1)  # Wait before retrying

        # Repeat for other specific files
        for specific_file in ['MergedPDF.pdf', 'NewRotate.pdf', 'encrypted_output.pdf', 'decrypted_output.pdf']:
            for attempt in range(1):  # One attempt for each file
                try:
                    if os.path.isfile(specific_file): # Checking if the file exists
                        os.remove(specific_file) # Delete the file if it exists
                    break  # Break if successful
                except PermissionError:
                    print(f"PermissionError: could not remove {specific_file}, retrying...")
                    time.sleep(0.1)  # Wait before retrying

    # Test the merge action
    def test_merge_pdfs(self):
        merge_pdfs(self.pdf_files, 'MergedPDF.pdf') # Calling merge function on sample PDFs
        self.assertTrue(os.path.isfile('MergedPDF.pdf'))  # Verify if merged PDF file was created

    # Test the rotate action
    def test_rotate_page(self):
        rotate_page(self.pdf_files[0], 1, 90)  # Rotating the first page of the first PDF
        self.assertTrue(os.path.isfile('NewRotate.pdf')) # Verifying if rotated PDF file was created

    # Test the encrypting action
    def test_encrypt_pdf(self):
        encrypt_pdf(self.pdf_files[0], 'testpassword') # Encrypting the first sample PDF with a password
        self.assertTrue(os.path.isfile('encrypted_output.pdf')) # Verifying if encrypted PDF file was created

    # Test the decrypting action
    def test_decrypt_pdf(self):
        encrypt_pdf(self.pdf_files[0], 'testpassword')  # First encrypt it
        decrypt_pdf('encrypted_output.pdf', 'testpassword') # Decrypting the encrypted PDF with the correct password
        self.assertTrue(os.path.isfile('decrypted_output.pdf')) # Verifying if decrypted PDF file was created


if __name__ == '__main__':
    unittest.main()
