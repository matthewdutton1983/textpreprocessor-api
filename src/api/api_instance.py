from flask_restx import Api

api = Api(
    version="1.0",
    title="Text PreProcessing API",
    description="This API provides a collection of text processing utilities that can be used to encode, flatten, normalize, segment, and transform text. The API is organized into different namespaces, each containing related functions."
)
