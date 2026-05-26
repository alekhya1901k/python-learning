1.Functions
    
    Quick Short Notes (10 Summary Points)
    1. A function is a reusable block of code that performs a specific task.
    2. Functions help avoid writing the same code repeatedly.
    3. Functions improve code readability and organization.
    4. Functions are created using the def keyword.
    5. Every function should have a meaningful name.
    6. Code inside a function must be properly indented.
    7. A function runs only when it is called.
    8. Calling a function means executing the code inside it.
    9. Functions can contain multiple statements.
    10. Functions help break large programs into smaller manageable parts.

Syntax of a Function:
        def function_name():
            # code block

Example: Defining a Function:
        def greet():
            print("Hello")

    Explanation:
    
    def → keyword used to create a function
    greet → function name
    () → parentheses required for functions
    : → starts the function block
    Indented code belongs to the function
    Calling a Function
    greet()
    Output
    Hello

Example 1: Simple Function
        
        def say_hello():
            print("Hello World")

        say_hello()
# Output
Hello World

Example 2: User Input Function

def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)

print("Welcome")
get_user_name()

# Output
Welcome
What is your name? Alekhya
Hello, Alekhya


# How Functions Work Internally:
    
    Step-by-Step Flow
Python reads the function definition.
Function code gets stored in memory.
Function does NOT execute immediately.
Function waits until it is called.
When called, Python executes the function block line by line.

    Important Points About Functions
1. Functions Reduce Repetition

# Without Function:

print("Hello")
print("Hello")
print("Hello")

# With Function:

def greet():
    print("Hello")

greet()
greet()
greet()

2. Functions Improve Readability

# Bad Practice:

print("Calculating...")
# many lines
# many lines

# Better Practice:

def calculate_bill():
    print("Calculating...")

3. Functions Help in Debugging

If an issue occurs, you can debug only that function instead of the whole program.

4. Function Names Should Be Meaningful

# Good:

def calculate_total():

# Bad:

def abc():

5. Function Code Runs Only When Called

def test():
    print("Running")

print("Start")
# Output

Start

Because the function was never called.

