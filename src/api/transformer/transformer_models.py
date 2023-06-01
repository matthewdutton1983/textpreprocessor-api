# Import third-party libraries
from flask_restx import fields, Namespace

transformer_ns = Namespace("transformer", description="This service contains functions that transform the format or representation of text, such as changing case or converting numbers to words.")

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
