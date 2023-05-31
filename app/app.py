# Import third-party libraries
import inspect
from flask import Flask
from flask_restx import Resource
from typing import Dict, Any
from werkzeug.middleware.proxy_fix import ProxyFix

# Import project code
from textpreprocessor import models, utils
from textpreprocessor.api_instance import api
from textpreprocessor.namespaces import encoder_ns, flattener_ns, normalizer_ns, segmenter_ns, transformer_ns, utilities_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

namespaces = [encoder_ns, flattener_ns, normalizer_ns, segmenter_ns, transformer_ns, utilities_ns]
for namespace in namespaces:
    api.add_namespace(namespace)

# =================================================================================================================================================
# ENCODER ROUTES
# =================================================================================================================================================

@encoder_ns.route("/encode_text")
class EncodeTextResource(Resource):
    @encoder_ns.expect(models.encode_text_model)
    def post(self):
        """
        This method encodes given text using a specified encoding.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        encoding: str = data.get("encoding", "utf-8")
        errors: str = data.get("errors", "strict")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.encode_text(text, encoding, errors)
        return {"result": result}, 200

# =================================================================================================================================================
# FLATTENER ROUTES
# =================================================================================================================================================

@flattener_ns.route("/handle_line_feeds")
class HandleLineFeedsResource(Resource):
    @flattener_ns.expect(models.handle_line_feeds_model)
    def post(self):
        """
        This method handles line feeds in the text based on the selected mode.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        mode: str = data.get("mode", "remove")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.handle_line_feeds(text, mode)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_brackets")
class RemoveBracketsResource(Resource):
    @flattener_ns.expect(models.remove_brackets_model)
    def post(self):
        """
        This method removes content inside brackets, braces, and parentheses.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_brackets(text)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_html_tags")
class RemoveHtmlTagsResource(Resource):
    @flattener_ns.expect(models.remove_html_tags_model)
    def post(self):
        """
        This method removes HTML tags from the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_html_tags(text)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_list_markers")
class RemoveListMarkersResource(Resource):
    @flattener_ns.expect(models.remove_list_markers_model)
    def post(self):
        """
        This method removes itemized list markers (numbering and bullets) from given text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_list_markers(text)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_special_characters")
class RemoveSpecialCharactersResource(Resource):
    @flattener_ns.expect(models.remove_special_characters_model)
    def post(self):
        """
        This method removes special characters from the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        remove_unicode: bool = data.get("remove_unicode", False)
        custom_characters: str = data.get("custom_characters", None)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_special_characters(text, remove_unicode, custom_characters)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_stopwords")
class RemoveStopwordsResource(Resource):
    @flattener_ns.expect(models.remove_stopwords_model)
    def post(self):
        """
        This method removes stopwords from the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        stop_words: list = data.get("stop_words", None)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_stopwords(text, stop_words)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_whitespace")
class RemoveWhiteSpaceResource(Resource):
    @flattener_ns.expect(models.remove_whitespace_model)
    def post(self):
        """
        This method removes whitespace from the text based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        mode: str = data.get("mode", "strip")
        keep_duplicates: bool = data.get("keep_duplicates", False)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_whitespace(text, mode, keep_duplicates)
        return {"result": result}, 200
    
# =================================================================================================================================================
# NORMALIZER ROUTES
# =================================================================================================================================================
    
@normalizer_ns.route("/expand_contractions")
class ExpandContractionsResource(Resource):
    @normalizer_ns.expect(models.expand_contractions_model)
    def post(self):        
        """
        This method expands contractions in a given text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.expand_contractions(text)
        return {"result": result}, 200

@normalizer_ns.route("/lemmatize_text")
class LemmatizeTextResource(Resource):
    @normalizer_ns.expect(models.lemmatize_text_model)
    def post(self):
        """
        This method uses lemmatization to processes the words in the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.lemmatize_text(text)
        return {"result": result}, 200

@normalizer_ns.route("/normalize_unicode")
class NormalizeUnicodeResource(Resource):
    @normalizer_ns.expect(models.normalize_unicode_model)
    def post(self):
        """
        This method normalizes unicode characters in given text to remove umlauts, accents, etc.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.normalize_unicode(text)
        return {"result": result}, 200

@normalizer_ns.route("/remove_numbers")
class RemoveNumbersResource(Resource):
    @normalizer_ns.expect(models.remove_numbers_model)
    def post(self):
        """
        This method removes all digits from the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_numbers(text)
        return {"result": result}, 200
    
