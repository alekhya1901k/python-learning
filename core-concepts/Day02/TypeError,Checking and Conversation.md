
A. TypeError occurs when an operation is performed on the wrong datatype.
    
    Example
        len(12345) --> Error(TypeError)
        len("12345") --> Correct Code
        len(str(12345)) --> Correct Code
Important Points:
    1. Happens due to incompatible datatypes
    2. Common in string-number combinations
    3. Python is strongly typed
    4, Functions expect specific datatypes
    5. len() works only on sequences
    6. Helps identify coding mistakes.

B. Type Checking: type() function is used to identify the datatype.
    Syntax:
        type(value)
    
    Examples
        print(type("abc")) --> <class 'str'> 
        print(type(123))   --> <class 'int'>
        print(type(3.14))  --> <class 'float'>
        print(type(True))  --> <class 'bool'>

C. Type Conversion: Changing one datatype into another datatype.
            | Function  | Purpose             |
            | --------- | ------------------- |
            | `str()`   | Converts to string  |
            | `int()`   | Converts to integer |
            | `float()` | Converts to float   |
            | `bool()`  | Converts to boolean |
    
    Example 1:
    age = 25
    print("My age is " + str(age))
    o/p --> My age is 25
    Example 2:
    Incorrect Code --> print("Number of letters in your name: " + len(input("Enter your name")))
    Correct Code --> print("Number of letters in your name: " + str(len(input("Enter your name: "))))
    Why? --> Because len() returns an integer and strings can only concatenate with strings.

