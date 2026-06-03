Namespaces and Scope
    
    Quick Short Notes:
    1. A namespace is a container that stores names (variables, functions, classes) and their corresponding values.
    2. Scope determines where a variable can be accessed in a program.
    3. Python searches variables using the LEGB rule:
        Local
        Enclosing
        Global
        Built-in
    4. Variables created inside a function belong to the Local Scope.
    5. Local variables are accessible only within the function where they are created.
    6. Variables declared outside all functions belong to the Global Scope.
    7. Global variables can be accessed anywhere in the same Python file.
    8. If a local and global variable have the same name, the local variable takes precedence inside the function.
    9. Functions themselves also belong to a namespace.
    10. Proper use of scope helps prevent naming conflicts and improves code readability.

# A. -------------------- Local Scope --------------------

    # Definition:
    # Variables created inside a function have local scope.
    # They exist only while the function is running.
    # They cannot be accessed outside the function.


# -------------------- Example 1 --------------------

    # Define a function named greet
def greet():

    # Create a local variable named 'name'
    # This variable exists only inside greet()
    name = "Alex"

    # Print the value of the local variable
    print(name)

    # Call the function
    # The code inside the function executes
greet()

    # Output: Alex

# -------------------- Example 2 --------------------

    # Define a function named test
def test():

    # Create a local variable named 'age'
    # This variable is available only inside test()
    age = 25

    # Try to print age outside the function
print(age)

    # Output: NameError: name 'age' is not defined

# Explanation:
    # The variable 'age' was created inside test().
    # It belongs only to the local scope of test().
    # Since it does not exist outside the function,
    # Python raises a NameError.

# -------------------- Visual Representation --------------------

# def test():
#     age = 25     ← Local Scope
#
# print(age)      ← Outside Function (Cannot Access)

# Scope Boundary:
#
# Function Start
#      ↓
#   age = 25
#      ↓
# Function End
#
# After the function ends,
# the local variable is no longer accessible.


# -------------------- Correct Way --------------------

    # Define a function
def test():

    # Local variable
    age = 25

    # Print inside the function
    print(age)

    # Call the function
test()

    # Output: 25

# Explanation:
    # Since age is used inside its own function,
    # it can be accessed successfully.

# B. -------------------- Global Scope --------------------

    # Definition:
    # Variables created outside all functions have global scope.
    # Global variables can be accessed from anywhere in the program,
    # including inside functions and outside functions.

# -------------------- Example 1 --------------------

    # Create a global variable named 'message'
    # It is defined outside any function
message = "Hello"

    # Define a function named display
def display():

    # Access and print the global variable
    # Python can find 'message' because it is in global scope
    print(message)

    # Call the function
display()

# Output: Hello

# -------------------- Example 2 --------------------

    # Create a global variable named 'score'
score = 100

    # Print the global variable directly
    # Since we are outside any function,
    # the variable is accessible here
print(score)

    # Output: 100

# -------------------- Visual Representation --------------------

# message = "Hello"   ← Global Variable
#
# def display():
#     print(message)
#
# display()

# Scope Diagram:
#
# Global Scope
# ├── message = "Hello"
# ├── score = 100
# └── display()
#
# Functions can access global variables
# unless a local variable with the same name exists.

# -------------------- Another Example --------------------

    # Global variable
country = "USA"

    # Function accessing global variable
def show_country():

    # Print the global variable
    print(country)

    # Call the function
show_country()

    # Output: USA

# -------------------- Key Difference --------------------

# Local Variable:
    # Created inside a function.
    # Accessible only inside that function.

# Global Variable:
    # Created outside functions.
    # Accessible throughout the program.

# Example:

    # city = "Dallas"      ← Global Variable

    # def demo():
        name = "Alex"    ← Local Variable

    # city can be used everywhere.
    # name can only be used inside demo().