@normalizer_ns.route("/remove_punctuation")
class RemovePunctutationResource(Resource):
    @normalizer_ns.expect(models.remove_punctuation_model)
    def post(self):
        """
        This method removes punctuations from the text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        punctuations: str = data.get("punctuations", None)
        remove_duplicates: bool = data.get("remove_duplicates", False)

        if not text: 
            return {"error": "No text provided."}, 400
        
        result = utils.remove_punctuation(text, punctuations, remove_duplicates)
        return {"result": result}, 200
    
@normalizer_ns.route("/stem_words")
class StemWordsResource(Resource):
    @normalizer_ns.expect(models.stem_words_model)
    def post(self):
        """
        This method uses stemming to processes the words in the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        stemmer: str = data.get("stemmer", "porter")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.stem_text(text, stemmer)
        return {"result": result}, 200
    
# =================================================================================================================================================
# SEGMENTER ROUTES
# =================================================================================================================================================

@segmenter_ns.route("/ngrams")
class ExtractNgramsResource(Resource):
    @segmenter_ns.expect(models.extract_ngrams_model)
    def post(self):
        """
        This method extract n-grams from the text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        n: int = data.get("n", 2)
        padding: bool = data.get("padding", False)
        tokens: list = data.get("tokens", [])

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.extract_ngrams(text, n, padding, tokens)
        return {"result": result}, 200
    
@segmenter_ns.route("/sentences")
class TokenizeSentencesResource(Resource):
    @segmenter_ns.expect(models.tokenize_sentences_model)
    def post(self):
        """
        This method tokenizes the input text into sentences or words based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.tokenize_sentences(text)
        return {"result": result}, 200
    
@segmenter_ns.route("/words")
class TokenizeWordsResource(Resource):
    @segmenter_ns.expect(models.tokenize_words_model)
    def post(self):
        """
        This method tokenizes the input text into sentences or words based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.tokenize_words(text)
        return {"result": result}, 200

# =================================================================================================================================================
# TRANSFORMER ROUTES
# =================================================================================================================================================

@transformer_ns.route("/change_case")
class ChangeCaseResource(Resource):
    @transformer_ns.expect(models.change_case_model)
    def post(self):
        """
        This method changes the case of the text based on the selected case type.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "''")
        case: str = data.get("case", "lower")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.change_case(text, case)
        return {"result": result}, 200
    
@transformer_ns.route("/convert_numbers_to_words")
class ConvertNumbersToWordsResource(Resource):
    @transformer_ns.expect(models.convert_numbers_to_words_model)
    def post(self):
        """
        This method converts numbers in the text to their corresponding words.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.convert_numbers_to_words(text)
        return {"result": result}, 200
    
@transformer_ns.route("/convert_words_to_numbers")
class ConvertWordsToNumbersResource(Resource):
    @transformer_ns.expect(models.convert_words_to_numbers_model)
    def post(self):
        """
        This method converts number-words in the text to their corresponding numbers.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "''")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.convert_words_to_numbers(text)
        return {"result": result}, 200
    
@transformer_ns.route("/replace_words")
class ReplaceWordsResource(Resource):
    @transformer_ns.expect(models.replace_words_model)
    def post(self):
        """
        This method replaces specified words in given text according to a replacement dictionary.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        replacement_dict: dict = data.get("replacement_dict", {})
        case_sensitive: bool = data.get("case_sensitive", False)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.replace_words(text, replacement_dict, case_sensitive)
        return {"result": result}, 200

# =================================================================================================================================================
# UTILITIES ROUTES
# =================================================================================================================================================

@utilities_ns.route("/actuator")
class ActuatorResource(Resource):
    def get(self):
        """
        This method displays a message that confirms that the service is up and running.
        """
        return {"message": "Service is running"}, 200

@utilities_ns.route("/methods")
class MethodsResource(Resource):
    def get(self):
        """
        This method displays a list of all available methods for processing text.
        """
        available_methods = [name for name, _ in inspect.getmembers(utils, inspect.isfunction) 
                             if not name.startswith("_")]

        if not available_methods:
            return "", 204
        
        return {"available_methods": available_methods}, 200
    
@utilities_ns.route("/run_pipeline")
class RunPipelineResource(Resource):
    @utilities_ns.expect(models.run_pipeline_model)
    def post (self):
        """
        This method applies an ordered series of text processing operations to the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        operations: list = data.get("operations", [])

        if not text:
            return {"error": "No text provided."}, 400
        
        if not operations:
            return {"error": "No operations provided."}, 400
        
        result = text
        for operation in operations:
            if operation not in utils.__dict__:
                return {"error": f"Invalid operation specified: {operation}"}, 400
            
            result = utils.__dict__[operation](result)
        
        return {"result": result}, 200

if __name__ == '__main__':
    app.run(debug=True)
