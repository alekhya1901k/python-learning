# Methods in Classes

## Quick Short Notes

- Methods define object behavior.
- Methods are functions inside classes.
- Every method must have `self` as the first parameter.
- Methods can modify attributes.
- Methods can accept additional parameters.
- Objects call methods using dot notation.
- Methods improve encapsulation.
- Methods operate on object data.
- Different objects can use the same method differently.
- Methods make classes interactive.

---

## What Is a Method?

A method is a function defined inside a class.

Methods describe what an object can do.

Example:

```
class User:

    def gain_follower(self):
        pass
```

Here, `gain_follower()` is a method of the `User` class.

---

## Example

```
class User:

    def __init__(self):
        self.followers = 0

    def gain_follower(self):
        self.followers += 1
```

### Explanation

- The constructor creates a `followers` attribute.
- The `gain_follower()` method increases the follower count by 1.
- The method operates on the object's data.

---

## Calling a Method

```
user.gain_follower()
```

### What Happens?

1. Python finds the `gain_follower()` method.
2. The current object is passed to `self`.
3. The method executes.
4. `followers` increases by 1.

---

## Why Is `self` Required?

`self` refers to the current object.

Example:

```
self.followers += 1
```

Meaning:

```
current_object.followers += 1
```

Without `self`, the method cannot access the object's attributes.

---

## Methods Can Modify Attributes

Methods often change object data.

Example:

```
class User:

    def __init__(self):
        self.followers = 0

    def gain_follower(self):
        self.followers += 1
```

Before:

```
followers = 0
```

After:

```
user.gain_follower()

followers = 1
```

---

## Methods Can Accept Parameters

Methods can receive additional information through parameters.

Example:

```
class User:

    def add_followers(self, amount):
        self.followers += amount
```

Calling the method:

```
user.add_followers(5)
```

Result:

```
followers increases by 5
```

---

## Dot Notation

Methods are called using dot notation.

### Syntax

```
object.method()
```

### Example

```
user.gain_follower()
```

Here:

- `user` is the object.
- `gain_follower()` is the method.

---

## Encapsulation

Methods help encapsulate behavior inside a class.

Instead of changing attributes directly:

```
user.followers += 1
```

You can use a method:

```
user.gain_follower()
```

This keeps object behavior organized and controlled.

---

## Methods Work on Object Data

Example:

```
class User:

    def __init__(self):
        self.followers = 0

    def gain_follower(self):
        self.followers += 1
```

Each object maintains its own data.

```
user1 = User()
user2 = User()
```

Calling:

```
user1.gain_follower()
```

Only changes:

```
user1.followers
```

It does not affect:

```
user2.followers
```

---

## Function vs Method

| Function | Method |
|-----------|---------|
| Exists independently | Belongs to a class |
| Not tied to an object | Operates on an object |
| Called directly | Called through an object |
| Example: `print()` | Example: `user.gain_follower()` |

---

## Complete Example

```
class User:

    def __init__(self):
        self.followers = 0

    def gain_follower(self):
        self.followers += 1

user = User()

user.gain_follower()

print(user.followers)
```

Output:

```
1
```

---

## FAQs

### 1. What is a method?

A method is a function defined inside a class.

Example:

```
def gain_follower(self):
    pass
```

---

### 2. Why is `self` required?

`self` allows the method to access the current object's attributes and other methods.

Example:

```
self.followers += 1
```

---

### 3. Can methods change attributes?

Yes.

Example:

```
def gain_follower(self):
    self.followers += 1
```

This modifies the `followers` attribute.

---

### 4. How are methods called?

Using dot notation.

Syntax:

```
object.method()
```

Example:

```
user.gain_follower()
```

---

### 5. Difference between a function and a method?

- Functions exist independently.
- Methods belong to objects and classes.

Example:

```
print("Hello")
```

Function

```
user.gain_follower()
```

Method

---

## Key Takeaways

- Methods define object behavior.
- Methods are functions inside classes.
- Every method requires `self` as the first parameter.
- Methods can modify object attributes.
- Methods can accept additional parameters.
- Methods are called using dot notation.
- Methods support encapsulation and code organization.
- Different objects can use the same method while maintaining separate data.
- Methods make classes interactive and useful.