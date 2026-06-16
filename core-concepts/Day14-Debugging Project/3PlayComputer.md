3.Play Computer

    10 Quick Summary Points
    1. Playing computer means reading code exactly like Python does.
    2. Check each condition step by step.
    3. Do not assume what the code should do.
    4. Look at the exact comparison operators.
    5. > means greater than.
    6. < means less than.
    7. The original code does not include year 1994.
    8. year < 1994 excludes 1994.
    9. year > 1994 also excludes 1994.
    10. Use <= or >= when boundary values must be included.

# Buggy Code

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fixed Code

year = int(input("What's your year of birth? "))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")


# Example

marks = 50

if marks >= 50:
    print("Pass")
else:
    print("Fail")

Here, 50 is included because we used >=.