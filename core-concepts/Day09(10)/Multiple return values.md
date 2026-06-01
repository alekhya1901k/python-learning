2.Multiple Return Values
    
    Quick Short Notes (10 Summary Points)
    1. A function can contain multiple return statements.
    2. Only one return statement executes during a function call.
    3. Execution stops immediately after a return statement.
    4. Multiple returns are commonly used with conditions.
    5. Different conditions can produce different outputs.
    6. Multiple returns improve code readability.
    7. Functions can return True or False based on logic.
    8. An empty return exits the function immediately.
    9. Code below a return statement is unreachable.
    10. Conditional returns are frequently used for validation.

# Conditional Return Examples:

# -------------------- Example 1 – Returning True or False --------------------

    # Define a function named can_buy_alcohol
    # It accepts one parameter: age
def can_buy_alcohol(age):

        # Check if age is 18 or above
    if age >= 18:

            # Return True if the condition is satisfied
        return True

    else:

            # Return False if the condition is not satisfied
        return False

    # Call the function with age = 20
    # Store nothing; directly print the returned value
print(can_buy_alcohol(20))

# Output: True

# -------------------- Example 2 – Grade Evaluation --------------------

    # Define a function named get_grade
    # It accepts one parameter: score
def get_grade(score):

        # Check if score is 90 or more
    if score >= 90:

            # Return grade A
        return "A"

        # Check if score is 80 or more
    elif score >= 80:

            # Return grade B
        return "B"

        # If none of the above conditions are true
    else:

            # Return grade C
        return "C"

    # Call the function with score = 85
    # Print the returned grade
print(get_grade(85))

# Output: B

# -------------------- Empty Return Example --------------------

    # Define a function named check_age
    # It accepts one parameter: age
def check_age(age):

        # Check whether age is an integer
    if type(age) != int:

            # Exit the function immediately
            # No value is returned
        return

        # This line executes only if age is an integer
    print("Valid Age")

    # Pass a string instead of an integer
check_age("18")

# Output: No output

    # Explanation:
    # type("18") is str, not int.
    # The condition becomes True.
    # return executes immediately.
    # Function stops before reaching print("Valid Age").


# -------------------- Example of Unreachable Code --------------------

    # Define a function named demo
def demo():

        # Return the string "Hello"
        # Function execution stops here
    return "Hello"

    # This line is unreachable
    # It never executes because return has already ended the function
    print("Python")

    # Call the function and print the returned value
print(demo())

# Output: Hello

    # Explanation:
    # Any code written after a return statement
    # inside the same block is called unreachable code.
    # Python never executes it because the function
    # terminates immediately when return is encountered.

