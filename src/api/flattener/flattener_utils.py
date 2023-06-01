# Import standard libraries
import re
from typing import Optional

# Import third-party libraries
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as _word_tokenize


def handle_line_feeds(text: str, mode: str = 'remove') -> str:
    """
    Handles line feeds in the text based on the selected mode.

    Parameters:
    - text (str): The input text.
    - mode (str): The mode to handle line feeds - either 'remove', 'crlf', or 'lf'. Defaults to 'remove'.

    Returns:
    - str: Text with line feeds handled as per the mode.
    """
    modes = ['remove', 'crlf', 'lf']
    if mode not in modes:
        raise ValueError(
            f"Invalid mode: '{mode}'. Valid options are {', '.join(modes)}.")

    if mode == 'remove':
        return text.replace('\n', ' ').replace('\r', '')
    elif mode == 'crlf':
        return text.replace('\n', '\r\n').replace('\r\r\n', '\r\n')
    elif mode == 'lf':
        return text.replace('\r\n', '\n').replace('\r', '\n')


def remove_brackets(text: str) -> str:
    """
    Remove text inside brackets, braces, and parentheses.

    Parameters:
    - text (str): Input string.

    Returns:
    - str: Text without content inside brackets, braces, and parentheses.
    """
    return re.sub(r'\[.*?\]|\(.*?\)|\{.*?\}', '', text)


def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from a text.

    Parameters:
    - text (str): Input string

    Returns:
    - str: Text without HTML tags
    """
    text = re.sub(r'</[^>]+>', ' ', text)
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def remove_list_markers(text: str) -> str:
    """
    This method removes list markers (numbering and bullets) from given text.

    Parameters:
    - text (str): The input text to remove list markers from.

    Returns:
    - str: The text with list markers removed.
    """
    return re.sub(r'(^|\s)[0-9a-zA-Z][.)]\s+|(^|\s)[ivxIVX]+[.)]\s+', ' ', text)


def remove_special_characters(text: str, remove_unicode: bool = False, custom_characters: Optional[str] = None) -> str:
    """
    Removes special characters from the text.

    Parameters:
    - text (str): The input text.
    - remove_unicode (bool): Whether to remove unicode characters. Defaults to False.
    - custom_characters (Optional[str]): Custom characters to be removed. Defaults to None.

    Returns:
    - str: The text with special characters removed.
    """
    processed_texts = []

    if remove_unicode:
        processed_text = re.sub(r'[^\w\s]', '', text)
        processed_text = ''.join(
            char for char in processed_text if ord(char) < 128)
    elif custom_characters is not None:
        processed_text = text
        for character in custom_characters:
            processed_text = processed_text.replace(character, '')
    else:
        processed_text = re.sub(r'[^\w\s]', '', text)

    processed_texts.append(processed_text)
    return ' '.join(processed_texts)


def remove_stopwords(text: str, stop_words: Optional[set] = None) -> str:
    """
    This method removes stopwords from given text.

    Parameters:
    - text (str): The input text to remove stopwords from.
    - stop_words (Optional[set]): A set of stopwords to remove. If None, uses the default set of English stopwords from NLTK. Default is None.

    Returns:
    - str: The list of tokens with stopwords removed.
    """
    if stop_words is None:
        stop_words = set(stopwords.words('english'))
    if isinstance(stop_words, list):
        stop_words = set(stop_words)

    tokens = _word_tokenize(text)
    processed_tokens = [token for token in tokens if token not in stop_words]

    return ' '.join(processed_tokens)


def remove_whitespace(text: str, mode: str = 'strip', keep_duplicates: bool = False) -> str:
    """
    Removes whitespace from the text based on the selected mode.

    Parameters:
    - text (str): The input text.
    - mode (str): The mode to remove whitespaces - either 'leading', 'trailing', 'all', or 'strip'. Defaults to 'strip'.
    - keep_duplicates (bool): Whether to keep duplicate whitespaces. Defaults to False.

    Returns:
    - str: The text with whitespace removed as per the mode.
    """
    modes = ['leading', 'trailing', 'all', 'strip']

    if mode not in modes:
        raise ValueError(
            f"Invalid mode: '{mode}'. Valid options are {', '.join(modes)}.")

    if mode == 'leading':
        processed_text = re.sub(r'^\s+', '', text, flags=re.UNICODE)
    elif mode == 'trailing':
        processed_text = re.sub(r'\s+$', '', text, flags=re.UNICODE)
    elif mode == 'all':
        processed_text = re.sub(r'\s+', '', text, flags=re.UNICODE)
    elif mode == 'strip':
        processed_text = re.sub(r'^\s+|\s+$', '', text, flags=re.UNICODE)

    if not keep_duplicates:
        processed_text = ' '.join(
            re.split('\s+', processed_text, flags=re.UNICODE))

    return processed_text
