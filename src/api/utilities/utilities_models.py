# Import third-party libraries
from flask_restx import fields, Namespace

# Import project code
from api.api_instance import api

utilities_ns = Namespace("utilities", description="This namespace contains methods that provide information about the available methods and also allow users to create and execute a comprehensive text preprocessing pipeline.")

run_pipeline_model = utilities_ns.model("RunPipeline", {
    "text": fields.String(required=True, description="The input text."),
    "operations": fields.List(fields.String, required=True, description="An ordered series of text processing operations to run on the input text."),
    "args": fields.Nested(api.model('OperationArgs', {}), required=False, description="Arguments for the operations. Key is operation name, value is a dictionary of arguments for that operation."),
})
