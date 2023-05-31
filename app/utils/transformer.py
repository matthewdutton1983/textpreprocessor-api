# Import standard libraries
import re
from typing import Dict

# Import third-party libraries
from num2words import num2words as _num2words
from word2number import w2n


def change_case(text: str, case: str = 'lower') -> str:
    """
    Changes the case of the text based on the selected case type.

    Parameters:
    - text (str): The input text.
    - case (str): The type of case - either 'lower', 'upper', 'title', or 'capitalize'. Defaults to 'lower'.

    Returns:
    - str: The text in the specified case type.
    """
    cases = ['lower', 'upper', 'title', 'capitalize']
    if case not in cases:
        raise ValueError(
            f"Invalid case type: '{case}'. Valid options are {', '.join(cases)}")

    if case == 'lower':
        return text.lower()
    elif case == 'upper':
        return text.upper()
    elif case == 'title':
        return text.title()
    elif case == 'capitalize':
        return text.capitalize()


def convert_numbers_to_words(text: str) -> str:
    """
    This method converts numbers in the text to their corresponding words.

    Parameters:
    - text (str): The input text.

    Returns:
    - str: The text with numbers converted to words.
    """
    def replace_with_words(match):
        number = match.group(0)
        return _num2words(number)
    return re.sub(r'\b\d+\b', replace_with_words, text)


def convert_words_to_numbers(text: str) -> str:
    """
    This method converts words in the text to their corresponding numbers.

    Parameters:
    - text (str): The input text.

    Return:
    - str: The text with words converted to numbers.
    """
    words = text.split()
    converted_words = [w2n.word_to_num(word) if word.isalpha() and
                       word.lower() in w2n.american_number_system else
                       word for word in words]
    return ' '.join(map(str, converted_words))


def replace_words(text: str, replacement_dict: Dict[str, str], case_sensitive: bool = False) -> str:
    """
    This method replaces specified words in given text according to a replacement dictionary.

    Parameters:
    - text (str): The input text to replace words in.
    - replacement_dict (Dict[str, str]): The dictionary mapping words to their replacements.
    - case_sensitive (bool): Flag indicating whether the replacement should be case-sensitive. Default is False.

    Returns:
    - str: The text with specified words replaced according to the replacement dictionary.
    """
    if case_sensitive:
        regex_pattern = re.compile(
            r'\b(' + '|'.join(re.escape(key) for key in replacement_dict.keys()) + r')\b')
        return regex_pattern.sub(lambda x: replacement_dict[x.group()], text)
    else:
        regex_pattern = re.compile(
            r'\b(' + '|'.join(re.escape(key) for key in replacement_dict.keys()) + r')\b', re.IGNORECASE)
        return regex_pattern.sub(lambda x: replacement_dict[x.group().lower()], text)
