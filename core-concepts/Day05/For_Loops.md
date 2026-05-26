1.For Loops
    
    Quick Short Notes (10 Points)
    1. A for loop is used to repeat a block of code multiple times.
    2. It helps avoid writing repetitive code.
    3. Loops can iterate through lists, strings, tuples, ranges, etc.
    4. The loop variable stores one item at a time from the sequence.
    5. Syntax always ends with a colon :.
    6. Indentation defines which code belongs to the loop.
    7. The loop continues until all items are processed.
    8. Python automatically moves to the next item in each iteration.
    9. Nested loops are possible (loop inside another loop).
    10. for loops are commonly used for data processing, automation, and validations.

# Syntax
for variable in sequence:
    # code block


# -------------------- Example 1 --------------------

# Create a list containing fruit names
fruits = ["Apple", "Peach", "Pear"]

# Start a for loop
# The loop picks one item at a time from the list
# and stores it in the variable 'fruit'
for fruit in fruits:

    # Print the current fruit value
    print(fruit)

# Output:
# Apple
# Peach
# Pear




# -------------------- Example 2 --------------------

# Create a list of fruits
fruits = ["Apple", "Peach", "Pear"]

# Loop through each fruit in the list
for fruit in fruits:

    # Add the word " pie" to each fruit name
    # String concatenation is used here
    print(fruit + " pie")

# Output:
# Apple pie
# Peach pie
# Pear pie




# -------------------- Be a Computer — Prediction --------------------

# Create a fruits list
fruits = ["Apple", "Peach", "Pear"]

# Loop through each fruit one by one
for fruit in fruits:

    # Print the fruit name
    print(fruit)

    # Print the fruit name with " pie"
    print(fruit + " pie")

# Output:
# Apple
# Apple pie
# Peach
# Peach pie
# Pear
# Pear pie




# -------------------- Indentation Importance - Example 1 --------------------

# Create a fruits list
fruits = ["Apple", "Peach", "Pear"]

# Start loop
for fruit in fruits:

    # This line is inside the loop
    # It runs for every fruit
    print(fruit)

    # This line is also inside the loop
    # Because it has the same indentation
    print("Hello")

# Output:
# Apple
# Hello
# Peach
# Hello
# Pear
# Hello




# -------------------- Indentation Importance - Example 2 --------------------

# Create a fruits list
fruits = ["Apple", "Peach", "Pear"]

# Start loop
for fruit in fruits:

    # This line is inside the loop
    print(fruit)

# This line is outside the loop
# Because it is not indented
# It runs only once after the loop finishes
print("Hello")

# Output:
# Apple
# Peach
# Pear
# Hello
```

