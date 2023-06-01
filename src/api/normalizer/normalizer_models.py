# Import third-party libraries
from flask_restx import fields, Namespace

normalizer_ns = Namespace("normalizer", description="This service provides utilities to standardize and normalize text, such as removing punctuation, handling unicode, or lemmatizing words.")

expand_contractions_model = normalizer_ns.model("ExpandContractions", {
    "text": fields.String(required=True, description="The input text.")
})

lemmatize_text_model = normalizer_ns.model("LemmatizeText", {
    "text": fields.String(required=True, description="The input text.")
})

normalize_unicode_model = normalizer_ns.model("NormalizeUnicode", {
    "text": fields.String(required=True, description="The input text.")
})

remove_numbers_model = normalizer_ns.model("RemoveNumbers", {
    "text": fields.String(required=True, description="The input text.")
})

remove_punctuation_model = normalizer_ns.model("RemovePunctuation", {
    "text": fields.String(required=True, description="The input text."),
    "punctuations": fields.String(required=False, description="The specific punctuations to remove. Defaults to None, which means all punctuations will be removed."),
    "remove_duplicates": fields.Boolean(required=False, description="If True, duplicate punctuations will be removed. Defaults to False.")
})

stem_words_model = normalizer_ns.model("StemWords", {
    "text": fields.String(required=True, description="The input text."),
    "stemmer": fields.String(required=False, description="The stemmer algorithm to use. Options are 'snowball', 'porter' and 'lancaster'. Defaults to 'porter'.")
})
