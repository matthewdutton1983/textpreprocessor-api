# Import standard libraries
import unittest

# Import project code
from api.normalizer.normalizer_utils import *


class TestNormalizerFunctions(unittest.TestCase):
    def test_expand_contractions(self):
        text = "You've won! Isn't it great? It's your day."
        self.assertEqual(expand_contractions(text), 
                         "You have won! Is not it great? It is your day.")


    def test_lemmatize_text(self):
        text = "Running faster won't help if you're moving in the wrong direction."
        self.assertEqual(lemmatize_text(text), 
                         "Running fast wo n't help if you 're moving in the wrong direction.")


    def test_normalize_unicode(self):
        text = "Cliché is a cliché. Résumé is commonly used."
        self.assertEqual(normalize_unicode(text), 
                         "Cliche is a cliche. Resume is commonly used.")


    def test_remove_numbers(self):
        text = "123hello456world789"
        self.assertEqual(remove_numbers(text), "helloworld")


    def test_remove_punctuation(self):
        text = "Hello, world!!! How's it going???"
        self.assertEqual(remove_punctuation(text), "Hello world How s it going")
        self.assertEqual(remove_punctuation(text, remove_duplicates=True), "Hello world How s it going?")


    def test_stem_text(self):
        text = "Running faster won't help if you're moving in the wrong direction."
        self.assertEqual(stem_text(text, 'porter'), 
                         "Run faster wo n't help if you 'r move in the wrong direct .")

        with self.assertRaises(ValueError):
            stem_text(text, 'invalid_stemmer')


if __name__ == '__main__':
    unittest.main()
