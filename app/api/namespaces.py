# Import third-party libraries
from flask_restx import Namespace

encoder_ns = Namespace("encoder", description="This namespace provides functions that encode or embed text into different forms.")
flattener_ns = Namespace("flattener", description="This namespace contains methods designed to simplify or reduce the complexity of the text, such as removing line breaks, whitespace, or special characters.")
normalizer_ns = Namespace("normalizer", description="This namespace provides utilities to standardize and normalize text, such as removing punctuation, handling unicode, or lemmatizing words.")
segmenter_ns = Namespace("segmenter", description="This namespace includes functions that divide text into meaningful segments or units, such as sentences, n-grams or tokens.")
transformer_ns = Namespace("transformer", description="This namespace contains functions that transform the format or representation of text, such as changing case or converting numbers to words.")
utilities_ns = Namespace("utilities", description="This namespace contains methods that provide information about the available methods and also allow users to create and execute a comprehensive text preprocessing pipeline.")
