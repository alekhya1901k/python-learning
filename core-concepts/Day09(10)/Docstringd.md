3.Docstrings
    
    Quick Short Notes (10 Summary Points)
    1. Docstrings are used to document Python code.
    2. They are written using triple double quotes """ """.
    3. Docstrings can span multiple lines.
    4. They explain the purpose of functions, classes, and modules.
    5. Docstrings improve code readability.
    6. IDEs display docstrings when hovering over functions.
    7. They help other developers understand code quickly.
    8. Good docstrings describe inputs and outputs.
    9. Python stores docstrings in the __doc__ attribute.
    10. Writing docstrings is considered a professional coding practice.

# Syntax:

"""
This is a docstring.
"""
# -------------------- Example 1 – Function Docstring --------------------

    # Define a function named square
def square(num):

        # Docstring:
        # A special string used to describe what the function does
        # It is written immediately below the function definition
        """Returns the square of a number."""

        # Return the square of the given number
    return num * num

    # Call the function with argument 5
    # Store nothing; directly print the returned value
print(square(5))

# Output: 25

# -------------------- Example 2 – Multi-line Docstring --------------------

    # Define a function named add
def add(a, b):

        # Multi-line docstring
        # Used when a longer explanation is needed
        """
        Adds two numbers.
        Returns the sum.
        """

        # Return the addition result
    return a + b

    # Call the function and print the result
print(add(10, 20))

# Output: 30

# -------------------- Accessing a Docstring --------------------

    # Define a function named greet
def greet():

        # Function documentation
    """Displays a greeting message."""

        # Print a greeting message
    print("Hello")

    # Access the docstring using __doc__
    # __doc__ returns the documentation string of the function
print(greet.__doc__)

# Output: Displays a greeting message.

# -------------------- Additional Example --------------------

    # Define a function with a docstring
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

    # Print the function's documentation
print(multiply.__doc__)

# Output: Returns the product of two numbers.


 -------------------- Important Notes --------------------

 1. A docstring documents the purpose of a function.

 2. It is written immediately after the function definition.

 3. Single-line docstrings are used for short descriptions.

 4. Multi-line docstrings are used for detailed explanations.

 5. Docstrings are enclosed within triple quotes:
    """Docstring"""

 6. Docstrings can be accessed using:
    function_name.__doc__

 7. Tools like help() use docstrings to display documentation.