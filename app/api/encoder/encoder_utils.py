# Import standard libraries
import base64


def encode_text(text: str, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
    """
    This method encodes given text using a specified encoding.

    Parameters:
    - text (str): The input text to encode.
    - encoding (str): The encoding type to use. Defaults to 'utf-8'.
    - errors (str): The error handling strategy to use. Defaults to 'strict'.

    Returns:
    - bytes: The base64-encoded string representation of the text.

    Raises:
    ValueError: If an unsupported encoding type or error handling strategy is specified.
    """
    encodings = ['utf-8', 'ascii']

    if encoding not in encodings:
        raise ValueError(
            "Invalid encoding type. Only 'utf-8' and 'ascii' are supported.")

    if errors not in ['strict', 'ignore', 'replace']:
        raise ValueError(
            "Invalid error handling strategy. Only 'strict', 'ignore', and 'replace' are supported.")

    encoded_text = text.encode(encoding, errors=errors)
    
    return base64.b64encode(encoded_text).decode("utf-8")
