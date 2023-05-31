# Import third-party libraries
import inspect
from flask import Flask
from flask_restx import Resource
from typing import Dict, Any
from werkzeug.middleware.proxy_fix import ProxyFix

# Import project code
from api import models
from api.api_instance import api
from api.namespaces import encoder_ns, flattener_ns, normalizer_ns, segmenter_ns, transformer_ns, utilities_ns
from utils import encoder, flattener, normalizer, segmenter, transformer

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

namespaces = [encoder_ns, flattener_ns, normalizer_ns, segmenter_ns, transformer_ns, utilities_ns]
for namespace in namespaces:
    api.add_namespace(namespace)

utils = [encoder, flattener, normalizer, segmenter, transformer]

# =================================================================================================================================================
# ENCODER ROUTES
# =================================================================================================================================================

@encoder_ns.route("/encode_text")
class EncodeTextResource(Resource):
    @encoder_ns.doc(description=inspect.getdoc(encoder.encode_text))
    @encoder_ns.expect(models.encode_text_model)
    def post(self):
        """
        Encodes the input text using a specified encoding.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        encoding: str = data.get("encoding", "utf-8")
        errors: str = data.get("errors", "strict")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = encoder.encode_text(text, encoding, errors)
        return {"result": result}, 200

# =================================================================================================================================================
# FLATTENER ROUTES
# =================================================================================================================================================

@flattener_ns.route("/handle_line_feeds")
class HandleLineFeedsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.handle_line_feeds))
    @flattener_ns.expect(models.handle_line_feeds_model)
    def post(self):
        """
        Handles line feeds in the text based on the selected mode.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        mode: str = data.get("mode", "remove")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.handle_line_feeds(text, mode)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_brackets")
class RemoveBracketsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.remove_brackets))
    @flattener_ns.expect(models.remove_brackets_model)
    def post(self):
        """
        Removes content inside brackets, braces, and parentheses.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.remove_brackets(text)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_html_tags")
class RemoveHtmlTagsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.remove_html_tags))
    @flattener_ns.expect(models.remove_html_tags_model)
    def post(self):
        """
        Removes HTML tags from the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.remove_html_tags(text)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_list_markers")
class RemoveListMarkersResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.remove_list_markers))
    @flattener_ns.expect(models.remove_list_markers_model)
    def post(self):
        """
        Removes itemized list markers (numbering and bullets) from given text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.remove_list_markers(text)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_special_characters")
class RemoveSpecialCharactersResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.remove_special_characters))
    @flattener_ns.expect(models.remove_special_characters_model)
    def post(self):
        """
        Removes special characters from the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        remove_unicode: bool = data.get("remove_unicode", False)
        custom_characters: str = data.get("custom_characters", None)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.remove_special_characters(text, remove_unicode, custom_characters)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_stopwords")
class RemoveStopwordsResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.remove_stopwords))
    @flattener_ns.expect(models.remove_stopwords_model)
    def post(self):
        """
        Removes stopwords from the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        stop_words: list = data.get("stop_words", None)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.remove_stopwords(text, stop_words)
        return {"result": result}, 200
    
@flattener_ns.route("/remove_whitespace")
class RemoveWhiteSpaceResource(Resource):
    @flattener_ns.doc(description=inspect.getdoc(flattener.remove_whitespace))
    @flattener_ns.expect(models.remove_whitespace_model)
    def post(self):
        """
        Removes whitespace from the text based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        mode: str = data.get("mode", "strip")
        keep_duplicates: bool = data.get("keep_duplicates", False)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = flattener.remove_whitespace(text, mode, keep_duplicates)
        return {"result": result}, 200
    
# =================================================================================================================================================
# NORMALIZER ROUTES
# =================================================================================================================================================
    
@normalizer_ns.route("/expand_contractions")
class ExpandContractionsResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer.expand_contractions))
    @normalizer_ns.expect(models.expand_contractions_model)
    def post(self):        
        """
        Expands contractions in a given text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = normalizer.expand_contractions(text)
        return {"result": result}, 200

@normalizer_ns.route("/lemmatize_text")
class LemmatizeTextResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer.lemmatize_text))
    @normalizer_ns.expect(models.lemmatize_text_model)
    def post(self):
        """
        Lemmatizes the words in the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = normalizer.lemmatize_text(text)
        return {"result": result}, 200

@normalizer_ns.route("/normalize_unicode")
class NormalizeUnicodeResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer.normalize_unicode))
    @normalizer_ns.expect(models.normalize_unicode_model)
    def post(self):
        """
        Normalizes unicode characters in given text to remove umlauts, accents, etc.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = normalizer.normalize_unicode(text)
        return {"result": result}, 200

@normalizer_ns.route("/remove_numbers")
class RemoveNumbersResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer.remove_numbers))
    @normalizer_ns.expect(models.remove_numbers_model)
    def post(self):
        """
        Removes all digits from the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = normalizer.remove_numbers(text)
        return {"result": result}, 200
    
