A. Basic Operators:
    | Operator | Meaning        | Example  |
    | -------- | -------------- | -------- |
    | `+`      | Addition       | `5 + 2`  |
    | `-`      | Subtraction    | `5 - 2`  |
    | `*`      | Multiplication | `5 * 2`  |
    | `/`      | Division       | `5 / 2`  |
    | `//`     | Floor Division | `5 // 2` |
    | `**`     | Exponent       | `5 ** 2` |

    Examples: 
    print(10 + 5) --> 15
    print(10 - 5) --> 5
    print(10 * 5) --> 50
    print(10 / 5) --> 2.0 (Division always returns float type)
    print(10 // 3) --> 3 (Floor Division always returns int type)
    print(2 ** 3) --> 8

B. PEMDAS Rule: Order of operation execution.
    PEMDAS Full Form
        P → Parentheses
        E → Exponents
        M → Multiplication
        D → Division
        A → Addition
        S → Subtraction

    Example:
        print(3 * 3 + 3 / 3 - 3) --> 7.0
        Step by step:
        = 9 + 1 - 3
        = 10 - 3
        = 7.0
