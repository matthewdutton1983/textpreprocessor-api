import contractions
import re
import spacy
import string
from abbreviations import schwartz_hearst
from autocorrect import Speller
from bs4 import BeautifulSoup
from nltk import ngrams as _ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.tokenize import sent_tokenize as _sent_tokenize
from nltk.tokenize import word_tokenize as _word_tokenize
from num2words import num2words as _num2words
from typing import Dict, List, Optional, Union
from unicodedata import normalize as _normalize
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


def check_spelling(text: str, language: str = 'en') -> str:
    """
    Correct spelling in the text.

    Parameters:
    - text (str): Input string.
    - language (str, optional): Language for spell checking. Supported languages are 'en' (English), 'es' (Spanish), and 'fr' (French). Defaults to 'en'.

    Returns:
        str: Text with corrected spelling.
    """
    supported_languages = ['en', 'es', 'fr']

    if language not in supported_languages:
        raise ValueError(
            f"Unsupported language '{language}'. Supported languages are: {supported_languages}")

    spell = Speller(lang=language)
    tokens = _word_tokenize(text)
    corrected_tokens = [spell(word) for word in tokens]
    return ' '.join(corrected_tokens).strip()


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


def encode_text(text: str, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
    """
    This method encodes given text using a specified encoding.

    Parameters:
    - text (str): The input text to encode.
    - encoding (str): The encoding type to use. Defaults to 'utf-8'.
    - errors (str): The error handling strategy to use. Defaults to 'strict'.

    Returns:
    - bytes: The encoded text.

    Raises:
    ValueError: If an unsupported encoding type or error handling strategy is specified.
    """
    encodings = ['utf-8', 'ascii']
    if encoding not in encodings:
        raise ValueError(
            "Invalid encoding type. Only 'utf-8' and 'ascii' are supported.")

    if errors not in ['strict', 'ignore', 'replace']:
        raise ValueError(
            "Invalid error handling strategy. Only 'strict', 'ignore', and 'replace' are supported.")

    return text.encode(encoding, errors=errors)


def expand_contractions(text: str) -> str:
    """
    Expands contractions in a given text.

    Parameters:
    - text (str): Text with potential contractions.

    Returns:
    - str: Text with contractions expanded.
    """
    return contractions.fix(text)


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


def find_abbreviations(text: str) -> Dict[str, str]:
    """
    This method identifies abbreviations in given text and returns dictionaries of abbreviations and their definitions.

    Parameters:
    - text (str): The input text to identify abbreviations.

    Returns:
    - Dict[str, str]: The dictionary containing abbreviations and their definitions.
    """
    return schwartz_hearst.extract_abbreviation_definition_pairs(doc_text=text)


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


def remove_brackets(text: str) -> str:
    """
    Remove text inside brackets, braces, and parentheses.

    Parameters:
    - text (str): Input string.

    Returns:
    - str: Text without content inside brackets, braces, and parentheses.
    """
    return re.sub(r'\[.*?\]|\(.*?\)|\{.*?\}', '', text)


def remove_credit_card_numbers(text: str, use_mask: bool = True, mask: str = '<CREDIT_CARD_NUMBER>'):
    """
    Removes or masks credit card numbers from the input text.

    Parameters:
    - text (str): The input text.
    - use_mask (bool): If True, replaces credit card numbers with a mask. Defaults to True.
    - mask (str): The mask to replace credit card numbers with. Defaults to '<CREDIT_CARD_NUMBER>'.

    Returns:
    - str: The text with credit card numbers removed or masked.
    """
    pattern = r'(4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][' \
        r'0-9]|2720)[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(' \
        r'?:2131|1800|35\d{3})\d{11})'
    return re.sub(pattern, mask if use_mask else '', text)


def remove_email_addresses(text: str, use_mask: bool = True, mask: str = '<EMAIL_ADDRESS>'):
    """
    Removes or masks email addresses from the input text.

    Parameters:
    - text (str): The input text.
    - use_mask (bool): If True, replaces email addresses with a mask. Defaults to True.
    - mask (str): The mask to replace email addresses with. Defaults to '<EMAIL_ADDRESS>'.

    Returns:
    - str: The text with email addresses removed or masked.
    """
    pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    return re.sub(pattern, mask if use_mask else '', text)


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


def remove_names(text: str, use_mask: Optional[bool] = True, mask: str = '<NAME>') -> str:
    """
    Remove all names from the text using named entity recognition.

    Parameters:
    - text (str): Input string.
    - use_mask (Optional[bool], optional): If True, replaces names with a mask. Defaults to True.
    - custom_mask (Optional[str], optional): Custom mask to replace names. If None, '<NAME>' will be used. Defaults to None.

    Returns:
    - str: Text without names.
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    tokens = [mask if token.ent_type_ ==
              'PERSON' and use_mask else token.text for token in doc]

    return ' '.join(tokens)


def remove_numbers(text: str) -> str:
    """
    Remove all numbers from the text.

    Paramters:
    - text (str): Input string.

    Returns:
    - str: Text without numbers.
    """
    return re.sub('\d+', '', text)


def remove_phone_numbers(text: str, use_mask: bool = True, mask: str = '<PHONE_NUMBER>'):
    """
    Removes or masks phone numbers from the input text.

    Parameters:
    - text (str): The input text.
    - use_mask (bool): If True, replaces phone numbers with a mask. Defaults to True.
    - mask (str): The mask to replace phone numbers with. Defaults to '<PHONE_NUMBER>'.

    Returns:
    - str: The text with phone numbers removed or masked.
    """
    pattern = r'(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?(?!\d)'
    return re.sub(pattern, mask if use_mask else '', text)


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


def remove_social_security(text: str, use_mask: bool = True, mask: str = '<SOCIAL_SECURITY_NUMBER>'):
    """
    Removes or masks Social Security numbers from the input text.

    Parameters:
    - text (str): The input text.
    - use_mask (bool): If True, replaces SSNs with a mask. Defaults to True.
    - mask (str): The mask to replace SSNs with. Defaults to '<SOCIAL_SECURITY_NUMBER>'.

    Returns:
    - str: The text with SSNs removed or masked.
    """
    pattern = r'(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}|(' \
        r'?!219099999|078051120)(?!666|000|9\d{2})\d{3}(?!00)\d{2}(?!0{4})\d{4}'
    return re.sub(pattern, mask if use_mask else '', text)


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


def remove_url(text: str, use_mask: bool = True, mask: str = '<URL>'):
    """
    Removes or masks URLs from the input text.

    Parameters:
    - text (str): The input text.
    - use_mask (bool): If True, replaces URLs with a mask. Defaults to True.
    - mask (str): The mask to replace URLs with. Defaults to '<URL>'.

    Returns:
    - str: The text with URLs removed or masked.
    """
    pattern = r'(www|http)\S+'
    return re.sub(pattern, mask if use_mask else '', text)


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


def tokenize_text(text: str, mode: str = 'sentences') -> List[str]:
    """
    Tokenize the input text into sentences or words based on the selected mode.

    Parameters:
    - text (str): The input text to be tokenized.
    - mode (str): The type of tokenization - either 'sentences' or 'words'. Defaults to 'sentences'.

    Returns:
    - List[str]: The tokenized text.
    """
    modes = ['sentences', 'words']

    if mode not in modes:
        raise ValueError(
            f"Invalid mode: '{mode}'. Valid options are {', '.join(modes)}")

    if mode == 'sentences':
        return _sent_tokenize(text)
    elif mode == 'words':
        return _word_tokenize(text)
