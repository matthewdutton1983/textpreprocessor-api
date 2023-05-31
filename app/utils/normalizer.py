# Import standard libraries
import re
import string
from typing import List, Optional, Union

# Import third-party libraries
import contractions
from nltk.stem import WordNetLemmatizer, PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.tokenize import word_tokenize as _word_tokenize
from unicodedata import normalize as _normalize


def expand_contractions(text: str) -> str:
    """
    Expands contractions in a given text.

    Parameters:
    - text (str): Text with potential contractions.

    Returns:
    - str: Text with contractions expanded.
    """
    return contractions.fix(text)


def lemmatize_text(text: str) -> str:
    """
    Process words in given text using lemmatization.

    Parameters:
    - text (str): The input text.

    Returns:
    - str: The lemmatized text.
    """
    lemmatizer = WordNetLemmatizer()
    tokens = _word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_words)


def normalize_unicode(text: str) -> str:
    """
    This method normalizes unicode characters in given text to remove umlauts, accents, etc.

    Parameters:
    - text (str): The input text to normalize unicode.

    Returns:
    - str: The text with normalized unicode characters.
    """
    return _normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')




def remove_numbers(text: str) -> str:
    """
    Remove all numbers from the text.

    Paramters:
    - text (str): Input string.

    Returns:
    - str: Text without numbers.
    """
    return re.sub('\d+', '', text)


def remove_punctuation(text: Union[str, List[str]], punctuations: Optional[str] = None, remove_duplicates: Optional[bool] = False) -> Union[str, List[str]]:
    """
    Removes punctuations from the text. Optionally, also removes duplicate punctuations.

    Parameters:
    - text (Union[str, List[str]]): The input text.
    - punctuations (Optional[str]): The punctuations to remove. Defaults to None, which means all punctuations will be removed.
    - remove_duplicates (Optional[bool]): If True, duplicate punctuations will be removed. Defaults to False.

    Returns:
    - Union[str, List[str]]: The text with punctuations removed. If remove_duplicates is True, also removes duplicate punctuations.
    """
    if punctuations is None:
        punctuations = string.punctuation

    def process(s: str) -> str:
        no_punct = s.translate(str.maketrans('', '', punctuations))
        return re.sub(r'([\!\?\.\,\:\;]){2,}', r'\1', no_punct) if remove_duplicates else no_punct

    if isinstance(text, list):
        return [process(s) for s in text]
    else:
        return process(text)


def stem_text(text: str, stemmer: str = 'porter') -> str:
    """
    Process words in given text using stemming.

    Parameters:
    - text (str): The input text.
    - stemmer (str): The stemmer algorithm to use. Options are 'snowball', 'porter', and 'lancaster'. Default is 'porter'.

    Returns:
    - str: The stemmed text.
    """
    supported_stemmers = {
        'snowball': SnowballStemmer('english'),
        'porter': PorterStemmer(),
        'lancaster': LancasterStemmer()
    }
    stemmer = stemmer.lower()
    if stemmer not in supported_stemmers:
        raise ValueError(
            f"Unsupported stemmer '{stemmer}'. Supported stemmers are: {', '.join(supported_stemmers.keys())}")

    tokens = _word_tokenize(text)
    stemmed_words = [supported_stemmers[stemmer].stem(
        token) for token in tokens]

    return ' '.join(stemmed_words)
