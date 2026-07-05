# Creating Your Own Class

## Quick Short Notes

* A class is a blueprint used to create objects.
* Objects are instances of a class.
* Classes help organize related data and behavior.
* Use the `class` keyword to create a class.
* Class names follow the **PascalCase** naming convention.
* Empty classes can use the `pass` keyword.
* Objects are created by calling the class name.
* Each object can have its own attributes and methods.
* Classes improve code reusability.
* OOP models real-world entities easily.

---

## What is a Class?

A class is a blueprint or template used to create objects.

It defines:

* Data (attributes)
* Behavior (methods)

A class itself does not represent a real object until an instance is created.

---

## Creating a Class

```
class User:
    pass

user_1 = User()
```

### Explanation

| Component | Description                    |
| --------- | ------------------------------ |
| `class`   | Keyword used to create a class |
| `User`    | Class name                     |
| `pass`    | Placeholder for an empty class |
| `user_1`  | Object (instance)              |
| `User()`  | Creates a new object           |

---

## What is an Object?

An object is an instance of a class.

Example:

```
user_1 = User()
```

Here:

* `User` is the class.
* `user_1` is the object.
* The object is created from the class blueprint.

---

## PascalCase Naming Convention

Class names should follow **PascalCase**.

### Example

```
class StudentRecord:
    pass
```

### Rules

* Every word starts with a capital letter.
* No underscores between words.

### Examples

```
class User:
    pass

class BankAccount:
    pass

class StudentRecord:
    pass
```

---

## Using the `pass` Keyword

The `pass` keyword creates an empty code block.

Example:

```
class User:
    pass
```

Without `pass`, Python would raise an error because the class body cannot be empty.

---

## Why Use Classes?

Classes help developers:

* Organize code
* Reuse functionality
* Model real-world objects
* Reduce duplication
* Improve maintainability

### Real-World Examples

| Class         | Possible Objects     |
| ------------- | -------------------- |
| `User`        | Alice, Bob, Charlie  |
| `Car`         | Toyota, Honda, Tesla |
| `Student`     | Student records      |
| `BankAccount` | Customer accounts    |

---

## Class vs Object

| Class             | Object                  |
| ----------------- | ----------------------- |
| Blueprint         | Instance                |
| Defines structure | Contains actual data    |
| Created once      | Can have many instances |
| Example: `User`   | Example: `user_1`       |

---

## Example Workflow

### Step 1: Create a Class

```
class User:
    pass
```

### Step 2: Create an Object

```
user_1 = User()
```

### Result

* Class blueprint exists.
* Object is created from the blueprint.

---

## Benefits of OOP

Using classes and objects provides:

* Better code organization
* Reusability
* Scalability
* Easier maintenance
* Real-world modeling

---

## FAQs

### 1. What is a class?

A class is a blueprint for creating objects.

Example:

```
class User:
    pass
```

### 2. What is an object?

An object is an instance created from a class.

Example:

```
user_1 = User()
```

### 3. Why use classes?

Classes organize data and behavior together, making code easier to manage and reuse.

### 4. What naming convention is used for classes?

**PascalCase**

Example:

```
class StudentRecord:
    pass
```

### 5. What does `pass` do?

The `pass` keyword creates an empty block of code and prevents syntax errors.

Example:

```
class User:
    pass
```

---

## Key Takeaways

* A class is a blueprint for objects.
* An object is an instance of a class.
* Classes are created using the `class` keyword.
* Objects are created using `ClassName()`.
* Class names follow the PascalCase convention.
* The `pass` keyword allows empty classes.
* Classes help organize data and behavior.
* OOP makes programs more reusable and maintainable.
