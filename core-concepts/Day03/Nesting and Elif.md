Nesting and Elif ---> Quick Short Notes 

    1. Nesting means placing one if inside another.
    2. Nested conditions allow detailed checking.
    3. Inner condition executes only if outer condition is true.
    4. elif means “else if”.
    5. elif checks multiple conditions efficiently.
    6. elif avoids deep nesting.
    7. Multiple elif blocks can be used.
    8. else acts as default block.
    9. Nested conditions improve decision making.
    10. Commonly used in grading systems and validations.

Example 1 – Nested If

maths_score = 95
english_score = 92

if maths_score >= 90:
    if english_score >= 90:
        print("Good at everything")
o/p --> Good at everything

Example 2 – Elif

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

o/p --> Grade B

