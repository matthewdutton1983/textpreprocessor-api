# Import third-party libraries
import inspect
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from . import transformer_utils
from .transformer_models import *
from ..api_instance import api
from log_config import Logger

logger = Logger().get_logger()

@transformer_ns.route("/change_case")
class ChangeCaseResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer_utils.change_case))
    @transformer_ns.expect(change_case_model)
    def post(self):
        """
        Changes the case of the text based on the selected case type.
        """
        try:
            data: Dict[str, Any] = api.payload    
            text: str = data.get("text", "''")
            case: str = data.get("case", "lower")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = transformer_utils.change_case(text, case)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@transformer_ns.route("/convert_numbers_to_words")
class ConvertNumbersToWordsResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer_utils.convert_numbers_to_words))
    @transformer_ns.expect(convert_numbers_to_words_model)
    def post(self):
        """
        Converts numbers in the text to their corresponding words.
        """
        try:
            data: Dict[str, Any] = api.payload    
            text: str = data.get("text", "")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = transformer_utils.convert_numbers_to_words(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@transformer_ns.route("/convert_words_to_numbers")
class ConvertWordsToNumbersResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer_utils.convert_words_to_numbers))
    @transformer_ns.expect(convert_words_to_numbers_model)
    def post(self):
        """
        Converts number-words in the text to their corresponding numbers.
        """
        try:
            data: Dict[str, Any] = api.payload    
            text: str = data.get("text", "''")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = transformer_utils.convert_words_to_numbers(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")    
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@transformer_ns.route("/replace_words")
class ReplaceWordsResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer_utils.replace_words))
    @transformer_ns.expect(replace_words_model)
    def post(self):
        """
        Replaces specified words in given text according to a replacement dictionary.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            replacement_dict: dict = data.get("replacement_dict", {})
            case_sensitive: bool = data.get("case_sensitive", False)

            if not text:
                return {"error": "No text provided."}, 400
            
            result = transformer_utils.replace_words(text, replacement_dict, case_sensitive)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500

