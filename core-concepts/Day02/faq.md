1. What is a String in Python?
    
    A string is a sequence of characters enclosed within single, double, or triple quotes.
        Example: name = "Python"

2. Are Python strings mutable or immutable?
    
    Strings are immutable, meaning they cannot be changed after creation.
        Example:  name = "Python"
        name[0] = "J"  ❌ Error

3. What is the difference between single quotes and double quotes?
    
    There is no functional difference. Both are used to create strings.
        Example: 'a' , "a"

4. What is string concatenation?

    Combining two or more strings using the + operator.
        Example: print("Hello " + "World") --> Hello World

5. What does the len() function do with strings?

    It returns the number of characters in a string.
        Example: print(len("Python")) --> 6

6. What is an integer in Python?
    
    An integer is a whole number without decimal points.
    Example:    x = 100

7. Can integers be negative?

    Yes, integers can be positive, negative, or zero.
        Example: a = -50

8. What datatype is returned by floor division (//)?

    Floor division usually returns an integer.
    Example: print(10 // 3) --> 3

9. What is the difference between int and float?
        | int           | float           |
        | ------------- | --------------- |
        | Whole numbers | Decimal numbers |
        | Example: 5    | Example: 5.5    |

10. How do you convert a string into an integer?

    Using the int() function.
        Example:num = int("25")

11. What is a float in Python?

    A float is a number containing decimal values.
        Example: price = 99.99

12. What is the difference between int() and float()?
        int() removes decimal values
        float() keeps decimal values

13. Why does division return float values in Python?

    Because Python uses true division with /.
        Example: print(10 / 2) --> 5.0

14. How can you round float values?

    Using the round() function.
        Example:round(3.14159, 2) --> 3.14

15. What is floating-point precision issue?
    
    Sometimes decimal calculations are not perfectly accurate due to internal binary representation.
    Example: print(0.1 + 0.2) --> 0.3

16. What are Boolean values in Python?
    
    Boolean values are True and False.

17. Where are Booleans mainly used?
    
    They are mainly used in conditions and decision-making.
        Example:
            if True:
                print("Run")

18. Is True equal to 1 in Python?

    Yes.
        Example: print(True == 1) --> Yes

19. What is the datatype of comparison results?

    Comparison operations return Boolean values.
        Example: print(5 > 2) --> True

20. What are logical operators used with Booleans?
        | Operator | Meaning              |
        | -------- | -------------------- |
        | `and`    | Both conditions true |
        | `or`     | At least one true    |
        | `not`    | Reverse result       |


21. What is TypeError in Python?

    TypeError occurs when incompatible datatypes are used together.

22. Why does "Hello" + 5 produce an error?

    Because Python cannot concatenate string and integer directly.

23. How can TypeError be fixed?

    Using datatype conversion.
        Example: "Hello " + str(5)

24. Why does len(123) give TypeError?
        
    Because len() works only on sequences like strings, lists, etc.

25. Is Python strongly typed?

    Yes. Python strictly checks datatype compatibility.

26. What is the purpose of the type() function?

    It identifies the datatype of a variable or value.

27. What is the output of type(10)?
    <class 'int'>

28. Can type() check user-defined classes?

    Yes.

29. What datatype is returned by input()?

    Always a string (str).

30. Why is type checking important?

    It helps avoid runtime errors and improves debugging.

31. What is type conversion?

    Changing one datatype into another datatype.

32. What is implicit type conversion?

    Automatic datatype conversion by Python.
    Example: 5 + 2.0

33. What is explicit type conversion?

    Manual datatype conversion using functions.
    Example: int("5")

34. Which functions are commonly used for type conversion?
        | Function  | Purpose            |
        | --------- | ------------------ |
        | `int()`   | Convert to integer |
        | `float()` | Convert to float   |
        | `str()`   | Convert to string  |
        | `bool()`  | Convert to boolean |

35. Can all strings be converted to integers?
        No
        Example: int("abc")   # Error


36. What are arithmetic operators in Python?
        | Operator | Meaning        |
        | -------- | -------------- |
        | `+`      | Addition       |
        | `-`      | Subtraction    |
        | `*`      | Multiplication |
        | `/`      | Division       |

37. Difference between / and //?
    a/b --> returns float division
    a//b --> returns floor division

38. What does ** operator do?

    It performs exponentiation.
        Example: 2 ** 3

39. What is modulus operator %?

    It returns the remainder.
        Example: 10 % 3 --> 1

40. Which operator has highest precedence?

    Exponent (**) has higher precedence than multiplication and division.

41. What is PEMDAS?

    PEMDAS: Order of operation execution: Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

42. Why is operator precedence important?

    It determines the correct calculation order.

43. Which executes first: multiplication or addition?

    Multiplication executes first.

44. How can we change execution order?

    Using parentheses ().

45. What is associativity in Python?

    It determines evaluation direction when operators have same precedence.

46. What does int() do to float values?

    It removes decimal places.

47. Does int() round numbers?

    No. It truncates values.

    Example:int(3.9) --> 3

48. Difference between int() and round()?
    | int()            | round()      |
    | ---------------- | ------------ |
    | Removes decimals | Rounds value |

49. What is floor division?  When is flooring useful?

    Division that removes decimal part. Useful in indexing, pagination, and loop calculations.

50. What is the purpose of round()? Can round() round decimal places?

    Rounds numbers to nearest value. Yes, round decimal places.
        Example: round(3.14159, 2) --> 3.14

51. What happens if decimal part is .5?
 
    Python rounds to nearest even number in some cases.

52. What datatype does round() return?

    Usually integer or float depending on arguments.

53. What are assignment operators?

    Operators that update variable values.

54. What does += mean? Why are assignment operators useful?

    Add and assign. They reduce code length.

55. Are assignment operators faster?

    Generally more efficient and readable.

56. What is an f-string? Why are f-strings preferred?

    A formatted string literal. They are readable and faster.


57. Can expressions be used inside f-strings?

    Example: print(f"{5 + 2}") --> 7

58. Difference between .format() and f-strings?
    | `.format()`   | f-strings     |
    | ------------- | ------------- |
    | Older method  | Modern method |
    | Less readable | More readable |
    | Slower        | Faster        |
