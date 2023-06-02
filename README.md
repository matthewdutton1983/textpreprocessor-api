# Text Preprocessor API

This API provides a collection of text processing utilities that can be used to encode, flatten, normalize, segment, and transform text. The API is organized into different services, each containing related methods.

- **Encoder:** This namespace provides functions that encode or embed text into different forms.

- **Flattener:** This namespace contains methods designed to simplify or reduce the complexity of the text, such as removing line breaks, whitespace, or special characters.

- **Normalizer:** This namespace provides utilities to standardize and normalize text, such as removing punctuation, handling unicode, or lemmatizing words.

- **Segmenter:** This namespace includes functions that divide text into meaningful segments or units, such as sentences, n-grams or tokens.

- **Transformer:** This namespace contains functions that transform the format or representation of text, such as changing case or converting numbers to words.

- **Utilities:** This namespace provides endpoints for fetching actuator details, retrieving a list of available methods, and executing a comprehensive text processing pipeline.

## Using the API

To use the API, send a HTTP request to the appropriate endpoint with the required parameters. The parameters for each endpoint are defined in the corresponding models.

Example:

```curl
curl -X POST "http://localhost:5000/segmenter/sentences" -H "Content-Type: application/json" -d '{"text": "This is a sample sentence. This is another sentence. How about another sentence."}'
```

This would return the following response:

```
{
  "result": [
    "This is a sample sentence.",
    "This is another sample sentence.",
    "And here is another sentence."
  ]
}
```

## Documentation

Full API documentation can be found at http://localhost:5000/.
