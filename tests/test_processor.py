# Import standard libraries
import unittest

# Import project code
from api.processor.processor_utils import *


class TestProcessorFunctions(unittest.TestCase):
    def test_list_available_methods(self):
        expected_methods = ['change_case', 'expand_contractions', 'handle_line_feeds',
                            'remove_punctuation', 'remove_special_characters', 'remove_whitespace']
        actual_methods = list_available_methods()
        self.assertCountEqual(actual_methods, expected_methods)


    def test_custom_pipeline(self):
        text = "Hello, World! It's a lovely DAY!"
        operations = ['expand_contractions', 'remove_whitespace', 'change_case']
        args = {'change_case': {'case': 'lower'}}
        expected_result = "hello,world!it'salovelyday!"
        actual_result = custom_pipeline(text, operations, args)
        self.assertEqual(actual_result, expected_result)


        with self.assertRaises(ValueError):
            custom_pipeline(text, ['invalid_operation'], {})


    def test_default_pipeline(self):
        text = "Hello, World! It's a lovely DAY!"
        expected_result = "helloworlditsalovelyday"
        actual_result = default_pipeline(text)
        self.assertEqual(actual_result, expected_result)

        with self.assertRaises(ValueError):
            default_pipeline(text, ['invalid_operation'], {})


if __name__ == '__main__':
    unittest.main()