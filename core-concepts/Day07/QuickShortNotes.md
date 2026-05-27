# Quick Short Notes
    1.Functions can take multiple inputs.
    Multiple parameters are separated using commas.
    Positional arguments assign values based on order.
    Incorrect order can produce wrong output.
    Keyword arguments assign values using parameter names.
    Keyword arguments improve readability.
    Keyword arguments reduce confusion in large functions.
    Positional arguments are shorter to write.
    Functions become flexible with multiple inputs.
    Mixing positional and keyword arguments is allowed carefully.

# -------------------- Example – Mixing Arguments --------------------

# Define a function named student
# This function has two parameters:
# 1. name
# 2. grade
def student(name, grade):

    # Print the value stored in 'name'
    print(name)

    # Print the value stored in 'grade'
    print(grade)

# Call the function using:
# - one positional argument
# - one keyword argument
#
# "Alex" is assigned to 'name' by position
# grade="A" is assigned using the parameter name
student("Alex", grade="A")

# Output:
# Alex
# A



# Explanation:
Python allows mixing positional and keyword arguments.

# Rules:
 1. Positional arguments must come first.
 2. Keyword arguments must come after positional arguments.

# Correct:
student("Alex", grade="A")

# Incorrect:
student(name="Alex", "A")   # Causes SyntaxError

