# Import third-party libraries
from flask_restx import Resource
from typing import Dict, Any

# Import project code
from .import utilities_utils
from .utilities_models import *
from ..api_instance import api
from log_config import Logger

logger = Logger().get_logger()

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
        try:
            available_methods = utilities_utils.list_available_methods()

            if not available_methods:
                return "", 204
            
            return {"available_methods": available_methods}, 200
        
        except Exception as e:
            logger.exception("An error occurred during the encoding process.")
            return {"error": f"An unexpected error occurred: {str(e)}"}, 500
    
@utilities_ns.route("/pipeline")
class RunPipelineResource(Resource):
    @utilities_ns.expect(run_pipeline_model)
    def post (self):
        """
        Applies an ordered series of text processing operations to the input text.
        """
        data: Dict[str, Any] = api.payload
        text: str = data.get("text", "")
        operations: list = data.get("operations", [])
        args: dict = data.get("args", {})

        logger.info(f"Received request: Text - {text[:50]}..., Operations - {operations}, Args - {args}")

        if not text:
            logger.error("No text provided.")
            return {"error": "No text provided."}, 400
        
        if not operations:
            logger.error("No operations provided.")
            return {"error": "No operations provided."}, 400
        
        try:
            result = utilities_utils.run_pipeline(text, operations, args)
            logger.info(f"Processing completed. Result - {result[:50]}...")

        except Exception as e:
            logger.error(f"An error occurred during processing: {str(e)}")
            return {"error": str(e)}, 500    
        
        return {"result": result}, 200
