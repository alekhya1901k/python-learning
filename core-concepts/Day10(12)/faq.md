**FAQs (Interview Recommended)**

1. What is a namespace in Python?

A namespace is a mapping between names and objects. It stores variables, functions, and classes.

2. What is scope in Python?

Scope defines where a variable can be accessed in the program.

3. What is local scope?

Variables declared inside a function belong to local scope and are accessible only within that function.

4. What is global scope?

Variables declared outside functions belong to global scope and can be accessed throughout the file.

5. What happens if a local variable is accessed outside its function?

Python raises a NameError.

def demo():
    x = 10

print(x)

6. Which scope is searched first by Python?

Python first searches the Local Scope and then follows the LEGB rule.

7. Can functions have local variables with the same name as global variables?

Yes. The local variable temporarily hides the global variable inside that function.

name = "Global"

def show():
    name = "Local"
    print(name)

show()

Output: Local

8. Does Python support block scope?

No. Python does not support block scope for loops and conditional statements.

9. What is block scope?

Block scope means variables exist only within a block such as if, for, or while. Python does not implement this behavior.

10. Are variables inside a for loop accessible outside the loop?

Yes.

for i in range(3):
    pass

print(i)

Output: 2

11. Which structure creates a new scope in Python?

Functions create new scopes.

12. Why is Python different from languages like Java or C++?

Python follows function-level scoping rather than block-level scoping.

13. Can variables declared inside an if statement be used later?

Yes.

if True:
    x = 10

print(x)

14. Is indentation related to variable scope?

No. Indentation defines code blocks but does not create block scope.

15. What is a global variable?

A variable declared outside all functions.

16. Can a function read a global variable?

Yes.

x = 100

def show():
    print(x)


17. Why is the global keyword needed?

To tell Python that you want to modify the global variable rather than create a new local one.

18. What happens if global is omitted while modifying?

Python raises an error.

x = 1

def update():
    x += 1

19. Is using global variables recommended?

Only when necessary. Excessive use can make programs difficult to maintain.

20. Can multiple functions access the same global variable?

Yes.

21. What is a common use case for global variables?

Application settings, configuration values, and shared constants.

22. What is a constant?

A value that should remain unchanged throughout program execution.

23. Does Python support true constants?

No. Python relies on naming conventions.

24. How are constants named in Python?

Using ALL_CAPS naming style.

MAX_SIZE = 100

25. Why use constants?

To improve readability and avoid hardcoded values.

26. Where are constants usually declared?

At the top of the file in global scope.

27. Can constants be modified?

Technically yes, but it is considered bad practice.

PI = 3.14159
PI = 4

28. Give examples of commonly used constants.

PI = 3.14159
MAX_ATTEMPTS = 3
API_URL = "https://api.example.com"
SECONDS_IN_DAY = 86400
