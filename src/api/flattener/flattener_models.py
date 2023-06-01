# Import third-party libraries
from flask_restx import fields, Namespace

flattener_ns = Namespace("flattener", description="This service contains methods designed to simplify or reduce the complexity of the text, such as removing line breaks, whitespace, or special characters.")

handle_line_feeds_model = flattener_ns.model("HandleLineFeeds", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=False, description="The mode to handle line feeds, either 'remove',  'crlf' (carriage return) or 'lf' (line feed). Defaults to 'remove'." )
})

remove_brackets_model = flattener_ns.model("RemoveBrackets", {
    "text": fields.String(required=True, description="The input text.")
})

remove_html_tags_model = flattener_ns.model("RemoveHtmlTags", {
    "text": fields.String(required=True, description="The input text.")
})

remove_list_markers_model = flattener_ns.model("RemoveListMarkers", {
    "text": fields.String(required=True, description="The input text.")
})

remove_special_characters_model = flattener_ns.model("RemoveSpecialCharacters", {
    "text": fields.String(required=True, description="The input text."),
    "remove_unicode": fields.Boolean(required=False, description="If True, removes unicode characters. If False, does not remove unicode. Defaults to False.")
})

remove_stopwords_model = flattener_ns.model("RemoveStopwords", {
    "text": fields.String(required=True, description="The input text."),
    "stop_words": fields.List(fields.String, required=False, description="A custom list of stopwords to remove. If None, uses the default set of English stopwords from NLTK. Defaults to None.")
})

remove_whitespace_model = flattener_ns.model("RemoveWhiteSpace", {
    "text": fields.String(required=True, description="The input text."),
    "mode": fields.String(required=True, description="The mode to remove whitespaces, either 'leading', 'trailing', 'all' or 'strip'. Defaults to 'strip'."),
    "keep_duplicates": fields.Boolean(required=False, description="Whether to keep duplicate whitespaces. Defaults to False.")
})
