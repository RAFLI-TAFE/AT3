# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:22:32 2024

@author: Rafli (20115423)

Part A 
In the first part of this assessment, you must design, code, and test a program that uses Python to manage PDF files. 
1. Write a Python program that provides the ability to: 
1.1. Merge at least two PDF files into one. Use list data structure with at least two PDF files. As an optional bonus you can create an empty list and ask for user input to populate empty list with user-defined PDF files.
1.2. Rotate a page in PDF file.
1.3. Encrypt PDF file.
1.4. Decrypt PDF file.
"""

# Importing required libraries
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_sample_pdf(file_name, text):
    """Create a PDF file with specified text."""
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

# List to store names of created PDFs
listofpdf = []

# Number of PDFs to create
num_pdfs = 2  # Change this to the desired number

for i in range(num_pdfs):
    file_name = f'sample{i + 1}.pdf'  # Naming the PDFs
    text = f'This is sample PDF number {i + 1}.'
    create_sample_pdf(file_name, text)
    listofpdf.append(file_name)  # Add the file name to the list

# Output the list of created PDF names
print("Created PDF files:", listofpdf)

# Merge multiple PDFs into one file
def merge_pdfs(pdf_list, output_file):
    """Merge multiple PDF files into one."""
    pdf_writer = PyPDF2.PdfWriter()  # This writer object will create the new PDF

    for pdf in pdf_list:
        try:
            with open(pdf, 'rb') as pdf_file:  # Open each PDF in 'read-binary' mode
                pdf_reader = PyPDF2.PdfReader(pdf_file)  # Create a reader to read each PDF
                for page in pdf_reader.pages:  # Adding each page in the PDF to the writer object
                    pdf_writer.add_page(page)

            print(f"Added {pdf} to the merge list.")
        except Exception as e:
            print(f"An error occurred while processing {pdf}: {e}")

    # Saving the combined pages to a new file
    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)  # Write all pages into one PDF
    print(f"PDFs merged into '{output_file}'.")

# Rotate a page in a PDF by a specified degree
def rotate_page(pdf_file, page_number, degrees):
    """Rotate a specified page in a PDF file by a given degree."""
    try:
        with open(pdf_file, 'rb') as rotate_file:  # Open the PDF file to rotate
            pdf_reader = PyPDF2.PdfReader(rotate_file)  # Use the reader to access the PDF's content
            pdf_writer = PyPDF2.PdfWriter()  # Writer to save rotated content

            # Check if the page number is valid
            if page_number < 1 or page_number > len(pdf_reader.pages):
                raise ValueError("Invalid page number. Make sure the page number exists.")

            for i, page in enumerate(pdf_reader.pages):
                if i == page_number - 1:  # If we are at the page to rotate
                    page.rotate(degrees)  # Rotating the page

                pdf_writer.add_page(page)  # Add each page to the writer

            # Save the new rotated PDF as 'NewRotate.pdf'
            with open('NewRotate.pdf', 'wb') as result_pdf_file:
                pdf_writer.write(result_pdf_file)
            print("Rotated page saved as 'NewRotate.pdf'.")  # Confirm rotation

    except Exception as e:
        print(f"An error occurred while rotating the page: {e}")

# Add password protection to a PDF for encryption
def encrypt_pdf(pdf_file, password):
    """Encrypt a PDF file with a password."""
    try:
        pdf_reader = PyPDF2.PdfReader(open(pdf_file, 'rb'))  # Open the PDF to be encrypted
        pdf_writer = PyPDF2.PdfWriter()  # Create a writer to save the encrypted PDF

        for page in pdf_reader.pages:  # Loop through all pages in the original PDF and add them to the writer
            pdf_writer.add_page(page)

        pdf_writer.encrypt(password)  # Set the password protection on the PDF

        # Save the encrypted PDF as 'encrypted_output.pdf'
        with open('encrypted_output.pdf', 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print("PDF encrypted as 'encrypted_output.pdf'.")  # Confirm encryption

    except Exception as e:
        print(f"An error occurred while encrypting the PDF: {e}")

# Removing password protection from a PDF
def decrypt_pdf(encrypted_pdf_file, password):
    """Decrypt an encrypted PDF file with the provided password."""
    try:
        pdf_reader = PyPDF2.PdfReader(open(encrypted_pdf_file, 'rb'))  # Open the encrypted PDF

        # Checking if the PDF is encrypted
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)  # Try to unlock the PDF using the given password

        pdf_writer = PyPDF2.PdfWriter()  # Create a writer to save the decrypted PDF

        for page in pdf_reader.pages:  # Loop through all pages in the decrypted PDF and add them to the writer
            pdf_writer.add_page(page)

        # Save the decrypted PDF as 'decrypted_output.pdf'
        with open('decrypted_output.pdf', 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print("PDF decrypted as 'decrypted_output.pdf'.")  # Confirm decryption

    except Exception as e:
        print(f"An error occurred while decrypting the PDF: {e}")

def play():
    """Start of the main function."""
    while True:  # Keep the program running until the user exits
        action = input("Enter function to run: 'merge', 'rotate', 'encrypt', 'decrypt', or 'exit': ")

        if action.lower() == 'exit':  # If user chose to exit
            print("Exiting program...")  # Show exit message
            break  # Stop the loop to exit

        elif action.lower() == 'merge':  # If user chose to merge PDFs
            pdf_list = []  # List to store PDF files
            print("Enter PDF paths to merge. Type 'done' after adding 2+ files.")  # Instructions

            while True:  # Loop to add multiple PDFs
                pdf_file = input("PDF file path: ")  # Get PDF file path

                if pdf_file.lower() == 'done':  # If user is done adding files
                    if len(pdf_list) < 2:  # If fewer than 2 files were added
                        print("Add at least two PDFs.")  # Reminder for minimum files
                    else:  # If enough files are added
                        break  # Exit this loop
                else:
                    if os.path.isfile(pdf_file):  # Check if the file exists
                        pdf_list.append(pdf_file)  # Add file to the list
                    else:
                        print(f"File '{pdf_file}' does not exist. Please try again.")  # Error message

            merge_pdfs(pdf_list, 'MergedPDF.pdf')  # Call merge function

        elif action.lower() == 'rotate':  # If user chose to rotate a page
            pdf_file = input("Enter the PDF file path: ")  # Get PDF file path
            page_num = input("Enter the page number to rotate: ")  # Get page number
            degrees = input("Enter degrees to rotate (90, 180, 270): ")  # Get rotation degrees

            # Input validation for page number and degrees
            try:
                page_num = int(page_num)  # Convert to integer
                degrees = int(degrees)  # Convert to integer
                if degrees not in [90, 180, 270]:  # Check if the degrees are valid
                    raise ValueError("Invalid rotation degrees. Must be 90, 180, or 270.")
                rotate_page(pdf_file, page_num, degrees)  # Call rotate function
            except ValueError as e:
                print(f"Input error: {e}")  # Error message

        elif action.lower() == 'encrypt':  # If user chose to encrypt
            pdf_file = input("Enter the PDF file path: ")  # Get PDF file path
            password = input("Enter a password: ")  # Get password

            if os.path.isfile(pdf_file):  # Check if the file exists
                encrypt_pdf(pdf_file, password)  # Call encrypt function
            else:
                print(f"File '{pdf_file}' does not exist. Please try again.")  # Error message

        elif action.lower() == 'decrypt':  # If user chose to decrypt
            pdf_file = input("Enter the encrypted PDF file path: ")  # Get PDF file path
            password = input("Enter the password: ")  # Get password

            if os.path.isfile(pdf_file):  # Check if the file exists
                decrypt_pdf

if __name__ == '__main__':
    play()