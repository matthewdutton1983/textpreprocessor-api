# Import standard libraries
import base64
import unittest

# Import project code
from api.encoder.encoder_utils import *

class TestEncodeText(unittest.TestCase):
    def test_encode_text_utf_8(self):
        self.assertEqual(encode_text('Hello', 'utf-8'), base64.b64encode(b'Hello').decode("utf-8"))
    

    def test_encode_text_ascii(self):
        self.assertEqual(encode_text('World', 'ascii'), base64.b64encode(b'World').decode("utf-8"))


    def test_encode_text_strict(self):
        self.assertEqual(encode_text('Strict', 'utf-8', 'strict'), base64.b64encode(b'Strict').decode("utf-8"))


    def test_encode_text_ignore(self):
        self.assertEqual(encode_text('Ignore', 'utf-8', 'ignore'), base64.b64encode(b'Ignore').decode("utf-8"))


    def test_encode_text_replace(self):
        self.assertEqual(encode_text('Replace', 'utf-8', 'replace'), base64.b64encode(b'Replace').decode("utf-8"))


    def test_encode_text_unsupported_encoding(self):
        with self.assertRaises(ValueError):
            encode_text('Hello', 'unsupported')


    def test_encode_text_unsupported_error_strategy(self):
        with self.assertRaises(ValueError):
            encode_text('Hello', 'utf-8', 'unsupported')

if __name__ == '__main__':
    unittest.main()
