# Import standard libraries
import unittest

# Import project code
from api.transformer.transformer_utils import *


class TestTransformerFunctions(unittest.TestCase):
    def test_change_case(self):
        text = "i am a chatbot."
        self.assertEqual(change_case(text, 'upper'), "I AM A CHATBOT.")
        self.assertEqual(change_case(text, 'title'), "I Am A Chatbot.")
        self.assertEqual(change_case(text, 'capitalize'), "I am a chatbot.")
        
        with self.assertRaises(ValueError):
            change_case(text, 'invalid')


    def test_convert_numbers_to_words(self):
        text = "I am 1 chatbot among 100."
        expected_result = "I am one chatbot among one hundred."
        self.assertEqual(convert_numbers_to_words(text), expected_result)


    def test_convert_words_to_numbers(self):
        text = "I am one chatbot among one hundred."
        expected_result = "I am 1 chatbot among 100."
        self.assertEqual(convert_words_to_numbers(text), expected_result)


    def test_replace_words(self):
        text = "I am a chatbot. I like to help people."
        replacement_dict = {"chatbot": "robot", "people": "humans"}
        expected_result = "I am a robot. I like to help humans."
        self.assertEqual(replace_words(text, replacement_dict), expected_result)

        replacement_dict_case = {"i": "You", "am": "are", "to": "too"}
        expected_result_case = "You am a chatbot. I like too help people."
        self.assertEqual(replace_words(text, replacement_dict_case, True), expected_result_case)

        expected_result_case = "You are a chatbot. You like too help people."
        self.assertEqual(replace_words(text, replacement_dict_case), expected_result_case)

if __name__ == '__main__':
    unittest.main()