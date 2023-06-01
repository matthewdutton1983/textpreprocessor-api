# Import third-party libraries
import inspect
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from ..models.encoder_models import *
from api.api_instance import api
from utils import encoder_utils
from log_config import Logger

logger = Logger().get_logger()

@encoder_ns.route("/encode_text")
class EncodeTextResource(Resource):
    @encoder_ns.doc(description=inspect.getdoc(encoder_utils.encode_text))
    @encoder_ns.expect(encode_text_model)
    def post(self):
        """
        Encodes the input text using a specified encoding.
        """
        try:
            data: Dict[str, Any] = api.payload
            text: str = data.get("text", "")
            encoding: str = data.get("encoding", "utf-8")
            errors: str = data.get("errors", "strict")

            if not text:
                return {"error": "No text provided."}, 400
            
            result = encoder_utils.encode_text(text, encoding, errors)
            return {"result": result}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
