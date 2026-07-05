# Using Open Trivia DB with the Quiz Project

## Quick Short Notes

- Open Trivia DB provides free quiz questions.
- Data is received in JSON format.
- JSON resembles Python dictionaries.
- Only `question` and `correct_answer` are needed.
- OOP allows easy data replacement.
- `QuizBrain` works without modification.
- Modularity is a major OOP advantage.
- Different datasets can use the same logic.
- Classes isolate responsibilities.
- OOP makes large applications easier to maintain.

---

## What Is Open Trivia DB?

Open Trivia DB is a free online database that provides trivia questions.

It supplies questions from various categories such as:

- Science
- History
- Geography
- Sports
- Entertainment

These questions can be used directly in quiz applications.

---

## Data Format

Open Trivia DB returns data in **JSON** format.

### What Is JSON?

JSON stands for:

```
JavaScript Object Notation
```

It is a common format for storing and exchanging data.

Example:

```
{
    "question": "2 + 3 = 5",
    "correct_answer": "True"
}
```

---

## JSON and Python Dictionaries

JSON looks very similar to Python dictionaries.

### JSON

```
{
    "question": "2 + 3 = 5",
    "correct_answer": "True"
}
```

### Python Dictionary

```
{
    "question": "2 + 3 = 5",
    "correct_answer": "True"
}
```

Because of this similarity, JSON data is easy to work with in Python.

---

## Previous Data Structure

Earlier quiz data used:

```
question["text"]
question["answer"]
```

Example:

```
{
    "text": "2 + 3 = 5",
    "answer": "True"
}
```

---

## Open Trivia DB Data Structure

Open Trivia DB uses different key names.

### New Keys

```
question["question"]
question["correct_answer"]
```

Example:

```
{
    "question": "2 + 3 = 5",
    "correct_answer": "True"
}
```

---

## Converting Data into Question Objects

Previous version:

```
new_question = Question(
    question["text"],
    question["answer"]
)
```

Open Trivia DB version:

```
new_question = Question(
    question["question"],
    question["correct_answer"]
)
```

Only the data mapping changes.

The rest of the application remains unchanged.

---

## Why Didn't QuizBrain Need Changes?

`QuizBrain` works with `Question` objects.

It does not care where the data comes from.

Example:

```
Question(
    text="2 + 3 = 5",
    answer="True"
)
```

Whether the data comes from:

- A local list
- A file
- A database
- Open Trivia DB

`QuizBrain` still receives the same `Question` objects.

---

## OOP Advantage: Modularity

Modularity means separating a program into independent components.

### Question Class

Responsible for:

- Question text
- Correct answer

### QuizBrain Class

Responsible for:

- Quiz flow
- Scoring
- User interaction

### Data Source

Responsible for:

- Supplying question data

Each component has a separate responsibility.

---

## Visual Representation

```text
Open Trivia DB
        ↓
     JSON Data
        ↓
 Question Objects
        ↓
   Question Bank
        ↓
    QuizBrain
        ↓
      Quiz
```

Notice that only the data source changes.

The quiz engine remains the same.

---

## Benefits of Modularity

Because responsibilities are separated:

- Code is easier to update.
- Components are reusable.
- Bugs are easier to find.
- New features are easier to add.
- Data sources can be replaced easily.

---

## Example of Data Replacement

### Source 1

```
question_data = [...]
```

### Source 2

```
Open Trivia DB API
```

### Source 3

```
Database
```

### Source 4

```
CSV File
```

All can create:

```
Question Objects
```

The rest of the application stays unchanged.

---

## Real-World Analogy

Imagine a restaurant.

### Kitchen

Prepares food.

### Supplier

Provides ingredients.

The kitchen does not care which supplier delivers ingredients.

As long as ingredients arrive, the kitchen operates normally.

Similarly:

```
QuizBrain
```

does not care where questions originate.

It only needs valid `Question` objects.

---

## Why OOP Helps Large Applications

As applications grow:

- More files are added.
- More features are added.
- More developers may contribute.

OOP helps by:

- Separating responsibilities
- Reducing dependencies
- Improving maintainability
- Encouraging code reuse

This makes large projects easier to manage.

---

## FAQs

### 1. What is Open Trivia DB?

A free online trivia question database that provides quiz questions.

---

### 2. What format does it provide?

JSON.

Example:

```
{
    "question": "...",
    "correct_answer": "..."
}
```

---

### 3. Why didn't QuizBrain need changes?

Because of modular OOP design.

`QuizBrain` works with `Question` objects and does not depend on the original data source.

---

### 4. What is modularity?

Modularity is the practice of separating a program into independent components with specific responsibilities.

Benefits:

- Easier maintenance
- Better organization
- Improved reusability

---

### 5. Why is OOP useful here?

OOP allows easy replacement of data sources without changing the quiz logic.

Only the data conversion step changes.

---

## Key Takeaways

- Open Trivia DB provides free trivia questions.
- Data is delivered in JSON format.
- JSON closely resembles Python dictionaries.
- Only `question` and `correct_answer` fields are needed.
- Question data is converted into `Question` objects.
- `QuizBrain` works without modification.
- Modularity separates responsibilities into independent components.
- OOP makes data sources interchangeable.
- Classes improve maintainability and scalability.
- This flexibility is one of the biggest advantages of Object-Oriented Programming.