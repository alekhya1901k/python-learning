# Day 21 - Quiz Game Using OOP

## Project Objective

Build a True/False Quiz Game using Object-Oriented Programming (OOP) concepts in Python.

## Concepts Covered

1. Classes and Objects
2. Attributes
3. Constructors (`__init__`)
4. Methods
5. Encapsulation
6. Lists of Objects
7. Object Interaction
8. Data Modeling
9. Quiz Flow Control
10. Score Tracking

## Project Files

| File                | Purpose                        |
| ------------------- | ------------------------------ |
| `main.py`           | Entry point of the application |
| `data.py`           | Stores question data           |
| `question_model.py` | Contains the Question class    |
| `quiz_brain.py`     | Contains the QuizBrain class   |

## Project Architecture

```text
main.py
    │
    ├── data.py
    │       │
    │       └── question_data
    │
    ├── question_model.py
    │       │
    │       └── Question Class
    │
    └── quiz_brain.py
            │
            └── QuizBrain Class
```

## Execution Flow

1. Load quiz questions from `data.py`.
2. Convert dictionaries into Question objects.
3. Store all Question objects in a Question Bank.
4. Create a QuizBrain object.
5. Display questions one by one.
6. Accept user input.
7. Check answers.
8. Update score.
9. Continue until all questions are completed.
10. Display final score.

## How to Run

```bash
python main.py
```

## Sample Output

```text
Q.1: A slug's blood is green. (True/False): True

You got it right!
The correct answer was: True
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): False

You got it right!
The correct answer was: False
Your current score is: 2/2
```

## Expected Learning Outcomes

By completing this project, you will understand:

* How to create custom classes.
* How constructors initialize objects.
* How attributes store object data.
* How methods define object behavior.
* How multiple classes collaborate in a project.
* How OOP improves modularity and maintainability.
* How to separate data, models, and business logic.

## Final Result

The application presents a complete True/False quiz, validates answers, tracks the score, and displays the final result after all questions are answered.
