--> Python has 4 commonly used primitive data types:

    String (str)
    Integer (int)
    Float (float)
    Boolean (bool)

A. Strings (str): A String is a sequence of characters written inside quotes.
        name = "Alekhya"
        city = 'Dallas'
    Important Points:
    1. Written inside single ' ' or double " " quotes and are Used to store text data
    2. Strings are immutable (cannot be changed directly)
    3. Supports indexing and slicing
    4. Can contain letters, numbers, and symbols
    5. Multi-line strings use triple quotes ''' ''' or """ """
    6. Concatenation uses +
    7. Repetition uses *
    8. Length can be found using len()
    9. Common functions: upper(), lower(), replace()

B. Integers (int): Integers are whole numbers without decimal points.
        age = 25
        marks=100
    1. Important Points:
    2. Can be positive or negative
    3. No decimal values
    4. Unlimited size in Python
    5. Supports arithmetic operations
    6. Used for counting values
    7. Can be converted using int()
    8. Floor division // returns integer

C. Floats (float): Floats are decimal numbers.
        price = 99.99
        pi = 3.14
    1. Important Points:
    2. Contains decimal points
    3. Used for precise calculations
    4. Supports arithmetic operations
    5. Can store scientific notation
    6. Division / returns float
    7. Can be rounded using round()
    8. Can be converted using float()
    9. Floating-point precision may vary
    10. Useful in mathematical calculations

D. Booleans (bool): Boolean data types represent only two values: True or False.
        is_logged_in = True
        is_admin = False
    Important Points:
    1. Only two values: True and False
    2. Used in conditions and decisions
    3. Important in loops and if-statements
    4. Case-sensitive (True, not true)
    5. Derived from comparisons
    6. Supports logical operations
    7. 0 acts like False
    8. Non-zero values act like True
    9. Widely used in validations


    Quick Summary Points:
    1. Python supports multiple primitive data types.
    2. Strings store text values.
    3. Integers store whole numbers.
    4. Floats store decimal values.
    5. Booleans store True or False.
    6. type() checks the datatype.
    7. str(), int(), and float() convert datatypes.
    8. Strings must be inside quotes.
    9. Arithmetic operations work on numbers.
    10. Correct datatype usage avoids errors.

Example Program:

        name = "Alekhya"
        age = 25
        height = 5.6
        is_student = True

        print(name)
        print(age)
        print(height)
        print(is_student)