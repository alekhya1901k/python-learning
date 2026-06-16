6.Use a Debugger
    
    10 Quick Summary Points
    1. A debugger helps pause code during execution.
    2. Breakpoints are used to stop code at a specific line.
    3. Step Over runs one line at a time.
    4. Step Into enters functions or modules.
    5. Step Into My Code enters only your own code.
    6. Debuggers show live variable values.
    7. They are better than too many print statements.
    8. The bug here is indentation.
    9. b_list.append(new_item) is outside the loop.
    10. It should be inside the loop to store every changed item.

# Buggy Code
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Fixed Code

import random
import maths


def mutate(a_list):
    b_list = []

    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)

    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Simple Version Without maths.py

import random


def mutate(a_list):
    b_list = []

    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = new_item + item
        b_list.append(new_item)

    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

