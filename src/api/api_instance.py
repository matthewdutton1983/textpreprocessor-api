from flask_restx import Api

api = Api(
    version="1.0",
    title="Text Preprocessor",
    description="""This API provides a collection of text processing methods that can be used to clean and transform text. The API is organized into several different services, each containing related functions."""
)
