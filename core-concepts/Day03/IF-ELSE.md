If-Else :

A. Condition Check
    
Syntax:

if condition:
    # code
else:
    # code
    
    Quick Short Notes
    
    1. if statement checks whether a condition is True or False.
    2. Code inside if runs only when the condition is True.
    3. Conditions usually return Boolean values (True or False).
    4. Python uses : after conditions.
    5. Indentation decides which code belongs inside the condition.
    6. else runs when the if condition becomes False.
    7. if-else helps programs make decisions.
    8. Comparison operators are commonly used in conditions.
    9. Multiple conditions can be checked using logical operators.
    10. Conditionals are widely used in login systems, validations, and automation.

Example 1
    age = 18
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible")

Example 2
        temperature = 35
    if temperature > 30:
        print("Hot weather")
    else:
        print("Cool weather")

B. Python Indentation

    Quick Short Notes
    
    1. Python uses indentation instead of {} braces.
    2. Indentation means spaces before a line of code.
    3. Usually 4 spaces are used as standard indentation.
    4. Incorrect indentation causes IndentationError.
    5. Child statements must be indented under parent statements.
    6. Indentation improves readability.
    7. All lines in the same block must have equal indentation.
    8. Nested blocks require additional indentation.
    9. Tabs and spaces should not be mixed.
    10. Python strictly enforces indentation rules.

Example:
name = "Alex"

if name == "Alex":
    print("Welcome")
    print("Login successful")

    o/p: Welcome
         Login successful

C. Comparator Operators
    
    Quick Short Notes
    
    1. Comparator operators compare two values.
    2. Result is always True or False.
    3. > means greater than.
    4. < means less than.
    5. >= means greater than or equal to.
    6. <= means less than or equal to.
    7. == checks equality.
    8. != checks inequality.
    9. Comparators are mainly used inside conditions.
    10. Comparisons are essential in filtering and validations.

Example 1
print(10 > 5) --> o/p: True
Example 2
print(7 != 3)--> o/p: True