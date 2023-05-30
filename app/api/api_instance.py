from flask_restx import Api

api = Api(
    version='1.0',
    title='Text PreProcessor API',
    description='A simple api for cleaning and normalizing unstructured text.'
)
