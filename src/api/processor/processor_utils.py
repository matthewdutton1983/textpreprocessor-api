# Import standard libraries
import inspect

# Import project code
from api.encoder import encoder_utils
from api.flattener import flattener_utils
from api.normalizer import normalizer_utils
from api.segmenter import segmenter_utils
from api.transformer import transformer_utils
from log_config import Logger

logger = Logger().get_logger()

utils = {
    "encoder": encoder_utils, 
    "flattener": flattener_utils, 
    "normalizer": normalizer_utils, 
    "segmenter": segmenter_utils, 
    "transformer": transformer_utils
}


def list_available_methods():
    """
    This method returns a list of all available methods for text processing.

    Returns:
    - list: The names of all available methods.
    """
    available_methods = []
    
    for _, module in utils.items():
        available_methods.extend([name for name, _ in inspect.getmembers(module, inspect.isfunction) 
                                  if not name.startswith("_")])
    
    available_methods.sort()

    return available_methods


def custom_pipeline(text: str, operations: list, args: dict) -> str:
    """
    This method applies a custom ordered series of text processing operations to the input text.

    Parameters:
    - text (str): The input text.
    - operations (list): An ordered list of operations to run on the text.
    - args (dict): A dictionary mapping operations to their arguments.

    Returns:
    - str: The processed text after all operations have been applied.
    """
    result = text
    
    for operation in operations:
        operation_found = False
        for _, module in utils.items():
            if hasattr(module, operation):
                operation_func = getattr(module, operation)
                operation_args = args.get(operation, {})
                result = operation_func(result, **operation_args)
                operation_found = True
                break
        if not operation_found:
            return {"error": f"Invalid operation specified: {operation}"}, 400

    return result


def default_pipeline(text: str) -> str:
    """
    This method applies a preset ordered series of text processing operations to the input text.

    Parameters:
    - text (str): This input text.

    Returns:
    - str: The processed text after all operations have been applied.
    """
    default_operations = [
        "expand_contractions",
        "change_case",
        "handle_line_feeds",
        "remove_whitespace",
        "remove_special_characters",
        "remove_punctuation",
    ]

    default_args = {
        "change_case": {
            "case": "lower"
            }
    }

    result = text

    for operation in default_operations:
        operation_found = False
        for _, module in utils.items():
            if hasattr(module, operation):
                operation_func = getattr(module, operation)
                operation_args = default_args.get(operation, {})
                result = operation_func(result, **operation_args)
                operation_found = True
                break
        if not operation_found:
            return {"error": f"Invalid operation specified: {operation}"}, 400
        
    return result