@normalizer_ns.route("/remove_punctuation")
class RemovePunctutationResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer.remove_punctuation))
    @normalizer_ns.expect(models.remove_punctuation_model)
    def post(self):
        """
        Removes punctuations from the text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        punctuations: str = data.get("punctuations", None)
        remove_duplicates: bool = data.get("remove_duplicates", False)

        if not text: 
            return {"error": "No text provided."}, 400
        
        result = normalizer.remove_punctuation(text, punctuations, remove_duplicates)
        return {"result": result}, 200
    
@normalizer_ns.route("/stem_words")
class StemWordsResource(Resource):
    @normalizer_ns.doc(description=inspect.getdoc(normalizer.stem_text))
    @normalizer_ns.expect(models.stem_words_model)
    def post(self):
        """
        Stems the words in the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        stemmer: str = data.get("stemmer", "porter")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = normalizer.stem_text(text, stemmer)
        return {"result": result}, 200
    
# =================================================================================================================================================
# SEGMENTER ROUTES
# =================================================================================================================================================

@segmenter_ns.route("/ngrams")
class ExtractNgramsResource(Resource):
    @segmenter_ns.doc(description=inspect.getdoc(segmenter.extract_ngrams))
    @segmenter_ns.expect(models.extract_ngrams_model)
    def post(self):
        """
        Extracts n-grams from the text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        n: int = data.get("n", 2)
        padding: bool = data.get("padding", False)
        tokens: list = data.get("tokens", [])

        if not text:
            return {"error": "No text provided."}, 400
        
        result = segmenter.extract_ngrams(text, n, padding, tokens)
        return {"result": result}, 200
    
@segmenter_ns.route("/sentences")
class TokenizeSentencesResource(Resource):
    @segmenter_ns.doc(description=inspect.getdoc(segmenter.tokenize_sentences))
    @segmenter_ns.expect(models.tokenize_sentences_model)
    def post(self):
        """
        Tokenizes the input text into sentences or words based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = segmenter.tokenize_sentences(text)
        return {"result": result}, 200
    
@segmenter_ns.route("/words")
class TokenizeWordsResource(Resource):
    @segmenter_ns.doc(description=inspect.getdoc(segmenter.tokenize_words))
    @segmenter_ns.expect(models.tokenize_words_model)
    def post(self):
        """
        Tokenizes the input text into sentences or words based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = segmenter.tokenize_words(text)
        return {"result": result}, 200

# =================================================================================================================================================
# TRANSFORMER ROUTES
# =================================================================================================================================================

@transformer_ns.route("/change_case")
class ChangeCaseResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer.change_case))
    @transformer_ns.expect(models.change_case_model)
    def post(self):
        """
        Changes the case of the text based on the selected case type.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "''")
        case: str = data.get("case", "lower")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = transformer.change_case(text, case)
        return {"result": result}, 200
    
@transformer_ns.route("/convert_numbers_to_words")
class ConvertNumbersToWordsResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer.convert_numbers_to_words))
    @transformer_ns.expect(models.convert_numbers_to_words_model)
    def post(self):
        """
        Converts numbers in the text to their corresponding words.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = transformer.convert_numbers_to_words(text)
        return {"result": result}, 200
    
@transformer_ns.route("/convert_words_to_numbers")
class ConvertWordsToNumbersResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer.convert_words_to_numbers))
    @transformer_ns.expect(models.convert_words_to_numbers_model)
    def post(self):
        """
        Converts number-words in the text to their corresponding numbers.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "''")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = transformer.convert_words_to_numbers(text)
        return {"result": result}, 200
    
@transformer_ns.route("/replace_words")
class ReplaceWordsResource(Resource):
    @transformer_ns.doc(description=inspect.getdoc(transformer.replace_words))
    @transformer_ns.expect(models.replace_words_model)
    def post(self):
        """
        Replaces specified words in given text according to a replacement dictionary.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        replacement_dict: dict = data.get("replacement_dict", {})
        case_sensitive: bool = data.get("case_sensitive", False)

        if not text:
            return {"error": "No text provided."}, 400
        
        result = transformer.replace_words(text, replacement_dict, case_sensitive)
        return {"result": result}, 200

# =================================================================================================================================================
# UTILITIES ROUTES
# =================================================================================================================================================

@utilities_ns.route("/actuator")
class ActuatorResource(Resource):
    def get(self):
        """
        Displays a message that confirms that the service is up and running.
        """
        return {"message": "Service is running"}, 200

@utilities_ns.route("/methods")
class MethodsResource(Resource):
    def get(self):
        """
        This method displays a list of all available methods for processing text.
        """
        available_methods = []

        for module in utils:
            available_methods.extend([name for name, _ in inspect.getmembers(module, inspect.isfunction) 
                                      if not name.startswith("_")])
        
        available_methods.sort()

        if not available_methods:
            return "", 204
        
        return {"available_methods": available_methods}, 200
    
@utilities_ns.route("/run_pipeline")
class RunPipelineResource(Resource):
    @utilities_ns.expect(models.run_pipeline_model)
    def post (self):
        """
        Applies an ordered series of text processing operations to the input text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        operations: list = data.get("operations", [])
        args: dict = data.get("args", {}) # how do I add args to each operation

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
