import pytest
from api import utils


def test_change_case():
    text = "This is a test"
    assert utils.change_case(text, mode='lower') == "this is a test"
    assert utils.change_case(text, mode='upper') == "THIS IS A TEST"
    assert utils.change_case(text, mode='title') == "This Is A Test"
    assert utils.change_case(text, mode='capitalize') == "This is a test"
    with pytest.raises(ValueError):
        utils.change_case(text, mode='invalid')


def test_check_spelling():
    text = "This is a tst"
    assert utils.check_spelling(text, language='en') == "This is a test"
    with pytest.raises(ValueError):
        utils.check_spelling(text, language='invalid')


def test_encode_text():
    text = "This is a test"
    assert utils.encode_text(text, encoding='utf-8') == b"This is a test"
    assert utils.encode_text(text, encoding='ascii') == b"This is a test"
    with pytest.raises(ValueError):
        utils.encode_text(text, encoding='invalid')


def test_expand_contractions():
    text = "I've been there"
    assert utils.expand_contractions(text) == "I have been there"


def test_extract_ngrams():
    text = "This is a test"
    assert utils.extract_ngrams(text, n=2) == ["This is", "is a", "a test"]
    with pytest.raises(ValueError):
        utils.extract_ngrams(text, n=0)


def test_find_abbreviations():
    text = "NLP is short for Natural Language Processing"
    assert utils.find_abbreviations(
        text) == {"NLP": "Natural Language Processing"}


def test_handle_line_feeds():
    text = "This\nis a\ntest"
    assert utils.handle_line_feeds(text, mode='remove') == "This is a test"
    assert utils.handle_line_feeds(text, mode='crlf') == "This\r\nis a\r\ntest"
    assert utils.handle_line_feeds(text, mode='lf') == "This\nis a\ntest"
    with pytest.raises(ValueError):
        utils.handle_line_feeds(text, mode='invalid')


def test_normalize_unicode():
    text = "café"
    assert utils.normalize_unicode(text) == "cafe"


def test_numbers_to_words():
    text = "This is a test 123"
    assert utils.numbers_to_words(
        text) == "This is a test one hundred and twenty-three"


def test_process_words():
    text = "running ran run"
    assert utils.process_words(text, technique='stemming') == "run ran run"
    assert utils.process_words(
        text, technique='lemmatization') == "run ran run"
    with pytest.raises(ValueError):
        utils.process_words(text, technique='invalid')


def test_remove_data():
    assert utils.remove_data("www.example.com", ["URL"]) == "<URL>"
    assert utils.remove_data(
        "123-45-6789", ["SSN"]) == "<SOCIAL SECURITY NUMBER>"
    assert utils.remove_data("+1-202-555-0114", ["PHONE"]) == "<PHONE NUMBER>"
    assert utils.remove_data(
        "user@example.com", ["EMAIL"]) == "<EMAIL ADDRESS>"
    assert utils.remove_data(
        "378282246310005", ["CCN"]) == "<CREDIT CARD NUMBER"


def test_remove_list_markers():
    assert utils.remove_list_markers('1. Item') == ' Item'
    assert utils.remove_list_markers('a) Item') == ' Item'
    assert utils.remove_list_markers('ii) Item') == ' Item'


def test_remove_names():
    assert utils.remove_names('Hello, John') == 'Hello, <NAME>'


def test_remove_numbers():
    assert utils.remove_numbers('123') == ''
    assert utils.remove_numbers('abc123def') == 'abcdef'


def test_remove_punctuation():
    assert utils.remove_punctuation('Hello, World!') == 'Hello World'


def test_remove_special_characters():
    assert utils.remove_special_characters('@#!*^') == ''
    assert utils.remove_special_characters('abc@def#') == 'abcdef'


def test_remove_stopwords():
    assert utils.remove_stopwords('This is a test') == 'This test'


def test_remove_whitespace():
    assert utils.remove_whitespace(
        '    leading whitespace') == 'leading whitespace'
    assert utils.remove_whitespace(
        'trailing whitespace    ') == 'trailing whitespace'
    assert utils.remove_whitespace(
        '  multiple   whitespaces  ') == 'multiple whitespaces'
    assert utils.remove_whitespace('  strip  ') == 'strip'


def test_replace_words():
    assert utils.replace_words(
        'Hello, world', {'world': 'everyone'}) == 'Hello, everyone'
    assert utils.replace_words(
        'Hello, WORLD', {'world': 'everyone'}, case_sensitive=False) == 'Hello, everyone'


def test_tokenize_text(self):
    assert utils.tokenize_text('This is a test.', 'words') == [
        'This', 'is', 'a', 'test', '.']
    assert utils.tokenize_text('This is a test. And another one.', 'sentences') == [
        'This is a test.', 'And another one.']
