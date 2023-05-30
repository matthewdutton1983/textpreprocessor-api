"""
===================================
TextPreProcessing API Documentation
===================================

The TextPreProcessing API includes the following endpoints:

1. `/` [GET]

    This endpoint returns a confirmation message indicating that the server is running.
    
    Response Example:
    {
        "message": "Server is running"
    }

2. `/methods` [GET]

    This endpoint returns a list of available preprocessing methods in the application.
    
    Response Example:
    {
        "available_methods": ["method1", "method2", "method3"]
    }

3. `/<method_name>/info` [GET]

    This endpoint returns the docstring for the specified method.
    
    Request Example:
    `/method1/info`
    
    Response Example:
    {
        "docstring": "This is the docstring for method1."
    }

4. `/<method_name>` [POST]

    This endpoint executes a specified preprocessing function on the input text.

    The function and its parameters are defined in the JSON body of the POST request.

    Request Body format:
    {
        "text": "The input text to be preprocessed",
        "args": {
            // optional arguments for the function
        }
    }

    Response Example:
    {
        "result": "Processed text"
    }

    Note: Replace `<method_name>` with the actual name of the preprocessing function you want to execute. 
    The `args` object should contain the arguments needed for the function in key-value pairs.

5. `/pipeline` [POST]

    This endpoint executes a series of preprocessing steps on the input text.
    
    The steps to be executed, along with their corresponding parameters, 
    are defined in the JSON body of the POST request.
    
    Request Body format:
    {
        "text": "The input text to be preprocessed",
        "steps": ["step1", "step2"],
        "modes": {
            "step1": {
                // optional parameters for step1
            },
            "step2": {
                // optional parameters for step2
            }
        }
    }
    
    Response Example:
    {
        "result": "Processed text"
    }
"""
