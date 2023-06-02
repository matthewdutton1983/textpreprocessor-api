# Import third-party libraries
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from .import processor_utils
from .processor_models import *
from ..api_instance import api
from log_config import Logger

logger = Logger().get_logger()

@processor_ns.route("/methods")
class MethodsResource(Resource):
    def get(self):
        """
        This method displays a list of all available methods for processing text.
        """
        try:
            available_methods = processor_utils.list_available_methods()

            if not available_methods:
                return "", 204
            
            return {"available_methods": available_methods}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@processor_ns.route("/custom-pipeline")
class CustomPipelineResource(Resource):
    @processor_ns.expect(custom_pipeline_model)
    def post(self):
        """
        Applies a custom ordered series of text processing operations to the input text.
        """
        data: Dict[str, Any] = api.payload
        text: str = data.get("text", "")
        operations: list = data.get("operations", [])
        args: dict = data.get("args", {})

        if not text:
            logger.error("No text provided.")
            return {"error": "No text provided."}, 400
        
        if not operations:
            logger.error("No operations provided.")
            return {"error": "No operations provided."}, 400
        
        try:
            result = processor_utils.custom_pipeline(text, operations, args)
        except Exception as e:
            logger.error(f"An error occurred during processing: {str(e)}")
            return {"error": str(e)}, 500    
        
        return {"result": result}, 200
    
@processor_ns.route("/default-pipeline")
class DefaultPipelineResource(Resource):
    @processor_ns.expect(default_pipeline_model)
    def post(self):
        """
        Applies a preset ordered series of text processing operations to the input text.
        """
        data: Dict[str, Any] = api.payload
        text: str = data.get("text", "")

        if not text:
            logger.error("No text provided.")
            return {"error": "No text provided."}, 400
        
        try:
            result = processor_utils.default_pipeline(text)
        except Exception as e:
            logger.error(f"An error occurred during processing: {str(e)}")
            return {"error": str(e)}, 500
        
        return {"result": result}, 200
        
