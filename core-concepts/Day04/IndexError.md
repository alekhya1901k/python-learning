A.IndexError and len()
    
    Quick Short Notes (10 Points)
    1. len() returns total items.
    2. Lists and strings support len().
    3. Index ranges depend on length.
    4. Accessing invalid indexes causes IndexError.
    5. Indexes start from 0.
    6. Last valid index is len(list)-1.
    7. len() helps prevent errors.
    8. Common debugging concept.
    9. Useful in loops.
    10. Essential for safe indexing.

Examples

# Create a list named 'fruits'
# The list contains two elements
fruits = ["Apple", "Banana"]

# len() returns the total number of elements in the list
# Here, the list has 2 items
print(len(fruits))

# Output:
# 2

# Try to access the element at index 5
# Valid indexes for this list are:
# Index 0 → "Apple"
# Index 1 → "Banana"
#
# Since index 5 does not exist,
# Python raises an IndexError
print(fruits[5])  # IndexError

# Output: IndexError: list index out of range


B.Nested Lists (2D Lists)
    
    Quick Short Notes (10 Points)
    1. Nested lists contain lists inside lists.
    2. Also called 2D lists.
    3. Useful for tables and matrices.
    4. Access requires multiple indexes.
    5. Common in data science.
    6. Supports structured data storage.
    7. Can represent rows and columns.
    8. Widely used in games and grids.
    9. Complex data can be grouped easily.
    10. Lists can be nested to many levels.

Examples

# Create a list named 'fruits'
# This list stores fruit names
fruits = ["Apple", "Banana"]

# Create another list named 'veg'
# This list stores vegetable names
veg = ["Carrot", "Tomato"]

# Create a nested list named 'food'
# It contains two lists:
# Index 0 → fruits list
# Index 1 → veg list
food = [fruits, veg]

# Access an element from the nested list
# food[0] → selects the fruits list
# food[0][1] → selects index 1 from the fruits list
# Index 1 in fruits list is "Banana"
print(food[0][1])

# Output: Banana
