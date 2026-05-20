Logical Operators --> Quick Short Notes 

    1. Logical operators combine conditions.
    2. and requires all conditions to be true.
    3. or requires at least one condition to be true.
    4. not reverses the condition result.
    5. Logical operators return Boolean values.
    6. Used in validations and filtering.
    7. Parentheses improve readability.
    8. Logical operators work with comparison operators.
    9. Frequently used in authentication systems.
    10. Essential for complex decision-making.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses the result                 |

Example 1

age = 50

if age >= 45 and age <= 55:
    print("Ride is free")

o/p --> Ride is free

Example 2

is_logged_in = False

if not is_logged_in:
    print("Please login")

o/p --> Please login
