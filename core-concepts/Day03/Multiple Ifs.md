Multiple If Statements --> Quick Short Notes
        
    1. Multiple if statements are independent.
    2. Every condition gets checked.
    3. One condition does not affect another.
    4. Multiple blocks may execute together.
    5. Useful for unrelated conditions.
    6. Different from if-elif-else.
    7. if-elif-else stops after first true condition.
    8. Multiple if improves flexibility.
    9. Common in validations.
    10. Easier to debug independent conditions.

Example 1:

age = 20

if age > 18:
    print("Adult")

if age > 15:
    print("Teenager")
o/p --> Adult

Example 2: 

marks = 95

if marks >= 90:
    print("Excellent")

if marks >= 80:
    print("Very Good")

o/p --> Excellent
