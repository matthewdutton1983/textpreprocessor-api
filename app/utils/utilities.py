# Import standard libraries
import inspect

# Import project code
from utils import encoder, flattener, normalizer, segmenter, transformer

utils = {
    "encoder": encoder, 
    "flattener": flattener, 
    "normalizer": normalizer, 
    "segmenter": segmenter, 
    "transformer": transformer
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


def run_pipeline(text: str, operations: list, args: dict) -> str:
    """
    This method applies an ordered series of text processing operations to the input text.

    Parameters:
    - text (str): The input text.
    - operations (list): An ordered list of operations to run on the text.
    - args (dict): A dictionary mapping operations to their arguments.

    Returns:
    - str: The text after all operations have been applied.
    """
    result = text
    for operation in operations:
        for _, module in utils.items():
            if hasattr(module, operation):
                operation_func = getattr(module, operation)
                operation_args = args.get(operation, {})
                result = operation_func(result, **operation_args)
        else:
                return {"error": f"Invalid operation specified: {operation}"}, 400
    return result