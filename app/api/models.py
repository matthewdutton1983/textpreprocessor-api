# Import third-party libraries
from flask_restx import fields

# Import project code
from .api_instance import api
from .namespaces import encoder_ns, flattener_ns, normalizer_ns, segmenter_ns, transformer_ns, utilities_ns

# =================================================================================================================================================
# ENCODER MODELS
# =================================================================================================================================================

encode_text_model = encoder_ns.model("EncodeText", {
    "text": fields.String(required=True, description="The input text."),
    "encoding": fields.String(required=False, description="The encoding type to use. Defaults to 'utf-8'."),
    "errors": fields.String(required=False, description="The error handling strategy to use, either 'strict', 'ignore' or 'replace'. Defaults to 'strict'.")
})

# =================================================================================================================================================
# FLATTENER MODELS
# =================================================================================================================================================

handle_line_feeds_model = flattener_ns.model("HandleLineFeeds", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=False, description="The mode to handle line feeds, either 'remove',  'crlf' (carriage return) or 'lf' (line feed). Defaults to 'remove'." )
})

remove_brackets_model = flattener_ns.model("RemoveBrackets", {
    "text": fields.String(required=True, description="The input text.")
})

remove_html_tags_model = flattener_ns.model("RemoveHtmlTags", {
    "text": fields.String(required=True, description="The input text.")
})

remove_list_markers_model = flattener_ns.model("RemoveListMarkers", {
    "text": fields.String(required=True, description="The input text.")
})

remove_special_characters_model = flattener_ns.model("RemoveSpecialCharacters", {
    "text": fields.String(required=True, description="The input text."),
    "remove_unicode": fields.Boolean(required=False, description="If True, removes unicode characters. If False, does not remove unicode. Defaults to False.")
})

remove_stopwords_model = flattener_ns.model("RemoveStopwords", {
    "text": fields.String(required=True, description="The input text."),
    "stop_words": fields.List(fields.String, required=False, description="A custom list of stopwords to remove. If None, uses the default set of English stopwords from NLTK. Defaults to None.")
})

remove_whitespace_model = flattener_ns.model("RemoveWhiteSpace", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=True, description="The mode to remove whitespaces, either 'leading', 'trailing', 'all' or 'strip'. Defaults to 'strip'."),
    "keep_duplicates": fields.Boolean(required=False, description="Whether to keep duplicate whitespaces. Defaults to False.")
})

# =================================================================================================================================================
# NORMALIZER MODELS
# =================================================================================================================================================

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

# =================================================================================================================================================
# SEGMENTER MODELS
# =================================================================================================================================================

extract_ngrams_model = segmenter_ns.model("ExtractNgrams", {
    "text": fields.String(required=True, description="The input text."),
    "n": fields.Integer(required=False, description="The number of grams for the n-grams. Defaults to 2."),
    "padding": fields.Boolean(required=False, description="Whether to add padding to the start and end of sentences. Defaults to False"),
    "tokens": fields.List(fields.String, required=False, description="Custom token list. If none, the text will be split by spaces.")
})

tokenize_sentences_model = segmenter_ns.model("TokenizeSentences", {
    "text": fields.String(required=True, description="The input text."),
})

tokenize_words_model = segmenter_ns.model("TokenizeWords", {
    "text": fields.String(required=True, description="The input text."),
})

# =================================================================================================================================================
# TRANSFORMER MODELS
# =================================================================================================================================================

change_case_model = transformer_ns.model("ChangeCase", {
    "text": fields.String(required=True, description="The input text."), 
    "case": fields.String(required=False, description="The case type, either 'lower', 'upper', 'title' or 'capitalize'. Defaults to 'lower'.")
})

convert_numbers_to_words_model = transformer_ns.model("ConvertNumbersToWords", {
    "text": fields.String(required=True, description="The input text.")
})

convert_words_to_numbers_model = transformer_ns.model("ConvertWordsToNumbers", {
    "text": fields.String(required=True, description="The input text.")
})

replace_words_model = transformer_ns.model("ReplaceWords", {
    "text": fields.String(required=True, description="The input text."),
    "replacement_dict": fields.Raw(required=True, description="The dictionary mapping words to their replacements."),
    "case_sensitive": fields.Boolean(required=False, description="Flag indicating whether the replacement should be case-sensitive. Defaults to False.")
})

# =================================================================================================================================================
# UTILTIES MODELS
# =================================================================================================================================================

run_pipeline_model = utilities_ns.model("RunPipeline", {
    "text": fields.String(required=True, description="The input text."),
    "operations": fields.List(fields.String, required=True, description="An ordered series of text processing operations to run on the input text."),
    "args": fields.Nested(api.model('OperationArgs', {}), required=False, description="Arguments for the operations. Key is operation name, value is a dictionary of arguments for that operation."),
})
