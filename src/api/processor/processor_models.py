# Import third-party libraries
from flask_restx import fields, Namespace

# Import project code
from api.api_instance import api

processor_ns = Namespace("processor", description="This service contains methods to create and execute a comprehensive text processing pipeline.")

run_pipeline_model = processor_ns.model("RunPipeline", {
    "text": fields.String(required=True, description="The input text."),
    "operations": fields.List(fields.String, required=True, description="An ordered series of text processing operations to run on the input text."),
    "args": fields.Nested(api.model('OperationArgs', {}), required=False, description="Arguments for the operations. Key is operation name, value is a dictionary of arguments for that operation."),
})
