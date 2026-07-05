# Creating the QuizBrain Class

## Quick Short Notes

- `QuizBrain` controls quiz flow.
- It receives the question bank.
- It tracks the current question number.
- Question numbering starts at zero internally.
- `next_question()` displays questions.
- Current question is retrieved from the list.
- User answers are collected using `input()`.
- Quiz logic is separated from question data.
- OOP improves maintainability.
- `QuizBrain` becomes the controller of the quiz.

---

## What Is QuizBrain?

`QuizBrain` is the class responsible for managing the quiz.

It controls:

- Question progression
- User interaction
- Quiz flow
- Score tracking (later)
- Answer checking (later)

Think of it as the controller of the entire quiz application.

---

## Creating the QuizBrain Class

```
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
```

### Explanation

| Component | Purpose |
|------------|---------|
| `QuizBrain` | Quiz controller class |
| `q_list` | Receives question bank |
| `question_number` | Tracks current question |
| `question_list` | Stores all questions |

---

## Understanding the Constructor

```
def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
```

When a `QuizBrain` object is created:

1. Question number starts at `0`.
2. The question bank is stored.
3. The quiz is ready to begin.

---

## Why Start at Zero?

Python lists use zero-based indexing.

Example:

```
question_list[0]
```

Accesses the first question.

```
question_list[1]
```

Accesses the second question.

```
question_list[2]
```

Accesses the third question.

Therefore:

```
self.question_number = 0
```

Starts the quiz at the first question.

---

## The Question List

```
self.question_list = q_list
```

The question list contains all `Question` objects.

Example:

```
[
    Question(...),
    Question(...),
    Question(...)
]
```

The `QuizBrain` uses this list to retrieve questions.

---

## The `next_question()` Method

```
def next_question(self):
    current_question = self.question_list[self.question_number]
```

### Purpose

Retrieve the current question from the question bank.

### Explanation

```
self.question_list
```

Stores all questions.

```
self.question_number
```

Tracks the current position.

```
current_question
```

Stores the question currently being asked.

---

## Retrieving the Current Question

Example:

```
self.question_number = 0
```

Then:

```
current_question =
self.question_list[0]
```

Returns the first question.

If:

```
self.question_number = 1
```

Then:

```
current_question =
self.question_list[1]
```

Returns the second question.

---

## Asking the User

A complete version might look like:

```
def next_question(self):
    current_question = self.question_list[self.question_number]

    answer = input(
        f"Q.{self.question_number + 1}: "
        f"{current_question.text} "
        "(True/False): "
    )
```

This:

1. Retrieves the current question.
2. Displays it.
3. Collects the user's answer.

---

## Quiz Flow

```text
Question Bank
       ↓
   QuizBrain
       ↓
Retrieve Question
       ↓
Display Question
       ↓
Get User Answer
       ↓
Move to Next Question
```

---

## Why Separate QuizBrain from Question?

### Question Class

Responsible for storing:

- Question text
- Correct answer

Example:

```
Question(
    "2 + 3 = 5",
    "True"
)
```

### QuizBrain Class

Responsible for:

- Displaying questions
- Tracking progress
- Collecting answers
- Managing quiz flow

This separation keeps responsibilities clear.

---

## Benefits of Modular Design

Separating classes provides:

- Cleaner code
- Easier debugging
- Better maintenance
- Improved scalability
- Higher reusability

Each class focuses on a single responsibility.

---

## Example Usage

### Create Question Bank

```
question_bank = [...]
```

### Create QuizBrain Object

```
quiz = QuizBrain(question_bank)
```

### Ask a Question

```
quiz.next_question()
```

The quiz controller handles the rest.

---

## Real-World Analogy

### Question Class

Acts like a flashcard.

Contains:

- Question
- Answer

### QuizBrain Class

Acts like the teacher.

Responsible for:

- Showing flashcards
- Asking questions
- Tracking progress

---

## FAQs

### 1. What is QuizBrain?

A class that manages quiz operations and controls quiz flow.

Responsibilities include:

- Displaying questions
- Tracking progress
- Managing user interaction

---

### 2. Why store `question_number`?

To track which question is currently being displayed.

Example:

```
self.question_number = 0
```

---

### 3. What is `question_list`?

The list containing all `Question` objects.

Example:

```
self.question_list = q_list
```

---

### 4. What does `next_question()` do?

It retrieves and displays the next question in the quiz.

Example:

```
current_question =
self.question_list[self.question_number]
```

---

### 5. Why separate QuizBrain from Question?

For modular design.

- `Question` stores data.
- `QuizBrain` controls behavior.

This makes the program easier to maintain and extend.

---

## Key Takeaways

- `QuizBrain` is the controller of the quiz.
- It receives the question bank during initialization.
- `question_number` tracks progress through the quiz.
- Questions are retrieved using list indexing.
- `next_question()` displays the current question.
- User answers are typically collected with `input()`.
- Quiz logic is separated from question data.
- OOP improves organization, maintainability, and scalability.
- `QuizBrain` forms the core engine of the quiz application.