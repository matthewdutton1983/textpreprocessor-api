# Import third-party libraries
from flask_restx import fields, Namespace

encoder_ns = Namespace("encoder", description="This service provides functions that encode or embed text into different forms.")

encode_text_model = encoder_ns.model("EncodeText", {
    "text": fields.String(required=True, description="The input text."),
    "encoding": fields.String(required=False, description="The encoding type to use. Defaults to 'utf-8'."),
    "errors": fields.String(required=False, description="The error handling strategy to use, either 'strict', 'ignore' or 'replace'. Defaults to 'strict'.")
})
