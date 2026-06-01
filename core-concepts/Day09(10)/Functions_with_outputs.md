1.Functions with Different Outputs
    
    Quick Short Notes:
    1. Functions can accept inputs, perform operations, and return outputs.
    2. The return keyword sends a value back from the function.
    3. Returned values can be stored in variables.
    4. A function can return strings, numbers, lists, dictionaries, or Boolean values.
    5. return ends the function execution immediately.
    6. Functions with outputs are more reusable than functions that only print values.
    7. Returned values can be used in further calculations.
    8. A function can modify input data before returning the result.
    9. print() displays data, while return provides data for later use.
    10. Functions with outputs improve modularity and reduce code duplication.
# Syntax
def function_name(input_parameter):
    # Function body
    return output

# -------------------- Example 1 – Returning a Name --------------------

    # Define a function named format_name
    # It accepts two parameters:
    # f_name = first name
    # l_name = last name
def format_name(f_name, l_name):

        # Convert the first name into Title Case
        # Example: "john" becomes "John"
    first = f_name.title()

        # Convert the last name into Title Case
        # Example: "doe" becomes "Doe"
    last = l_name.title()

        # Return the formatted full name
        # The function sends this value back to the caller
    return f"{first} {last}"

    # Call the function and store the returned value
    # "john" is assigned to f_name
    # "doe" is assigned to l_name
result = format_name("john", "doe")

    # Print the returned value stored in result
print(result)

# Output: John Doe


# -------------------- Example 2 – Returning a Calculation --------------------

    # Define a function named add
    # It accepts two parameters: a and b
def add(a, b):

        # Return the sum of a and b
    return a + b

    # Call the function with arguments 10 and 20
    # Store the returned value in sum_value
sum_value = add(10, 20)

    # Print the returned result
print(sum_value)

# Output: 30

# -------------------- Print vs Return --------------------

# Example 1: Using print()

    # Define a function named greet
def greet():

        # Display "Hello" directly on the screen
    print("Hello")

    # Call the function
greet()

# Output: Hello

    # Explanation:
    # print() only displays the value.
    # The value cannot be stored for later use.

# Example 2: Using return()

    # Define a function named greet
def greet():

        # Return the string "Hello"
        # The value is sent back to the caller
    return "Hello"

    # Store the returned value in a variable
message = greet()

    # Print the stored value
print(message)

# Output: Hello

        # Explanation:
        # return sends a value back from the function.
        # The returned value can be:
        # - Stored in variables
        # - Reused later
        # - Modified
        # - Passed to other functions

