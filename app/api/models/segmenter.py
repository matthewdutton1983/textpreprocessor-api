# Import third-party libraries
from flask_restx import fields, Namespace

segmenter_ns = Namespace("segmenter", description="This namespace includes functions that divide text into meaningful segments or units, such as sentences, n-grams or tokens.")

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
