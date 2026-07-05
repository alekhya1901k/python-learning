# Interview FAQs

## 1. What is Object Oriented Programming (OOP)?

OOP is a programming paradigm that organizes software into objects containing related data and behaviors, making code easier to manage and reuse.

---

## 2. What is Procedural Programming?

Procedural Programming organizes code into functions and procedures that execute sequentially to solve a problem.

---

## 3. Why is OOP preferred for large applications?

Because it improves maintainability, scalability, modularity, and code reusability while reducing complexity.

---

## 4. What problem does OOP solve?

OOP helps manage complex relationships between different parts of a program and reduces tightly coupled code.

---

## 5. What is modularity in OOP?

Modularity means breaking a large system into smaller independent components that can be developed and maintained separately.

---

## 6. How does OOP improve teamwork?

Different developers or teams can work on different objects/modules without affecting the entire system.

---

## 7. What is code reusability?

Code reusability means using existing components in multiple projects without rewriting them.

---

## 8. Give a real-world example used to explain OOP.

A restaurant where different employees perform different responsibilities (chef, waiter, cleaner, receptionist), allowing efficient operation.

---

## 9. What is "spaghetti code"?

Spaghetti code refers to overly complex, tangled code where relationships between functions and variables become difficult to understand.

---

## 10. What are the main advantages of OOP over Procedural Programming?

* Better organization
* Easier maintenance
* Code reuse
* Improved scalability
* Better collaboration among developers

## 11. What is a class?

A class is a blueprint used to create objects.

## 12. What is an object?

An object is an instance created from a class.

## 13. Can one class create multiple objects?

Yes.

## 14. Why do we use classes?

To organize and reuse code.

## 15. What naming convention is used for classes?

PascalCase.

Example:

CoffeeMaker
MoneyMachine

### 16. How do you create an object?

```
object_name = ClassName()
```

Example:

```
timmy = Turtle()
```

---

### 17. What is dot notation?

Dot notation (`.`) is used to access an object's attributes and methods.

Example:

```
timmy.color("blue")
print(my_screen.canvheight)
```

---

### 18. What is an attribute?

An attribute is data associated with an object.

Example:

```
my_screen.canvheight
```

---

### 19. What is a method?

A method is a function associated with an object.

Example:

```
timmy.forward(100)
```

---

### 20. What is object construction?

Object construction is the process of creating an object from a class.

Example:

```
timmy = Turtle()
```


### 21. What is PyPI?

PyPI stands for **Python Package Index**.

It is the official repository for Python packages.

---

### 22. Why do we use packages?

Packages allow developers to reuse existing code instead of building everything from scratch.

Benefits include:

- Faster development
- Less code to write
- More reliable solutions

---

### 23. What is the difference between a module and a package?

| Module | Package |
|----------|----------|
| Single Python file | Collection of modules |
| Contains code | Organizes related modules |

---

### 24. How do you install a package?

```
pip install package_name
```

Example:

```
pip install prettytable
```

---

### 25. Why should developers read documentation?

Documentation helps developers understand:

- Available classes
- Attributes
- Methods
- Installation steps
- Usage examples

---


### 26. What is PrettyTable?

PrettyTable is a package used to create formatted ASCII tables in Python.

---

### 27. Is `add_column()` a method or attribute?

**Method**

Example:

```
table.add_column("Name", ["Alice", "Bob"])
```

It performs an action by adding a column.

---

### 28 Is `align` a method or attribute?

**Attribute**

Example:

```
table.align = "l"
```

It stores a formatting setting.

---

### 29. How do you modify an attribute?

```
table.align = "l"
```

General syntax:

```
object.attribute = value
```

---

### 30. Why are attributes useful?

Attributes allow customization of an object's behavior and appearance.

Examples include:

- Alignment settings
- Colors
- Sizes
- Configuration options

---

### 31. Why is OOP useful in the Coffee Machine project?

OOP divides the application into classes, with each class handling a specific responsibility.

Benefits include:

- Better organization
- Easier maintenance
- Reusable code

---

### 32. Which class manages ingredients?

**CoffeeMaker**

Responsibilities:

- Water
- Milk
- Coffee
- Brewing drinks

---

### 33. Which class manages money?

**MoneyMachine**

Responsibilities:

- Accepting coins
- Calculating payments
- Returning change
- Tracking profit

---

### 34. Which class manages drink information?

**Menu** and **MenuItem**

- `Menu` stores available drinks.
- `MenuItem` represents an individual drink.

---

### 35. What OOP principle is demonstrated?

**Separation of responsibilities** and **modular design**.

Each class focuses on one task, making the system easier to manage and extend.

---
