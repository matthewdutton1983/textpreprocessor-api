import inspect
from api.api_instance import api
from api import models, utils
from flask import Flask
from flask_restx import Resource
from werkzeug.middleware.proxy_fix import ProxyFix
from typing import Dict, Any

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

@api.route("/methods")
class MethodsResource(Resource):
    def get(self):
        available_methods = [name for name, _ in inspect.getmembers(utils, inspect.isfunction) 
                             if not name.startswith("_")]

        if not available_methods:
            return "", 204
        
        return {"available_methods": available_methods}, 200


@api.route("/change_case")
class ChangeCaseResource(Resource):
    @api.expect(models.change_case_model)
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
    
@api.route("/check_spelling")
class CheckSpellingResource(Resource):
    @api.expect(models.check_spelling_model)
    def post(self):
        """
        This method corrects spelling mistakes in the text.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        language: str = data.get("language", "en")

        if not text:
            return {"error": "No text provided."}, 400

        result = utils.check_spelling(text, language)
        return {"result": result}, 200
    
@api.route("/convert_numbers_to_words")
class ConvertNumbersToWordsResource(Resource):
    @api.expect(models.convert_numbers_to_words_model)
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
    
@api.route("/convert_words_to_numbers")
class ConvertWordsToNumbersResource(Resource):
    @api.expect(models.convert_words_to_numbers_model)
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
    
@api.route("/encode_text")
class EncodeTextResource(Resource):
    @api.expect(models.encode_text_model)
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
    
@api.route("/expand_contractions")
class ExpandContractionsResource(Resource):
    @api.expect(models.expand_contractions_model)
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
    
@api.route("/extract_ngrams")
class ExtractNgramsResource(Resource):
    @api.expect(models.extract_ngrams_model)
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
    
@api.route("/find_abbreviations")
class FindAbbreviationsResource(Resource):
    @api.expect(models.find_abbreviations_model)
    def post(self):
        """
        This method identifies abbreviations in given text and returns a dictionary of abbreviations and their definitions.
        """
        data: Dict[str, Any] = api.payload
        
        text: str = data.get("text", "")
        
        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.find_abbreviations(text)
        return {"result": result}, 200

@api.route("/handle_line_feeds")
class HandleLineFeedsResource(Resource):
    @api.expect(models.handle_line_feeds_model)
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

@api.route("/lemmatize_text")
class LemmatizeTextResource(Resource):
    @api.expect(models.lemmatize_text_model)
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

@api.route("/normalize_unicode")
class NormalizeUnicodeResource(Resource):
    @api.expect(models.normalize_unicode_model)
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

@api.route("/remove_brackets")
class RemoveBracketsResource(Resource):
    @api.expect(models.remove_brackets_model)
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
    
@api.route("/remove_credit_card_numbers")
class RemoveCreditCardNumbersResource(Resource):
    @api.expect(models.remove_credit_card_numbers_model)
    def post(self):
        """
        This method removes or masks credit card numbers from the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        use_mask: bool = data.get("use_mask", True)
        mask: str = data.get("mask", "<CREDIT_CARD_NUMBER>")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_credit_card_numbers(text, use_mask, mask)
        return {"result": result}, 200
    
@api.route("/remove_email_addresses")
class RemoveEmailResource(Resource):
    @api.expect(models.remove_email_addresses_model)
    def post(self):
        """
        This method removes or masks email addresses from the input text.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        use_mask: bool = data.get("use_mask", True)
        mask: str = data.get("mask", "<EMAIL_ADDRESS>")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_email_addresses(text, use_mask, mask)
        return {"result": result}, 200
    
@api.route("/remove_html_tags")
class RemoveHtmlTagsResource(Resource):
    @api.expect(models.remove_html_tags_model)
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
    
@api.route("/remove_list_markers")
class RemoveHtmlTagsResource(Resource):
    @api.expect(models.remove_list_markers_model)
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
    
@api.route("/remove_names")
class RemoveNamesResource(Resource):
    @api.expect(models.remove_names_model)
    def post(self):
        """
        This method removes or masks all names from the text using named entity recognition.
        """
        data: Dict[str, Any] = api.payload
    
        text: str = data.get("text", "")
        use_mask: bool = data.get("use_mask", True)
        mask: str = data.get("mask", "<NAME>")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_names(text, use_mask, mask)
        return {"result": result}, 200
    
@api.route("/remove_numbers")
class RemoveNumbersResource(Resource):
    @api.expect(models.remove_numbers_model)
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
    
@api.route("/remove_phone_numbers")
class RemovePhoneNumbersResource(Resource):
    @api.expect(models.remove_phone_numbers_model)
    def post(self):
        """
        This method removes or masks phone numbers from the input text.
        """
        data: Dict[str, Any] = api.payload
    
        text: str = data.get("text", "")
        use_mask: bool = data.get("use_mask", True)
        mask: str = data.get("mask", "<PHONE_NUMBER>")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_phone_numbers(text, use_mask, mask)
        return {"result": result}, 200
    
@api.route("/remove_punctuation")
class RemovePunctutationResource(Resource):
    @api.expect(models.remove_punctuation_model)
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
    
@api.route("/remove_social_security")
class RemoveSocialSecurityResource(Resource):
    @api.expect(models.remove_social_security_model)
    def post(self):
        """
        This method masks or removes Social Security Numbers from the input text.
        """
        data: Dict[str, Any] = api.payload
    
        text: str = data.get("text", "")
        use_mask: bool = data.get("use_mask", True)
        mask: str = data.get("mask", "<SOCIAL_SECURITY_NUMBER>")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_social_security(text, use_mask, mask)
        return {"result": result}, 200
    
@api.route("/remove_special_characters")
class RemoveSpecialCharactersResource(Resource):
    @api.expect(models.remove_special_characters_model)
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
    
@api.route("/remove_stopwords")
class RemoveStopwordsResource(Resource):
    @api.expect(models.remove_stopwords_model)
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

@api.route("/remove_url")
class RemoveUrlResource(Resource):
    @api.expect(models.remove_url_model)
    def post(self):
        """
        This method removes or masks website addresses from the input text.
        """
        data: Dict[str, Any] = api.payload
    
        text: str = data.get("text", "")
        use_mask: bool = data.get("use_mask", True)
        mask: str = data.get("mask", "<URL>")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.remove_url(text, use_mask, mask)
        return {"result": result}, 200
    
@api.route("/remove_whitespace")
class RemoveWhiteSpaceResource(Resource):
    @api.expect(models.remove_whitespace_model)
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
    
@api.route("/replace_words")
class ReplaceWordsResource(Resource):
    @api.expect(models.replace_words_model)
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
    
@api.route("/stem_words")
class StemWordsResource(Resource):
    @api.expect(models.stem_words_model)
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
    
@api.route("/tokenize_text")
class TokenizeTextResource(Resource):
    @api.expect(models.tokenize_text_model)
    def post(self):
        """
        This method tokenizes the input text into sentences or words based on the selected mode.
        """
        data: Dict[str, Any] = api.payload

        text: str = data.get("text", "")
        mode: str = data.get("mode", "sentences")

        if not text:
            return {"error": "No text provided."}, 400
        
        result = utils.tokenize_text(text, mode)
        return {"result": result}, 200

if __name__ == '__main__':
    app.run(debug=True)
