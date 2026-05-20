Modulo Operator (%) --> Quick Short Notes 
    
    1. % is called the modulo operator.
    2. It returns the remainder after division.
    3. Useful for odd/even checking.
    4. Commonly used in validations.
    5. 10 % 2 gives 0.
    6. 10 % 3 gives 1.
    7. If remainder is 0, number divides completely.
    8. Used in cyclic operations.
    9. Helpful in pattern programs.

Example 1
print(10 % 3) ---> o/p : 1

Example 2 – Odd or Even
number = int(input("Enter number: ")) #Takes input from user for example : 8
if number % 2 == 0:                   # 8 % 2 -->Remainder=0
    print("Even")                     # prints Even in output
else:
    print("Odd")