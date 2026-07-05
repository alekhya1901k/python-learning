# Keeping the Quiz Running with a While Loop

## Quick Short Notes

- The quiz should continue until all questions are asked.
- A `while` loop controls quiz execution.
- `still_has_questions()` checks remaining questions.
- It returns `True` or `False`.
- Boolean values control loop execution.
- Question number increases after every question.
- Quiz ends automatically when questions finish.
- `len()` helps determine total questions.
- Loop logic remains inside `QuizBrain`.
- This creates continuous gameplay.

---

## Why Use a While Loop?

A quiz should continue asking questions until there are no questions left.

A `while` loop is ideal because it repeatedly executes code while a condition remains `True`.

Example:

```
while quiz.still_has_questions():
    quiz.next_question()
```

This keeps the quiz running automatically.

---

## The `still_has_questions()` Method

```
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

### Purpose

Determine whether more questions remain in the quiz.

### Returns

- `True` → Continue the quiz
- `False` → Stop the quiz

---

## Understanding the Logic

```
self.question_number
```

Tracks the current question position.

```
len(self.question_list)
```

Returns the total number of questions.

Example:

```
len(self.question_list)
```

Output:

```
10
```

Meaning there are 10 questions in the quiz.

---

## How the Comparison Works

```
self.question_number < len(self.question_list)
```

### Example 1

```
question_number = 0
total_questions = 10
```

Check:

```
0 < 10
```

Result:

```
True
```

Continue the quiz.

---

### Example 2

```
question_number = 5
total_questions = 10
```

Check:

```
5 < 10
```

Result:

```
True
```

Continue the quiz.

---

### Example 3

```
question_number = 10
total_questions = 10
```

Check:

```
10 < 10
```

Result:

```
False
```

Stop the quiz.

---

## The Quiz Loop

```
while quiz.still_has_questions():
    quiz.next_question()
```

### What Happens?

1. Check `still_has_questions()`.
2. If `True`, ask the next question.
3. Increase question number.
4. Repeat.
5. Stop when `False` is returned.

---

## Visual Flow

```text
Start Quiz
     ↓
Check still_has_questions()
     ↓
    True
     ↓
Ask Question
     ↓
Increase Question Number
     ↓
Check Again
     ↓
    False
     ↓
End Quiz
```

---

## Incrementing the Question Number

Inside `next_question()`, the question number is usually increased.

Example:

```
def next_question(self):
    current_question = self.question_list[self.question_number]

    answer = input(
        f"Q.{self.question_number + 1}: "
        f"{current_question.text} "
        "(True/False): "
    )

    self.question_number += 1
```

This ensures the quiz moves to the next question.

---

## Complete Example

### QuizBrain Method

```
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

### Main Program

```
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
```

### Result

The quiz continues until every question has been asked.

---

## Why Keep Loop Logic in QuizBrain?

The `QuizBrain` class manages:

- Question progression
- Quiz state
- User interaction

Keeping quiz logic inside the class improves:

- Encapsulation
- Readability
- Maintainability

---

## Boolean Values and Loops

`still_has_questions()` returns a Boolean value.

### Possible Results

```
True
```

Continue looping.

```
False
```

Stop looping.

The `while` loop depends entirely on these values.

---

## Real-World Analogy

Imagine a teacher asking questions from a stack of flashcards.

### While Cards Remain

```
Ask another question.
```

### No Cards Remaining

```
Stop asking questions.
```

`still_has_questions()` acts like checking whether any flashcards are left.

---

## FAQs

### 1. Why use a while loop?

To keep asking questions until all questions have been answered.

Example:

```
while quiz.still_has_questions():
    quiz.next_question()
```

---

### 2. What does `still_has_questions()` return?

A Boolean value.

Possible outputs:

```
True
```

or

```
False
```

---

### 3. When does the loop stop?

The loop stops when all questions have been asked.

Condition:

```
self.question_number >= len(self.question_list)
```

---

### 4. Why compare with `len()`?

`len()` provides the total number of questions.

Example:

```
len(self.question_list)
```

This helps determine when the quiz should end.

---

### 5. What happens when `False` is returned?

The `while` loop immediately stops and the quiz ends.

Example:

```
while False:
```

The loop does not execute.

---

## Key Takeaways

- A `while` loop keeps the quiz running continuously.
- `still_has_questions()` checks whether questions remain.
- The method returns a Boolean value.
- `len()` determines the total number of questions.
- `question_number` tracks progress through the quiz.
- The quiz automatically ends when all questions have been asked.
- Boolean values control loop execution.
- Keeping loop logic inside `QuizBrain` improves design and maintainability.
- This structure creates smooth, continuous gameplay.