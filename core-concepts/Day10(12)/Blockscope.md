2.Block Scope:
    
    Quick Short Notes (10 Summary Points)
    1. Python does not have block scope like Java, C++, or JavaScript.
    2. Variables created inside loops remain accessible after the loop ends.
    3. Variables created inside if statements remain available outside the if block.
    4. Variables inside for loops are not destroyed after loop execution.
    5. Variables inside while loops also remain available.
    6. Python uses indentation for code blocks but not for variable scope.
    7. Functions create scope boundaries.
    8. Loops do not create separate namespaces.
    9. Understanding block scope helps avoid accidental variable overwrites.
    10. Most variable scoping in Python happens at the function level.

# -------------------- Block Scope in Python --------------------

# Definition:
    # Python does NOT have block scope for:
    # - for loops
    # - if statements
    # - while loops
    #
    # Variables created inside these blocks
    # remain accessible outside the block.
    #
    # They belong to the surrounding scope
    # (usually the global scope if not inside a function).

# -------------------- Example 1 – For Loop --------------------

    # Start a loop that runs 5 times
    # i will take values: 0, 1, 2, 3, 4
for i in range(5):

        # Create a variable inside the loop
        # The value gets assigned during each iteration
    message = "Python"

    # Print the variable outside the loop
    # This works because Python does not create
    # a separate scope for the for loop
print(message)

# Output: Python

# -------------------- Example 2 – If Statement --------------------

    # Check a condition
if True:

        # Create a variable inside the if block
    age = 18

    # Print the variable outside the if block
    # This works because variables created inside
    # an if statement remain accessible afterwards
print(age)

# Output: 18

# -------------------- Why Does This Work? --------------------

# In some programming languages:

 if (true) {
     int age = 18;
 }

 print(age);  ← Error

    # because those languages have block scope.
    # Python is different.
    # Variables created inside loops and if statements
    # are still available outside the block.



# -------------------- Another Example --------------------

    # Create a variable inside a while loop
count = 0

while count < 1:

    city = "Dallas"

    count += 1

    # city is still available here
print(city)

# Output: Dallas

# -------------------- Important Note --------------------

    # Python does have:
    # ✔ Function Scope
    # ✔ Global Scope
    #
    # Python does NOT have:
    # ✘ Block Scope for if, for, and while blocks

# Example:
    #
    # if True:
    #     name = "Alex"
    #
    # print(name)
    #
    # Output: Alex