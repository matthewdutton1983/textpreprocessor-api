from .api_instance import api
from flask_restx import fields

change_case_model = api.model("ChangeCase", {
    "text": fields.String(required=True, description="The input text."), 
    "case": fields.String(required=False, description="The case type, either 'lower', 'upper', 'title' or 'capitalize'. Defaults to 'lower'.")
})

check_spelling_model = api.model("CheckSpelling", {
    "text": fields.String(required=True, description="The input text."),
    "language": fields.String(required=False, description="Language spell checking - supported languages are 'en' (English), 'es' (Spanish) and 'fr' (French). Defaults to English.")
})

convert_numbers_to_words_model = api.model("ConvertNumbersToWords", {
    "text": fields.String(required=True, description="The input text.")
})

convert_words_to_numbers_model = api.model("ConvertWordsToNumbers", {
    "text": fields.String(required=True, description="The input text.")
})

encode_text_model = api.model("EncodeText", {
    "text": fields.String(required=True, description="The input text."),
    "encoding": fields.String(required=False, description="The encoding type to use. Defaults to 'utf-8'."),
    "errors": fields.String(required=False, description="The error handling strategy to use, either 'strict', 'ignore' or 'replace'. Defaults to 'strict'.")
})

expand_contractions_model = api.model("ExpandContractions", {
    "text": fields.String(required=True, description="The input text.")
})

extract_ngrams_model = api.model("ExtractNgrams", {
    "text": fields.String(required=True, description="The input text."),
    "n": fields.Integer(required=False, description="The number of grams for the n-grams. Defaults to 2."),
    "padding": fields.Boolean(required=False, description="Whether to add padding to the start and end of sentences. Defaults to False"),
    "tokens": fields.List(fields.String, required=False, description="Custom token list. If none, the text will be split by spaces.")
})

find_abbreviations_model = api.model("FindAbbreviations", {
    "text": fields.String(required=True, description="The input text.")
})

handle_line_feeds_model = api.model("HandleLineFeeds", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=False, description="The mode to handle line feeds, either 'remove',  'crlf' (carriage return) or 'lf' (line feed). Defaults to 'remove'." )
})

lemmatize_text_model = api.model("LemmatizeText", {
    "text": fields.String(required=True, description="The input text.")
})

normalize_unicode_model = api.model("NormalizeUnicode", {
    "text": fields.String(required=True, description="The input text.")
})

remove_brackets_model = api.model("RemoveBrackets", {
    "text": fields.String(required=True, description="The input text.")
})

remove_credit_card_numbers_model = api.model("RemoveCreditCardNumbers", {
    "text": fields.String(required=True, description="The input text."),
    "use_mask": fields.Boolean(required=True, description="If True, replaces credit card numbers with a mask. If False, simply removes the credit card numbers. Defaults to True"),
    "mask": fields.String(required=False, description="The mask used to replace credit card numbers within the input text. Defaults to '<CREDIT_CARD_NUMBER>'.")
})

remove_email_addresses_model = api.model("RemoveEmailAddresses", {
    "text": fields.String(required=True, description="The input text."),
    "use_mask": fields.Boolean(required=True, description="If True, replaces email addresses with a mask. If False, simply removes the email addresses. Defaults to True"),
    "mask": fields.String(required=False, description="The mask used to replace email addresses within the input text. Defaults to '<EMAIL_ADDRESS>'.")
})

remove_html_tags_model = api.model("RemoveHtmlTags", {
    "text": fields.String(required=True, description="The input text.")
})

remove_list_markers_model = api.model("RemoveListMarkers", {
    "text": fields.String(required=True, description="The input text.")
})

remove_names_model = api.model("RemoveNames", {
    "text": fields.String(required=True, description="The input text."),
    "use_mask": fields.Boolean(required=False, description="If True, replaces names with a mask. If False, simply removes the names. Defaults to True"),
    "mask": fields.String(required=False, description="The mask used to replace names within the input text. Defaults to '<NAME>'.")
})

remove_numbers_model = api.model("RemoveNumbers", {
    "text": fields.String(required=True, description="The input text.")
})

remove_phone_numbers_model = api.model("RemovePhoneNumbers", {
    "text": fields.String(required=True, description="The input text."),
    "use_mask": fields.Boolean(required=False, description="If True, replaces phone numbers with a mask. If False, simply removes the phone numbers. Defaults to True."),
    "mask": fields.String(required=False, description="The mask used to replace phone numbers within the input text. Defaults to '<PHONE_NUMBER>'.")
})

remove_punctuation_model = api.model("RemovePunctuation", {
    "text": fields.String(required=True, description="The input text."),
    "punctuations": fields.String(required=False, description="The specific punctuations to remove. Defaults to None, which means all punctuations will be removed."),
    "remove_duplicates": fields.Boolean(required=False, description="If True, duplicate punctuations will be removed. Defaults to False.")
})

remove_social_security_model = api.model("RemoveSocialSecurity", {
    "text": fields.String(required=True, description="The input text."),
    "use_mask": fields.Boolean(required=True, description="If True, replaces Social Security Numbers (SSN) with a mask. If False, simply removes the SSNs. Defaults to True"),
    "mask": fields.String(required=False, description="The mask used to replace SSNs within the input text. Defaults to '<SOCIAL_SECURITY_NUMBER>'.")
})

remove_special_characters_model = api.model("RemoveSpecialCharacters", {
    "text": fields.String(required=True, description="The input text."),
    "remove_unicode": fields.Boolean(required=False, description="If True, removes unicode characters. If False, does not remove unicode. Defaults to False.")
})

remove_stopwords_model = api.model("RemoveStopwords", {
    "text": fields.String(required=True, description="The input text."),
    "stop_words": fields.List(fields.String, required=False, description="A custom list of stopwords to remove. If None, uses the default set of English stopwords from NLTK. Defaults to None.")
})

remove_url_model = api.model("RemoveUrl", {
    "text": fields.String(required=True, description="The input text."),
    "use_mask": fields.Boolean(required=True, description="If True, replaces URLs with a mask. If False, simply removes the URLs. Defaults to True"),
    "mask": fields.String(required=False, description="The mask used to replace URLs within the input text. Defaults to '<URL>'.")
})

remove_whitespace_model = api.model("RemoveWhiteSpace", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=True, description="The mode to remove whitespaces, either 'leading', 'trailing', 'all' or 'strip'. Defaults to 'strip'."),
    "keep_duplicates": fields.Boolean(required=False, description="Whether to keep duplicate whitespaces. Defaults to False.")
})

replace_words_model = api.model("ReplaceWords", {
    "text": fields.String(required=True, description="The input text."),
    "replacement_dict": fields.Raw(required=True, description="The dictionary mapping words to their replacements."),
    "case_sensitive": fields.Boolean(required=False, description="Flag indicating whether the replacement should be case-sensitive. Defaults to False.")
})

stem_words_model = api.model("StemWords", {
    "text": fields.String(required=True, description="The input text."),
    "stemmer": fields.String(required=False, description="The stemmer algorithm to use. Options are 'snowball', 'porter' and 'lancaster'. Defaults to 'porter'.")
})

tokenize_text_model = api.model("TokenizeText", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=False, description="The type of tokenization, either 'sentences' or 'words'. Defaults to 'sentences'.")
})
