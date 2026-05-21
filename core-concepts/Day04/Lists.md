Lists 

    Quick Short Notes (10 Points)
    1. Lists store multiple values.
    2. Lists are ordered collections.
    3. Lists are mutable.
    4. Items are separated using commas.
    5. Lists use square brackets [].
    6. Lists can store mixed data types.
    7. Duplicate values are allowed.
    8. Lists support indexing.
    9. Lists are widely used in data handling.
    10. Lists are dynamic in size.

Examples

# Create a list named 'fruits'
# Lists are used to store multiple values in a single variable
# Each value in the list is separated by a comma
fruits = ["Apple", "Mango", "Banana"]

# 'fruits' list contains 3 string elements:
# Index 0 → "Apple"
# Index 1 → "Mango"
# Index 2 → "Banana"



# Create another list named 'numbers'
# This list stores integer values
numbers = [1, 2, 3, 4]

# 'numbers' list contains 4 integer elements:
# Index 0 → 1
# Index 1 → 2
# Index 2 → 3
# Index 3 → 4

# Outputs:

print(fruits)
# Output: ['Apple', 'Mango', 'Banana']

print(numbers)

# Output: [1, 2, 3, 4]


B. Negative Indices
    
    Quick Short Notes (10 Points)
    1. Negative indexing accesses elements from the end.
    2. -1 means last item.
    3. -2 means second last item.
    4. Useful when list size is unknown.
    5. Makes reverse access easier.
    6. Works on strings and tuples too.
    7. Reduces need for len().
    8. Simplifies last-element retrieval.
    9. Common in stack operations.
    10. Helps in reverse traversal logic.

Examples

# Create a list named 'fruits'
# The list contains 3 string elements
fruits = ["Apple", "Banana", "Cherry"]

# Access the last element of the list using negative indexing
# -1 means the last item in the list
print(fruits[-1])

# Output: Cherry


# Access the second last element of the list
# -2 means the item before the last item
print(fruits[-2])

# Output: Banana


C. Modifying Items in Lists
    
    Quick Short Notes 
    1. Lists are mutable.
    2. Existing items can be changed.
    3. Use index assignment to modify values.
    4. Only valid indexes can be modified.
    5. Modifications happen in-place.
    6. No new list is created.
    7. Useful for updates and corrections.
    8. Frequently used in applications.
    9. Changes affect the original list.
    10. Strings cannot be modified like lists.

Example:

# Create a list named 'fruits'
# The list contains two string elements
fruits = ["Apple", "Banana"]

# Change the value at index 0
# Index 0 refers to the first element in the list
# "Apple" is replaced with "Orange"
fruits[0] = "Orange"

# Print the updated list
print(fruits)

# Output: ['Orange', 'Banana']


# Create a list named 'numbers'
# This list contains integer values
numbers = [1, 2, 3]

# Change the value at index 1
# Index 1 refers to the second element
# Value 2 is replaced with 20
numbers[1] = 20

# Print the updated list
print(numbers)

# Output: [1, 20, 3]

D. Adding Items Using append()
    
    Quick Short Notes (10 Points)
    1. append() adds items at the end.
    2. It modifies the original list.
    3. Only one item is added at a time.
    4. Syntax: list.append(item)
    5. Commonly used in loops.
    6. Useful for dynamic data collection.
    7. Order is preserved.
    8. Works with any data type.
    9. Returns None.
    10. Frequently used in real-time applications.

Examples:

# Create a list named 'fruits'
# Initially, the list contains one item
fruits = ["Apple"]

# Add a new item "Mango" to the end of the list
# append() adds a single element at the end
fruits.append("Mango")

# Print the updated fruits list
print(fruits)

# Output: ['Apple', 'Mango']

# Create an empty list named 'numbers'
# Empty lists are created using []
numbers = []

# Add the number 10 to the empty list
numbers.append(10)

# Print the updated numbers list
print(numbers)

# Output: [10]
