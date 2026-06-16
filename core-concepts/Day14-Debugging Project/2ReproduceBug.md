2.Reproduce the Bug

    10 Quick Summary Points
    1. Some bugs happen only sometimes.
    2. Random bugs are harder to find.
    3. To debug, we should reproduce the bug reliably.
    4. randint(1, 6) gives numbers from 1 to 6.
    5. List indexes start from 0.
    6. dice_images has indexes 0 to 5.
    7. If dice_num becomes 6, dice_images[6] causes an error.
    8. The error is IndexError.
    9. Fix by using randint(0, 5).
    10. Always match random number range with valid list indexes.


# Buggy Code

from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# Fixed Code

from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]

dice_num = randint(0, 5)

print(dice_images[dice_num])

# Example

fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

Valid indexes are: 0, 1, 2 but Not 3.