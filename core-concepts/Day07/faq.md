1. What is a function in Python?

A function is a reusable block of code that performs a specific task.

2. What is a parameter?

A parameter is a variable used while defining a function.

Example:

def greet(name):

name is the parameter.

3. What is an argument?

An argument is the actual value passed to the function.

greet("Alex")

"Alex" is the argument.

4. Can functions take multiple inputs?

Yes.

def add(a, b):
    print(a + b)

5. Why are functions important?

Functions improve:

* Code reuse
* Readability
* Maintenance
* Modularity

6. What happens if no argument is passed?

Python raises an error.

Example:

def greet(name):
    print(name)

greet()

Output:

TypeError

7. Can parameters have any name?

Yes, but meaningful names are recommended.

Good:

def calculate_total(price):

Bad:

def calculate_total(x):

8. What are positional arguments?

Arguments assigned according to their order in the function call.

9. What are keyword arguments?

Arguments assigned using parameter names.

Example:

greet(name="Tom")

10. Which is better: positional or keyword arguments?

Positional → shorter
Keyword → clearer and safer

Large programs usually prefer keyword arguments for readability.

11. Can we use both positional and keyword arguments together?

Yes.

student("Alex", grade="A")


12. What happens if positional argument order is wrong?

Values get assigned incorrectly.

13. Why are keyword arguments useful?

They:

* Improve clarity
* Prevent mistakes
* Make code easier to understand

14. Can keyword arguments be passed in any order?

Yes.

greet(location="Texas", name="Angela")

still works correctly.
