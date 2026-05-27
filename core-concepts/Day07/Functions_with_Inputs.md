1.Functions with Inputs:
    
    Quick Short Notes
    1. A function is a reusable block of code that performs a specific task.
    2. Functions help reduce repeated code and improve readability.
    3. Inputs allow functions to work with different values each time they are called.
    4. Inputs are written inside parentheses during function definition.
    5. The variable inside the function definition is called a parameter.
    6. The actual value passed during the function call is called an argument.
    7. Functions with inputs make programs dynamic and flexible.
    8. Parameters behave like normal variables inside the function.
    9. A function can accept one or more inputs.
    10. Inputs can be strings, integers, floats, lists, or any data type.
# Syntax
        def function_name(parameter):
            # code


# -------------------- Example 1 – Simple Function with Input --------------------

# Define a function named greet
# 'name' is a parameter
# Parameters receive values when the function is called
def greet(name):

    # Print a greeting message using the value stored in 'name'
    # f-string allows variable insertion inside a string
print(f"Hello {name}")

# Call the function and pass "Angela" as an argument
greet("Angela")

# Output: Hello Angela


# -------------------- Example 2 – Function with Number Input --------------------

# Define a function named square
# 'number' is the parameter
def square(number):

    # Multiply the number by itself
    # This calculates the square value
print(number * number)

# Call the function with argument 5
square(5)

# Output: 25


# -------------------- Understanding Parameters vs Arguments --------------------

Parameter:
1. A variable written in the function definition
2. It receives the value sent to the function

# Example:
def greet(name):
          ----
         parameter


Argument:
1. The actual value passed during the function call

# Example:
greet("Angela")
      --------
      argument


Quick Comparison Table

 Term        Meaning                              Example
 ----------------------------------------------------------------
 Parameter   Variable in function definition      name
 Argument    Actual value passed to function      "Angela"


Example:

def greet(name):   # name = parameter
    print(name)

greet("Angela")    # Angela = argument

# Step-by-Step Flow:
def greet(name):
    print(f"Hello {name}")

greet("Tom")

# Flow:
1. Function greet() is created.
2. name becomes the parameter.
3. Function is called with "Tom".
4. "Tom" is assigned to name.
5. Print statement executes.
6. Output becomes Hello Tom.

# Important Points:
1. Function definition uses def.
2. Parentheses hold parameters.
3. Function call sends arguments.
4. Parameters receive the arguments.
5. Functions only run when called.
