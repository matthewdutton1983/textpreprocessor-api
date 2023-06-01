# Import third-party libraries
import inspect
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from . import normalizer_utils
from .normalizer_models import *
from ..api_instance import api
from log_config import Logger

logger = Logger().get_logger()

@normalizer_ns.route("/expand_contractions")
class ExpandContractionsResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer_utils.expand_contractions))
    @normalizer_ns.expect(expand_contractions_model)
    def post(self):        
        """
        Expands contractions in a given text.
        """
        try:    
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = normalizer_utils.expand_contractions(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500

@normalizer_ns.route("/lemmatize_text")
class LemmatizeTextResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer_utils.lemmatize_text))
    @normalizer_ns.expect(lemmatize_text_model)
    def post(self):
        """
        Lemmatizes the words in the input text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = normalizer_utils.lemmatize_text(text)
        
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500

@normalizer_ns.route("/normalize_unicode")
class NormalizeUnicodeResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer_utils.normalize_unicode))
    @normalizer_ns.expect(normalize_unicode_model)
    def post(self):
        """
        Normalizes unicode characters in given text to remove umlauts, accents, etc.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = normalizer_utils.normalize_unicode(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500

@normalizer_ns.route("/remove_numbers")
class RemoveNumbersResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer_utils.remove_numbers))
    @normalizer_ns.expect(remove_numbers_model)
    def post(self):
        """
        Removes all digits from the input text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = normalizer_utils.remove_numbers(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@normalizer_ns.route("/remove_punctuation")
class RemovePunctutationResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer_utils.remove_punctuation))
    @normalizer_ns.expect(remove_punctuation_model)
    def post(self):
        """
        Removes punctuations from the text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            punctuations: str = data.get("punctuations", None)
            remove_duplicates: bool = data.get("remove_duplicates", False)

            if not text: 
                return {"error": "No text provided."}, 400
            
            result = normalizer_utils.remove_punctuation(text, punctuations, remove_duplicates)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@normalizer_ns.route("/stem_words")
class StemWordsResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer_utils.stem_text))
    @normalizer_ns.expect(stem_words_model)
    def post(self):
        """
        Stems the words in the input text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            stemmer: str = data.get("stemmer", "porter")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = normalizer_utils.stem_text(text, stemmer)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
