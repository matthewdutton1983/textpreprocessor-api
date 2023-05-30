import inspect
from api import utils
from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from typing import Dict, Any, List, Callable, Type, Tuple, Union, Optional

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(
    app,
    version='1.0',
    title='Text PreProcessor API',
    description='A simple api for cleaning and normalizing unstructured text.'
)

preprocessing_steps: Dict[str, Callable[..., Any]] = {}

for name, func in inspect.getmembers(utils, inspect.isfunction):
    preprocessing_steps[name] = func


def create_route(func: Callable[..., Any]) -> Type[Resource]:
    """
    This function dynamically creates a Flask-RestX Resource (route) for each
    text preprocessing function from the 'utils' module.
    """

    @api.route(f'/{func.__name__}')
    class TextProcessing(Resource):
        """
        This class represents a single route for text processing. It expects
        a JSON object containing 'text' and optional 'args'.
        """

        @api.expect(api.model('TextProcessing', {'text': fields.String, 'args': fields.Raw}))
        def post(self) -> Tuple[Dict[str, Any], int]:
            """
            This function handles POST requests to the route. It applies the
            text processing function associated with this route to the input text.
            """
            data: Dict[str, Any] = api.payload
            text: str = data.get('text', '')
            args: Dict[str, Any] = data.get('args', {})

            if not text:
                return {'error': 'No text provided'}, 400

            result = func(text, **args)

            return {'result': result}, 200

    return TextProcessing


for name, func in preprocessing_steps.items():
    create_route(func)


@api.route('/methods')
class Methods(Resource):
    """
    This class represents the route that provides information about the available text processing methods.
    """

    def get(self) -> Union[Tuple[str, int], Tuple[Dict[str, List[str]], int]]:
        """
        This function handles GET requests to the '/methods' route. It returns a list of the available methods.
        """
        methods_list: List[str] = [name for name, _ in inspect.getmembers(
            utils, inspect.isfunction) if not name.startswith('_')]

        if not methods_list:
            return '', 204

        return {'available_methods': methods_list}, 200


@api.route('/<method_name>/info')
@api.param('method_name', 'The name of the method')
class MethodInfo(Resource):
    """
    This class represents the route that provides information about a specific method.
    """

    def get(self, method_name: str) -> Tuple[Dict[str, str], int]:
        """
        This function handles GET requests to the '/<method_name>/info' route. It returns the docstring of the specified method.
        """
        func: Optional[Callable[..., Any]
                       ] = preprocessing_steps.get(method_name)

        if func is None:
            return {'error': f"No method with name: {method_name}"}, 404

        docstring: str = func.__doc__

        return {'docstring': docstring or 'No docstring available.'}, 200


if __name__ == '__main__':
    """
    If this module is run directly, it starts the Flask application.
    """
    app.run(debug=True)
