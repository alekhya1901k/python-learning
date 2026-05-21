A.Pseudorandom Number Generators (PRNG)
    
    Quick Short Notes
    1. Computers cannot generate truly random numbers naturally.
    2. PRNG stands for Pseudorandom Number Generator.
    3. PRNGs generate numbers using mathematical formulas.
    4. Same starting value (seed) gives the same sequence of numbers.
    5. PRNGs are widely used in games, simulations, and testing.
    6. Python’s random module uses PRNG internally.
    7. Generated values only “appear” random.
    8. PRNGs are fast and efficient for software applications.
    9. PRNGs are not secure for cryptography-related tasks.

    Examples:

# Import the built-in random module
# This module provides functions to generate random numbers
import random

# Generate a random whole number between 1 and 100 (inclusive)
# randint(1, 100) means:
# - minimum possible value = 1
# - maximum possible value = 100
# The generated number changes each time unless a seed is set
print(random.randint(1, 100))

    o/p: 20(Some Randon number)


# Import the built-in random module
# This module provides functions to generate random numbers
import random

# Set a fixed starting point (seed) for the random number generator
# Using the same seed value always produces the same sequence of random numbers
# This is useful for testing, debugging, and reproducible results
random.seed(10)

# Generate a random integer between 1 and 50 (both included)
# randint(start, end) returns a whole number within the given range
# Because the seed is fixed as 10, the generated number will always be 37
print(random.randint(1, 50))

    o/p: 37


B. Random Module

    Quick Short Notes 
    1. Python provides randomness using the random module.
    2. The module must be imported before use.
    3. It contains functions for integers, floats, and selections.
    4.random.randint() generates random integers.
    5. random.random() generates float values.
    6. random.uniform() generates float numbers in a custom range.
    7. Random module is commonly used in games.
    8. It is useful for simulations and testing.
    9. Random values change on every execution.
    10. The module improves program unpredictability.

Examples:

# Import the random module
# This module helps generate random numbers
import random

# Generate a random whole number between 1 and 10
# randint(1, 10) includes both 1 and 10
print(random.randint(1, 10))

# Output: 7

# Import the random module 
import random

# Generate a random decimal number between 0.0 and 1.0
# random() returns a floating-point value
print(random.random())

# Output: 0.4288890546751146

C. Random Whole Numbers Using randint()

    Quick Short Notes
    1. randint() generates random integers.
    2. Syntax: random.randint(a, b)
    3. Both lower and upper bounds are included.
    4. Output is always a whole number.
    5. Commonly used in dice and lottery programs.
    6. Requires importing random.
    7. Range values can be positive or negative.
    8. Useful for decision-making programs.
    9. Each execution may produce different results.

# Import the random module
# This module is used to generate random numbers
import random

# Generate and directly print a random whole number between 1 and 6
# This simulates rolling a dice
# Possible values: 1, 2, 3, 4, 5, or 6
print(random.randint(1, 6))

# Output: 4



# Import the random module again
# (Not necessary if already imported above, but valid)
import random

# Generate a random number between 1 and 6
# Store the generated value inside the variable 'dice'
dice = random.randint(1, 6)

# Print the value stored in the variable
print(dice)

# Output: 2

4.Modules
    
    Quick Short Note
    
    1. Modules help organize Python code.
    2. A module is simply a .py file.
    3. Modules improve code reusability.
    4. They reduce duplicate code.
    5. Python provides built-in modules.
    6. Users can create custom modules.
    7. Modules are imported using import.
    8. Functions and variables can be shared between files.
    9. Modules make projects cleaner and maintainable.
    10. Large applications heavily rely on modular programming.

Examples

# -------------------- File: math_utils.py --------------------

# Define a function named greet
# Functions are reusable blocks of code
def greet():

# Print the word "Hello" when the function is called
    print("Hello")

# Output: Hello


# -------------------- Main File --------------------

# Import the math_utils file/module
# This allows access to functions and variables inside math_utils.py
import math_utils

# Call the greet() function from the math_utils module
# The dot (.) operator is used to access module members
math_utils.greet()

# Output: Hello


5.Random Floats

    Quick Short Notes (10 Points)
    1. Random floats contain decimal values.
    2. random.random() returns values between 0.0 and 1.0.
    3. 1.0 is excluded in random.random().
    4. Multiplication expands the range.
    5. random.uniform(a,b) gives custom float ranges.
    6. uniform() may include the upper limit.
    7. Floats are useful in simulations.
    8. Used in probability-based systems.
    9. Random floats are widely used in AI and gaming.
    10. Precision depends on floating-point representation.

Examples
# Import the random module
# This module is used to generate random values
import random

# Generate a random decimal number between 0.0 and 1.0
# random() returns a floating-point number
# The value can include many decimal places
print(random.random())

# Output: 0.3478215942837124



# Import the random module 
import random

# Generate a random decimal number between 1 and 10
# uniform(start, end) returns a floating-point value
# The number can contain decimal points
print(random.uniform(1, 10))

# Output: 7.42819451290314


