1. What is the purpose of the return statement?

The return statement sends a value back from a function to the caller.

2. What happens if a function does not have a return statement?

Python automatically returns None.

def test():
    print("Hello")

print(test())


Output:
Hello
None

3. What is the difference between print() and return()?

| print()                    | return                   |
| -------------------------- | ------------------------ |
| Displays output            | Sends output back        |
| Cannot be reused easily    | Can be stored and reused |
| Used for debugging/display | Used for program logic   |

4. Can a function return different data types?

Yes.

return 10
return "Python"
return True
return [1,2,3]

5. Why is return preferred over print in large applications?

Because returned values can be reused, tested, and processed further.

6. Can a returned value be assigned to a variable?

Yes.

result = add(5, 5)


7. Does return stop function execution?

Yes. Any code after return will not execute.

8. Can a function have multiple return statements?

Yes. Only one executes depending on the program flow.

9. What happens after return is executed?

Function execution stops immediately.

10. What is an empty return?

A return statement without a value.

return

It exits the function and returns None.

11. What is conditional return?

Returning different values based on conditions.

if score > 50:
    return "Pass"
else:
    return "Fail"

12. What value does an empty return produce?

It returns None.

13. Is code after return executed?

No.

return 10
print("Hello")

The print statement never runs.

14. Why are multiple returns useful?

They simplify decision-making and make code easier to read.

15. What is a docstring in Python?

A docstring is a string used to document functions, classes, or modules.

16. How is a docstring different from a comment?

| Comment           | Docstring                  |
| ----------------- | -------------------------- |
| Uses #            | Uses """ """               |
| Ignored by Python | Stored by Python           |
| Not accessible    | Accessible through **doc** |

17. Why are docstrings important?

They improve readability, maintenance, and documentation.

18. Where should a function docstring be written?

Immediately below the function definition.

def add(a, b):
    """Adds two numbers."""

19. How can you access a docstring?

Using:

function_name.__doc__

20. Can docstrings span multiple lines?

Yes.

"""
Line 1
Line 2
Line 3
"""

21. What are the benefits of using docstrings?

* Better documentation
* Easier maintenance
* IDE support
* Helpful for teams
* Improves code quality
