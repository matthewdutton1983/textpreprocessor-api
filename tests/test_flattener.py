# Import standard libraries
import unittest

# Import project code
from api.flattener.flattener_utils import *

class TestFlattenerFunctions(unittest.TestCase):
    def test_handle_line_feeds(self):
        text = "Hello\nWorld\rHello\r\nWorld"
        self.assertEqual(handle_line_feeds(text, 'remove'), "Hello WorldHelloWorld")
        self.assertEqual(handle_line_feeds(text, 'crlf'), "Hello\r\nWorld\r\nHello\r\nWorld")
        self.assertEqual(handle_line_feeds(text, 'lf'), "Hello\nWorld\nHello\nWorld")

        with self.assertRaises(ValueError):
            handle_line_feeds(text, 'invalid')


    def test_remove_brackets(self):
        text = "Hello (world) [hello] {world}"
        self.assertEqual(remove_brackets(text), "Hello   ")


    def test_remove_html_tags(self):
        text = "<p>Hello</p> World"
        self.assertEqual(remove_html_tags(text), " Hello World")


    def test_remove_list_markers(self):
        text = "1. Hello 2) World i. Hello ii) World"
        self.assertEqual(remove_list_markers(text), " Hello  World  Hello  World")


    def test_remove_special_characters(self):
        text = "Hello! World$"
        self.assertEqual(remove_special_characters(text), "Hello World")
        self.assertEqual(remove_special_characters(text, remove_unicode=True), "Hello World")
        self.assertEqual(remove_special_characters(text, custom_characters="!$"), "Hello World")


    def test_remove_stopwords(self):
        text = "This is a test string"
        self.assertEqual(remove_stopwords(text), "This test string")


    def test_remove_whitespace(self):
        text = " Hello   World "
        self.assertEqual(remove_whitespace(text, 'leading'), "Hello   World ")
        self.assertEqual(remove_whitespace(text, 'trailing'), " Hello   World")
        self.assertEqual(remove_whitespace(text, 'all'), "HelloWorld")
        self.assertEqual(remove_whitespace(text, 'strip'), "Hello World")

        with self.assertRaises(ValueError):
            remove_whitespace(text, 'invalid')


if __name__ == '__main__':
    unittest.main()
