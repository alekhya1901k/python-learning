# Attributes, Constructors, and `__init__`

## Quick Short Notes

- Attributes are variables attached to objects.
- Attributes store object-specific data.
- Constructors initialize objects.
- Python constructors use `__init__()`.
- `__init__()` runs automatically during object creation.
- `self` refers to the current object.
- Constructor parameters receive initialization values.
- Attributes are created using `self.attribute_name`.
- Default values can be assigned to attributes.
- Constructors reduce repetitive code.

---

## What Are Attributes?

Attributes are variables that belong to an object.

They store data specific to that object.

Example:

```
user.id = "001"
user.name = "Angela"
```

Here:

- `id` is an attribute.
- `name` is an attribute.

Each object can have its own attribute values.

---

## What Is a Constructor?

A constructor is a special method used to initialize an object when it is created.

In Python, the constructor is:

```
__init__()
```

It runs automatically whenever a new object is created.

---

## Without Constructor

```
user = User()

user.id = "001"
user.name = "Angela"
```

### Problems

- Repetitive code
- Easy to forget attributes
- Difficult to manage many objects

---

## With Constructor

```
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user = User("001", "Angela")
```

### Benefits

- Initializes data automatically
- Cleaner code
- Less repetition
- Easier maintenance

---

## Understanding `__init__()`

```
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
```

### Breakdown

| Component | Purpose |
|------------|---------|
| `__init__` | Constructor method |
| `self` | Current object reference |
| `user_id` | Input parameter |
| `username` | Input parameter |
| `self.id` | Object attribute |
| `self.username` | Object attribute |

---

## What Is `self`?

`self` refers to the object currently being created or used.

Example:

```
self.id = user_id
```

Meaning:

```
current_object.id = user_id
```

Python automatically passes the current object to `self`.

---

## Creating Attributes

Attributes are typically created inside the constructor.

Example:

```
self.id = user_id
self.username = username
```

This creates two attributes:

- `id`
- `username`

for every object created from the class.

---

## Object Creation Flow

### Class Definition

```
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
```

### Object Creation

```
user = User("001", "Angela")
```

### What Happens?

1. Memory is allocated for the object.
2. `__init__()` is called automatically.
3. `"001"` is assigned to `user_id`.
4. `"Angela"` is assigned to `username`.
5. Attributes are created.
6. Object is ready for use.

---

## Accessing Attributes

```
print(user.id)
print(user.username)
```

Output:

```
001
Angela
```

---

## Using Default Values

Attributes can be given default values.

Example:

```
class User:
    def __init__(self, user_id, username, followers=0):
        self.id = user_id
        self.username = username
        self.followers = followers
```

Creating an object:

```
user = User("001", "Angela")
```

Result:

```
followers = 0
```

---

## Why Use Constructors?

Constructors help:

- Initialize object data
- Avoid repetitive code
- Ensure consistency
- Improve readability
- Simplify object creation

Without constructors, every attribute must be assigned manually.

---

## Real-World Example

### Class

```
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
```

### Object

```
student = Student("John", "A")
```

### Access Attributes

```
print(student.name)
print(student.grade)
```

Output:

```
John
A
```

---

## FAQs

### 1. What is `__init__()`?

A special method used to initialize objects.

Example:

```
def __init__(self):
    pass
```

---

### 2. When is `__init__()` called?

Automatically during object creation.

Example:

```
user = User()
```

Python automatically executes:

```
__init__()
```

---

### 3. What is `self`?

A reference to the current object.

Example:

```
self.username = username
```

---

### 4. Can attributes have default values?

Yes.

Example:

```
def __init__(self, followers=0):
    self.followers = followers
```

---

### 5. Why use constructors?

Constructors initialize object data efficiently and reduce repetitive code.

Benefits:

- Cleaner code
- Better organization
- Easier maintenance

---

## Key Takeaways

- Attributes store data inside objects.
- Constructors initialize objects.
- Python uses `__init__()` as the constructor.
- `__init__()` runs automatically during object creation.
- `self` refers to the current object.
- Attributes are created using `self.attribute_name`.
- Default values can be assigned to attributes.
- Constructors make object creation simpler and more consistent.