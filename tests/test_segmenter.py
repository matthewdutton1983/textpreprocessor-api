# Import standard libraries
import unittest

# Import project code
from api.segmenter.segmenter_utils import *


class TestSegmenterFunctions(unittest.TestCase):
    def test_extract_ngrams(self):
        text = "I am a chatbot. I like to help people."
        expected_result = ["I am", "am a", "a chatbot.", "chatbot. I", "I like", "like to", "to help", "help people."]
        actual_result = extract_ngrams(text)
        self.assertEqual(actual_result, expected_result)

        with self.assertRaises(ValueError):
            extract_ngrams(text, 0)


    def test_tokenize_sentences(self):
        text = "I am a chatbot. I like to help people."
        expected_result = ["I am a chatbot.", "I like to help people."]
        actual_result = tokenize_sentences(text)
        self.assertEqual(actual_result, expected_result)


    def test_tokenize_words(self):
        text = "I am a chatbot. I like to help people."
        expected_result = ["I", "am", "a", "chatbot", ".", "I", "like", "to", "help", "people", "."]
        actual_result = tokenize_words(text)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()