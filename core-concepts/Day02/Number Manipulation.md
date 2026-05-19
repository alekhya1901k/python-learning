A. Flooring a Number: Removing decimal places using int().
    
    Example
        print(int(3.738492)) --> 3

    Important Note: It does NOT round the number.

B. Rounding a Number: Rounds a number to nearest value.

    Examples
    print(round(3.738492)) --> 4
    print(round(3.14159, 2)) --> 3.14

C. Assignment Operators
    | Operator | Meaning             |
    | -------- | ------------------- |
    | `+=`     | Add and assign      |
    | `-=`     | Subtract and assign |
    | `*=`     | Multiply and assign |
    | `/=`     | Divide and assign   |

    Example :
    score = 10
    score += 5
    print(score) --> 15

D. f-Strings: Used to insert variables directly into strings. Introduced in Python 3.6.
        How f-Strings Work: Python looks inside the { } brackets and replaces the variable or expression with its value.
        
        Example
        age = 12
        print(f"I am {age} years old")
        Output:
        I am 12 years old

    Advantages:
        1. Easy to read.
        2. Faster formatting3.
        3. Cleaner syntax.
        4. Supports expressions directly.