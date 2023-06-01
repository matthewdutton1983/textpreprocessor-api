# Import third-party libraries
import inspect
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from ..models.flattener_models import *
from api.api_instance import api
from utils import flattener_utils
from log_config import Logger

logger = Logger().get_logger()

@flattener_ns.route("/handle_line_feeds")
class HandleLineFeedsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.handle_line_feeds))
    @flattener_ns.expect(handle_line_feeds_model)
    def post(self):
        """
        Handles line feeds in the text based on the selected mode.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            mode: str = data.get("mode", "remove")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.handle_line_feeds(text, mode)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@flattener_ns.route("/remove_brackets")
class RemoveBracketsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.remove_brackets))
    @flattener_ns.expect(remove_brackets_model)
    def post(self):
        """
        Removes content inside brackets, braces, and parentheses.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.remove_brackets(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@flattener_ns.route("/remove_html_tags")
class RemoveHtmlTagsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.remove_html_tags))
    @flattener_ns.expect(remove_html_tags_model)
    def post(self):
        """
        Removes HTML tags from the input text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.remove_html_tags(text)
            
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@flattener_ns.route("/remove_list_markers")
class RemoveListMarkersResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.remove_list_markers))
    @flattener_ns.expect(remove_list_markers_model)
    def post(self):
        """
        Removes itemized list markers (numbering and bullets) from given text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            
            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.remove_list_markers(text)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@flattener_ns.route("/remove_special_characters")
class RemoveSpecialCharactersResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.remove_special_characters))
    @flattener_ns.expect(remove_special_characters_model)
    def post(self):
        """
        Removes special characters from the input text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            remove_unicode: bool = data.get("remove_unicode", False)
            custom_characters: str = data.get("custom_characters", None)

            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.remove_special_characters(text, remove_unicode, custom_characters)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@flattener_ns.route("/remove_stopwords")
class RemoveStopwordsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.remove_stopwords))
    @flattener_ns.expect(remove_stopwords_model)
    def post(self):
        """
        Removes stopwords from the input text.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            stop_words: list = data.get("stop_words", None)

            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.remove_stopwords(text, stop_words)            
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@flattener_ns.route("/remove_whitespace")
class RemoveWhiteSpaceResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener_utils.remove_whitespace))
    @flattener_ns.expect(remove_whitespace_model)
    def post(self):
        """
        Removes whitespace from the text based on the selected mode.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            mode: str = data.get("mode", "strip")
            keep_duplicates: bool = data.get("keep_duplicates", False)

            if not text:
                return {"error": "No text provided."}, 400
            
            result = flattener_utils.remove_whitespace(text, mode, keep_duplicates)
            
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
