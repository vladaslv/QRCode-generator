import unittest
from io import BytesIO
from PIL import Image
from QRCodes.utils import generate_qr_code
from QRCodes.forms import QRCodeForm
from django.core.files.uploadedfile import SimpleUploadedFile


class TestGenerateQRCode(unittest.TestCase):
    def test_generate_qr_code_without_logo(self):
        identifier = "test_identifier"
        buffer = generate_qr_code(identifier)
        self.assertIsInstance(buffer, BytesIO)
    
    def test_generate_qr_code_with_logo(self):
        identifier = "test_identifier"
        logo = Image.new("RGB", (100, 100), (255, 255, 255))
        buffer = generate_qr_code(identifier, logo)
        self.assertIsInstance(buffer, BytesIO)


class QRCodeFormTests(unittest.TestCase):
    def test_form_valid_data(self):
        form_data = {
            'prefix': 'test_prefix',
            'suffix': 'test_suffix',
            'num_zeros': '5',
            'amount': '10'
        }
        form = QRCodeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_logo(self):
        form_data = {
            'prefix': 'test_prefix',
            'suffix': 'test_suffix',
            'num_zeros': '5',
            'amount': '10',
            'logo': SimpleUploadedFile("test_image.png", b"test_image_content")
        }
        form = QRCodeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_missing_amount(self):
        form_data = {
            'prefix': 'test_prefix',
            'suffix': 'test_suffix',
            'num_zeros': '5'
        }
        form = QRCodeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], ['This field is required.'])