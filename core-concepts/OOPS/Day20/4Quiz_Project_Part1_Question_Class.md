# Starting the Quiz Game with the Question Class

## Quick Short Notes

- The Quiz Game starts with a `Question` class.
- Each question has `text` and `answer` attributes.
- A constructor initializes both values.
- The `Question` class acts as a model.
- Objects represent individual quiz questions.
- Every question object stores its own data.
- Question data becomes easier to manage.
- OOP makes quiz questions reusable.
- Question objects improve readability.
- This is the foundation of the quiz project.

---

## Why Create a Question Class?

In a quiz application, every question contains similar information:

- Question text
- Correct answer

Instead of storing this information separately, we can create a class to represent a question.

This makes the code:

- Cleaner
- More organized
- Easier to maintain
- Easier to expand

---

## The Question Class

```
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

### Explanation

| Component | Purpose |
|------------|---------|
| `Question` | Class name |
| `__init__()` | Constructor |
| `q_text` | Receives question text |
| `q_answer` | Receives correct answer |
| `self.text` | Stores question text |
| `self.answer` | Stores correct answer |

---

## Understanding the Constructor

```
def __init__(self, q_text, q_answer):
    self.text = q_text
    self.answer = q_answer
```

When a question object is created:

1. The constructor runs automatically.
2. Question text is stored in `self.text`.
3. Correct answer is stored in `self.answer`.

Each object receives its own values.

---

## Creating an Object

```
new_q = Question(
    "2 + 3 = 5",
    "True"
)
```

### What Happens?

1. A new `Question` object is created.
2. `"2 + 3 = 5"` is assigned to `text`.
3. `"True"` is assigned to `answer`.
4. The object is stored in `new_q`.

---

## Accessing Attributes

After creating the object:

```
print(new_q.text)
print(new_q.answer)
```

Output:

```
2 + 3 = 5
True
```

---

## Multiple Question Objects

The same class can create many question objects.

Example:

```
question1 = Question(
    "2 + 3 = 5",
    "True"
)

question2 = Question(
    "The Earth is flat.",
    "False"
)

question3 = Question(
    "Python is a programming language.",
    "True"
)
```

Each object stores its own data independently.

---

## Why Use Objects for Questions?

Without OOP:

```
question_text = "2 + 3 = 5"
question_answer = "True"
```

Managing many questions becomes difficult.

With OOP:

```
question = Question(
    "2 + 3 = 5",
    "True"
)
```

Benefits:

- Better organization
- Easier management
- More readable code
- Reusable structure

---

## Question Class as a Model

The `Question` class acts as a model for quiz questions.

It defines what every question should contain:

- Text
- Answer

Every object created from the class follows the same structure.

---

## Real-World Analogy

Think of the class as a template.

### Template

```
Question
```

### Objects Created from the Template

```
Question 1
Question 2
Question 3
```

Each object contains different values but follows the same design.

---

## Role in the Quiz Project

The `Question` class is the foundation of the quiz game.

Later, these question objects can be:

- Stored in lists
- Displayed to users
- Checked for correctness
- Used to calculate scores

The entire quiz system is built around these objects.

---

## FAQs

### 1. Why create a Question class?

To model quiz questions and keep related data together.

Benefits:

- Organization
- Reusability
- Readability

---

### 2. What attributes does it contain?

The class contains:

- `text`
- `answer`

Example:

```
self.text = q_text
self.answer = q_answer
```

---

### 3. Why use objects for questions?

Objects make question data easier to organize and manage.

Each question becomes a single structured unit.

---

### 4. Is every question a separate object?

Yes.

Example:

```
question1 = Question(...)
question2 = Question(...)
question3 = Question(...)
```

Each object stores its own data.

---

### 5. What is initialized in the constructor?

The constructor initializes:

- Question text
- Correct answer

Example:

```
def __init__(self, q_text, q_answer):
    self.text = q_text
    self.answer = q_answer
```

---

## Key Takeaways

- The Quiz Game begins with a `Question` class.
- Each question object contains `text` and `answer` attributes.
- The constructor initializes both values.
- Every question is a separate object.
- The class acts as a reusable model for quiz questions.
- OOP improves organization and readability.
- Question objects form the foundation of the entire quiz project.