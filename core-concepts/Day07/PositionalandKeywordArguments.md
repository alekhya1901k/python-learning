2. Positional and Keyword Arguments

# Multiple Inputs
    Functions can accept multiple parameters separated by commas.
Syntax
def function_name(parameter1, parameter2):
    # code

# -------------------- Example 1 – Multiple Inputs --------------------

# Define a function named greet_with
# This function has two parameters:
# 1. name
# 2. location
# Parameters receive values from the function call
def greet_with(name, location):
    # Print a greeting message using the value of 'name'
    print(f"Hello {name}")
    # Print a sentence using the value of 'location'
    print(f"What is it like in {location}?")
    
    # Call the function with two arguments
    # "Angela" is assigned to name
    # "Texas" is assigned to location
greet_with("Angela", "Texas")

# Output:
# Hello Angela
# What is it like in Texas?

# Positional Arguments:
By default, Python assigns arguments based on their position.

# -------------------- Example --------------------

# Define a function named my_function
# This function has two parameters:
# a and b
# Parameters receive values from the function call
def my_function(a, b):

    # Print the value stored in parameter 'a'
    print(a)

    # Print the value stored in parameter 'b'
    print(b)

# Call the function with two arguments:
# 2 is assigned to 'a'
# 1 is assigned to 'b'
my_function(2, 1)

# Output:
# 2
# 1


# Important Rule

1. Order matters in positional arguments.

Wrong Order Example
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Texas", "Angela")
Output
Hello Texas
What is it like in Angela?

This happens because arguments are assigned by position.

# Keyword Arguments
1. Keyword arguments assign values using parameter names.

2. This removes confusion about argument order.

# -------------------- Keyword Arguments Example --------------------

# Define a function with two parameters:
# 1. name
# 2. location
def greet_with(name, location):

    # Print greeting message using the value of 'name'
    print(f"Hello {name}")

    # Print location message using the value of 'location'
    print(f"What is it like in {location}?")

# Call the function using keyword arguments
# Here, values are assigned using parameter names
# So order does not matter
greet_with(location="Texas", name="Angela")

# Output:
# Hello Angela
# What is it like in Texas?




# -------------------- Positional vs Keyword Arguments --------------------

# Positional Arguments:
# Values are assigned based on their position/order

# Example:
# greet_with("Angela", "Texas")
#
# name = "Angela"
# location = "Texas"



# Keyword Arguments:
# Values are assigned using parameter names

# Example:
# greet_with(location="Texas", name="Angela")
#
# location = "Texas"
# name = "Angela"



# -------------------- Comparison Table --------------------

# Feature              Positional Arguments      Keyword Arguments
# -------------------------------------------------------------------
# Assignment           By order                  By parameter name
#
# Order Important?     Yes                       No
#
# Readability          Moderate                  High
#
# Common Usage         Simple functions          Large functions
