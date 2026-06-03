3.Global Variables
    
    Quick Short Notes:
    1. Global variables are declared outside functions.
    2. They can be read inside functions without special keywords.
    3. Modifying a global variable inside a function requires the global keyword.
    4. Without global, Python treats the variable as local.
    5. Using many global variables is generally discouraged.
    6. Global variables can make debugging harder.
    7. They are useful for shared configuration values.
    8. The global keyword explicitly refers to a global variable.
    9. Changes made using global affect the original variable.
    10. Global variables remain available until program execution ends.

# -------------------- Example 1 – Reading a Global Variable --------------------

    # Create a global variable named 'count'
    # It is accessible throughout the program
count = 10

    # Define a function named show
def show():

    # Read and print the global variable
    # No 'global' keyword is needed when only reading
    print(count)

    # Call the function
show()

# Output: 10

# -------------------- Example 2 – Modifying a Global Variable --------------------

    # Create a global variable named 'count'
count = 10

    # Define a function named update
def update():

    # Tell Python that we want to use
    # and modify the global variable 'count'
    global count

    # Increase the global variable by 1
    # Same as:
    # count = count + 1
    count += 1

# Call the function
update()

    # Print the updated global variable
print(count)

# Output:   11




# -------------------- Why global is Needed --------------------

    # Without the global keyword:

count = 10

def update():

    # Python treats count as a local variable
    # because it is being modified
    count += 1

    # Calling update() would cause:
    # UnboundLocalError:
    # local variable 'count' referenced before assignment

# Explanation:
    # Python sees count += 1 as:

    # count = count + 1

    # It tries to create a local variable named count,
    # but before creating it, Python needs to read its value.
    # Since the local variable does not yet exist,
    # an error occurs.

# -------------------- Reading vs Modifying --------------------

 Reading a Global Variable:
    # count = 10
    # def show():
    #     print(count)

    # No global keyword required.

 Modifying a Global Variable:
    # count = 10
def update():
     global count
     count += 1

    # global keyword is required.

# -------------------- Another Example --------------------

    # Global variable
name = "Alex"

    # Function modifies the global variable
def change_name():

    # Access the global variable
    global name

    # Update its value
    name = "John"

    # Call the function
change_name()

    # Print the updated value
print(name)

# Output: John