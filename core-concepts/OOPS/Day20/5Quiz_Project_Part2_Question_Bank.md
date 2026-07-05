# Creating a Question Bank from Question Data

## Quick Short Notes

- Question data comes from a list of dictionaries.
- Each dictionary contains question details.
- Data is converted into `Question` objects.
- A question bank stores all question objects.
- Loops help create objects efficiently.
- `append()` adds objects to the bank.
- Question objects are easier to use than dictionaries.
- Object attributes reduce typing mistakes.
- Data and logic remain separated.
- This prepares questions for the `QuizBrain`.

---

## What Is Question Data?

Question data is typically stored as a list of dictionaries.

Example:

```
question_data = [
    {
        "text": "2 + 3 = 5",
        "answer": "True"
    },
    {
        "text": "The Earth is flat.",
        "answer": "False"
    }
]
```

Each dictionary contains information about a single question.

---

## Why Convert Dictionaries to Objects?

While dictionaries work, objects provide a cleaner structure.

Dictionary Access:

```
question["text"]
question["answer"]
```

Object Access:

```
question.text
question.answer
```

Benefits:

- Easier to read
- Fewer typing mistakes
- Better organization
- More maintainable code

---

## Creating the Question Bank

```
question_bank = []

for question in question_data:
    new_question = Question(
        question["text"],
        question["answer"]
    )

    question_bank.append(new_question)
```

---

## Step-by-Step Explanation

### Step 1: Create an Empty List

```
question_bank = []
```

This list will store all `Question` objects.

---

### Step 2: Loop Through the Data

```
for question in question_data:
```

The loop processes one dictionary at a time.

Example:

```
{
    "text": "2 + 3 = 5",
    "answer": "True"
}
```

---

### Step 3: Create a Question Object

```
new_question = Question(
    question["text"],
    question["answer"]
)
```

This converts dictionary data into a `Question` object.

Example result:

```
Question(
    text="2 + 3 = 5",
    answer="True"
)
```

---

### Step 4: Add the Object to the Question Bank

```
question_bank.append(new_question)
```

The newly created object is added to the list.

---

## What Does the Final Question Bank Contain?

After the loop finishes:

```
question_bank
```

Contains:

```
[
    Question(...),
    Question(...),
    Question(...)
]
```

Instead of dictionaries, the list now stores `Question` objects.

---

## Visual Representation

### Original Data

```
Dictionary
    ↓

{
    "text": "...",
    "answer": "..."
}
```

### Conversion

```
Question(
    text,
    answer
)
```

### Stored In

```
question_bank
```

---

## Why Use a Loop?

Without a loop:

```
q1 = Question(...)
q2 = Question(...)
q3 = Question(...)
```

This becomes repetitive.

Using a loop:

```
for question in question_data:
```

Automatically creates all objects regardless of the number of questions.

Benefits:

- Less code
- Easier maintenance
- Scales to large datasets

---

## Separation of Data and Logic

### Data

```
question_data
```

Stores raw information.

### Logic

```
Question class
```

Defines how questions are represented.

This separation improves:

- Organization
- Reusability
- Readability

---

## Preparing for QuizBrain

The `question_bank` becomes the data source for the `QuizBrain` class.

Example:

```
quiz = QuizBrain(question_bank)
```

The quiz engine can then:

- Display questions
- Check answers
- Track scores
- Move through the quiz

---

## Complete Example

```
question_bank = []

for question in question_data:
    new_question = Question(
        question["text"],
        question["answer"]
    )

    question_bank.append(new_question)
```

Result:

```
question_bank = [
    Question(...),
    Question(...),
    Question(...)
]
```

---

## FAQs

### 1. What is a question bank?

A question bank is a list of `Question` objects.

Example:

```
question_bank = [
    Question(...),
    Question(...)
]
```

---

### 2. Why convert dictionaries to objects?

Objects provide:

- Cleaner code
- Better structure
- Easier attribute access

Example:

```
question.text
```

instead of:

```
question["text"]
```

---

### 3. Which loop is used?

A `for` loop.

Example:

```
for question in question_data:
```

---

### 4. What does `append()` do?

`append()` adds an item to the end of a list.

Example:

```
question_bank.append(new_question)
```

---

### 5. Why use Question objects instead of raw dictionaries?

Question objects:

- Provide better structure
- Improve readability
- Reduce typing mistakes
- Work well with OOP design

---

## Key Takeaways

- Question data is stored as a list of dictionaries.
- Each dictionary is converted into a `Question` object.
- A `for` loop automates object creation.
- `append()` adds objects to the question bank.
- The question bank stores all quiz questions.
- Objects are easier to manage than raw dictionaries.
- Data and logic remain separated.
- The question bank serves as the foundation for the `QuizBrain` class.