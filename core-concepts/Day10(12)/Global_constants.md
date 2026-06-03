4.Global Constants
    
    Quick Short Notes:
    1. Constants are values intended not to change during program execution.
    2. Python does not enforce true constants.
    3. Developers use naming conventions to indicate constants.
    4. Constant names are written in UPPERCASE.
    5. Words are separated using underscores.
    6. Constants are usually declared globally.
    7. Constants improve code readability.
    8. They eliminate repeated hardcoded values.
    9. Constants make maintenance easier.
    10. Examples include PI, MAX_USERS, TAX_RATE, and API_URL.

# -------------------- Constants in Python --------------------

    #Definition:
     A constant is a value that is intended to remain unchanged throughout the program.
     Python does not have true constants.
     By convention, constant names are written in UPPERCASE.
     This tells other programmers: "Do not modify this value."

# -------------------- Example 1 – PI Constant --------------------

    # Create a constant named PI
    # PI stores the mathematical value of π (approximately)
PI = 3.14159

    # Create a variable named radius
radius = 5

    # Calculate the area of a circle
    # Formula:
    # Area = π × r × r
area = PI * radius * radius

    # Print the calculated area
print(area)

# Output: 78.53975

# -------------------- Example 2 – Website URL Constant --------------------

    # Create a constant to store Google's URL
    # URLs usually remain fixed and are good candidates for constants
GOOGLE_URL = "https://www.google.com"

    # Print the constant value
print(GOOGLE_URL)

# Output: https://www.google.com


# -------------------- Why Use Constants? --------------------

 1. Makes code easier to read.

 2. Avoids hardcoding values repeatedly.

 3. Makes maintenance easier.

 4. Reduces accidental changes.

 5. Gives meaningful names to important values.


# -------------------- Another Example --------------------

    # Constant for the number of days in a week
DAYS_IN_WEEK = 7

    # Print the constant
print(DAYS_IN_WEEK)

# Output: 7

# -------------------- Important Note --------------------

Python does not prevent changing constants.

PI = 3.14159

Technically allowed, but not recommended
PI = 3.14

print(PI)

# Output: 3.14

Although Python allows this, constants should normally remain unchanged. Writing them in UPPERCASE is a convention followed by Python developers.


