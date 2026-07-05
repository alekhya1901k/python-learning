

## 1. What is a class in Python?

A class is a blueprint used to create objects.

---

## 2. What is an object?

An object is an instance of a class.

---

## 3. What is OOP?

OOP (Object-Oriented Programming) is a programming paradigm based on objects and classes.

---

## 4. What is the purpose of `__init__()`?

`__init__()` is a constructor used to initialize object attributes when an object is created.

---

## 5. What does `self` represent?

`self` represents the current object instance.

---

## 6. What are attributes?

Attributes are variables associated with an object that store data.

Example:

```
self.name = "Angela"
```

---

## 7. What are methods?

Methods are functions defined inside a class that describe object behavior.

Example:

```
def gain_follower(self):
    pass
```

---

## 8. Difference between a class and an object?

| Class | Object |
|---------|---------|
| Blueprint | Real instance |
| Defines structure | Contains actual data |
| Created once | Can have many instances |

Example:

```
class User:
    pass
```

```
user_1 = User()
```

---

## 9. Why use constructors?

Constructors initialize objects with required data and reduce repetitive code.

Example:

```
user = User("001", "Angela")
```

---

## 10. What is encapsulation?

Encapsulation is the practice of bundling data and methods together inside a class.

Example:

```
class User:
    def __init__(self):
        self.followers = 0

    def gain_follower(self):
        self.followers += 1
```

---

## 11. What is modularity in OOP?

Modularity means separating responsibilities into independent classes or components.

Benefits:

- Easier maintenance
- Better organization
- Improved reusability

---

## 12. Why are classes useful in large projects?

Classes improve:

- Maintainability
- Readability
- Reusability
- Scalability

---

## 13. What is dot notation?

Dot notation (`.`) is used to access attributes and methods of an object.

Examples:

```
user.name
```

```
user.gain_follower()
```

---

## 14. What is a default attribute value?

A default attribute value is an automatically assigned starting value.

Example:

```
def __init__(self, followers=0):
    self.followers = followers
```

Here, `followers` defaults to `0`.

---

## 15. Why convert dictionaries into objects?

Objects provide:

- Cleaner code
- Better structure
- Easier attribute access
- Improved maintainability

Example:

Instead of:

```
question["text"]
```

Use:

```
question.text
```

---

## 16. What is a boolean value?

A boolean value can have one of two values:

```
True
```

or

```
False
```

Boolean values are commonly used in conditions and loops.

---

## 17. Why use `len()` in QuizBrain?

`len()` determines the total number of questions.

Example:

```
len(self.question_list)
```

This helps decide when the quiz should end.

---

## 18. Why use a Question class?

The `Question` class models quiz question data.

It stores:

- Question text
- Correct answer

Example:

```
Question(
    "2 + 3 = 5",
    "True"
)
```

---

## 19. Why use a QuizBrain class?

The `QuizBrain` class manages quiz logic separately from question data.

Responsibilities:

- Display questions
- Check answers
- Track score
- Control quiz flow

---

## 20. What is the biggest benefit of OOP in this project?

The biggest benefits are:

- Easy maintenance
- Code reusability
- Modular design
- Better organization
- Scalability

By separating responsibilities into classes, the quiz project becomes easier to understand, modify, and extend.

---

## Day 17 Key Takeaways

- Classes are blueprints; objects are instances.
- OOP organizes code into reusable components.
- `__init__()` initializes object data.
- `self` refers to the current object.
- Attributes store data; methods define behavior.
- Encapsulation combines data and methods within classes.
- Modularity separates responsibilities into independent components.
- `Question` stores quiz data.
- `QuizBrain` controls quiz logic.
- OOP makes applications easier to maintain, extend, and reuse.