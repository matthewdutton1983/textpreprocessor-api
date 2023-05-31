# Import standard libraries
import re
from typing import Dict, List, Optional

# Import third-party libraries
from nltk import ngrams as _ngrams
from nltk.tokenize import sent_tokenize as _sent_tokenize
from nltk.tokenize import word_tokenize as _word_tokenize


def extract_ngrams(text: str, n: int = 2, padding: bool = False, tokens: Optional[List[str]] = None) -> List[str]:
    """
    Extracts n-grams from the text.

    Parameters:
    - text (str): The input text.
    - n (int): The number of grams for the n-grams. Defaults to 2.
    - padding (bool): Whether to add padding to the start and end of sentences. Defaults to False.
    - tokens (list, optional): Custom token list. If None, the text will be split by spaces.

    Returns:
    - List[str]: The list of n-grams from the text.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError(
            "Invalid n: '{n}'. It should be an integer greater than 0.")

    if tokens is None:
        tokens = text.split()

    if padding:
        tokens = ['<s>']*(n-1) + tokens + ['</s>']*(n-1)

    n_grams = _ngrams(tokens, n)
    return [' '.join(grams) for grams in n_grams]


def tokenize_sentences(text: str) -> List[str]:
    """
    Tokenize the input text into sentences.

    Parameters:
    - text (str): The input text to be tokenized.

    Returns:
    - List[str]: The tokenized text.
    """
    return _sent_tokenize(text)


def tokenize_words(text: str) -> List[str]:
    """
    Tokenize the input text into words.

    Parameters:
    - text (str): The input text to be tokenized.

    Returns:
    - List[str]: The tokenized text.
    """
    return _word_tokenize(text)
