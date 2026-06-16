4.Fix the Errors

    10 Quick Summary Points
    1. Syntax errors must be fixed before running code.
    2. Indentation is very important in Python.
    3. Code inside an if block must be indented.
    4. Strings with variables need an f-string.
    5. "{age}" prints text literally.
    6. f"{age}" inserts the variable value.
    7. Editor red lines usually show serious errors.
    8. Yellow warnings may not stop the program but should be reviewed.
    9. try/except helps prevent crashes.
    10. Always fix visible errors first.

# Buggy Code
 age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")

# Fixed Code
age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")
Safer Version Using try/except
try:
    age = int(input("How old are you? "))
    if age > 18:
        print(f"You can drive at age {age}.")
except ValueError:
    print("Please enter a valid number.")