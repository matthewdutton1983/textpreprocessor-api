# Import third-party libraries
import inspect
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from . import segmenter_utils
from .segmenter_models import *
from ..api_instance import api
from log_config import Logger

logger = Logger().get_logger()

@segmenter_ns.route("/ngrams")
class ExtractNgramsResource(Resource):
    @segmenter_ns.doc(description=inspect.getdoc(segmenter_utils.extract_ngrams))
    @segmenter_ns.expect(extract_ngrams_model)
    def post(self):
        """
        Extracts n-grams from the text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            n: int = data.get("n", 2)
            padding: bool = data.get("padding", False)
            tokens: list = data.get("tokens", [])

            if not text:
                return {"error": "No text provided."}, 400
            
            result = segmenter_utils.extract_ngrams(text, n, padding, tokens)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@segmenter_ns.route("/sentences")
class TokenizeSentencesResource(Resource):
    @segmenter_ns.doc(description=inspect.getdoc(segmenter_utils.tokenize_sentences))
    @segmenter_ns.expect(tokenize_sentences_model)
    def post(self):
        """
        Tokenizes the input text into sentences or words based on the selected mode.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = segmenter_utils.tokenize_sentences(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@segmenter_ns.route("/words")
class TokenizeWordsResource(Resource):
    @segmenter_ns.doc(description=inspect.getdoc(segmenter_utils.tokenize_words))
    @segmenter_ns.expect(tokenize_words_model)
    def post(self):
        """
        Tokenizes the input text into sentences or words based on the selected mode.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = segmenter_utils.tokenize_words(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
