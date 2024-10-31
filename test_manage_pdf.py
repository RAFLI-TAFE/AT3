import unittest
import os
import time
from manage_pdf import merge_pdfs, rotate_page, encrypt_pdf, decrypt_pdf, create_sample_pdf

class TestPDFManager(unittest.TestCase):

    def setUp(self):
        """Create sample PDF files for testing."""
        self.pdf_files = []
        for i in range(2):
            file_name = f'test_sample_{i + 1}.pdf'
            create_sample_pdf(file_name, f'This is test sample PDF number {i + 1}.')
            self.pdf_files.append(file_name)

    def tearDown(self):
        """Remove created PDF files after tests."""
        for file in self.pdf_files:
            for attempt in range(3):  # Retry a few times
                try:
                    if os.path.isfile(file):
                        os.remove(file)
                    break  # Break if successful
                except PermissionError:
                    print(f"PermissionError: could not remove {file}, retrying...")
                    time.sleep(0.1)  # Wait before retrying

        # Repeat for other specific files
        for specific_file in ['MergedPDF.pdf', 'NewRotate.pdf', 'encrypted_output.pdf', 'decrypted_output.pdf']:
            for attempt in range(3):  # Retry a few times
                try:
                    if os.path.isfile(specific_file):
                        os.remove(specific_file)
                    break  # Break if successful
                except PermissionError:
                    print(f"PermissionError: could not remove {specific_file}, retrying...")
                    time.sleep(0.1)  # Wait before retrying

    def test_merge_pdfs(self):
        """Test merging two PDF files."""
        merge_pdfs(self.pdf_files, 'MergedPDF.pdf')
        self.assertTrue(os.path.isfile('MergedPDF.pdf'))

    def test_rotate_page(self):
        """Test rotating a page in a PDF file."""
        rotate_page(self.pdf_files[0], 1, 90)  # Rotate the first page of the first PDF
        self.assertTrue(os.path.isfile('NewRotate.pdf'))

    def test_encrypt_pdf(self):
        """Test encrypting a PDF file."""
        encrypt_pdf(self.pdf_files[0], 'testpassword')
        self.assertTrue(os.path.isfile('encrypted_output.pdf'))

    def test_decrypt_pdf(self):
        """Test decrypting a PDF file."""
        encrypt_pdf(self.pdf_files[0], 'testpassword')  # First encrypt it
        decrypt_pdf('encrypted_output.pdf', 'testpassword')
        self.assertTrue(os.path.isfile('decrypted_output.pdf'))

if __name__ == '__main__':
    unittest.main()
