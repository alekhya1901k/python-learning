# Quiz Project Part 5: Scoring

## Quick Short Notes

- User answers must be validated.
- Score starts at zero.
- Correct answers increase score.
- A `check_answer()` method handles validation.
- User input is compared with the correct answer.
- Lowercase comparison avoids case issues.
- Feedback is shown after every question.
- Current score is displayed continuously.
- Final score is displayed at the end.
- Scoring improves user engagement.

---

## Why Add Scoring?

A quiz becomes more useful when users can track their performance.

Scoring helps:

- Measure progress
- Increase engagement
- Provide feedback
- Encourage learning

The quiz should check answers and update the score accordingly.

---

## Storing the Score

The score is stored inside the `QuizBrain` class.

Example:

```
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
```

### Explanation

| Attribute | Purpose |
|------------|---------|
| `question_number` | Tracks current question |
| `score` | Tracks correct answers |
| `question_list` | Stores all questions |

---

## The `check_answer()` Method

```
def check_answer(self, user_answer, correct_answer):

    if user_answer.lower() == correct_answer.lower():
        self.score += 1
```

### Purpose

Validate the user's answer and update the score if correct.

---

## Understanding the Logic

### User Input

```
True
```

### Correct Answer

```
true
```

Without conversion:

```
True == true
```

Result:

```
False
```

Because Python is case-sensitive.

---

### Using `lower()`

```
user_answer.lower()
```

Converts:

```
"True"
```

to:

```
"true"
```

Now compare:

```
"true" == "true"
```

Result:

```
True
```

The answer is accepted regardless of capitalization.

---

## Updating the Score

When the answer is correct:

```
self.score += 1
```

Example:

### Before

```
score = 2
```

### Correct Answer

```
self.score += 1
```

### After

```
score = 3
```

---

## Showing Feedback

After checking the answer, feedback can be displayed.

Example:

```
if user_answer.lower() == correct_answer.lower():
    print("You got it right!")
else:
    print("That's wrong.")
```

This helps users learn immediately.

---

## Showing the Correct Answer

Example:

```
print(f"The correct answer was: {correct_answer}")
```

Benefits:

- Reinforces learning
- Clarifies mistakes
- Improves user understanding

---

## Displaying the Current Score

```
print(f"Score: {self.score}")
```

Example Output:

```
Score: 4
```

Users can track their progress throughout the quiz.

---

## Complete Example

```
def check_answer(self, user_answer, correct_answer):

    if user_answer.lower() == correct_answer.lower():
        print("You got it right!")
        self.score += 1
    else:
        print("That's wrong.")

    print(f"The correct answer was: {correct_answer}")
    print(f"Score: {self.score}")
```

---

## Integrating with `next_question()`

Example:

```
def next_question(self):

    current_question = self.question_list[self.question_number]

    answer = input(
        f"Q.{self.question_number + 1}: "
        f"{current_question.text} "
        "(True/False): "
    )

    self.check_answer(
        answer,
        current_question.answer
    )

    self.question_number += 1
```

### Flow

1. Display question.
2. Collect user input.
3. Check answer.
4. Update score.
5. Move to next question.

---

## Quiz Flow with Scoring

```text
Display Question
        ↓
Collect Answer
        ↓
Check Answer
        ↓
Correct?
   ↓         ↓
 Yes         No
   ↓         ↓
Increase     Keep
 Score       Score
   ↓
Show Feedback
   ↓
Display Score
   ↓
Next Question
```

---

## Final Score

At the end of the quiz:

```
print(
    f"You completed the quiz. "
    f"Your final score was "
    f"{self.score}/{len(self.question_list)}"
)
```

Example Output:

```
You completed the quiz.
Your final score was 8/10
```

---

## Why Keep Scoring Inside QuizBrain?

The `QuizBrain` class controls:

- Question progression
- User interaction
- Score tracking
- Answer validation

Keeping these responsibilities together improves:

- Encapsulation
- Maintainability
- Readability

---

## FAQs

### 1. Why convert answers to lowercase?

To avoid case sensitivity issues.

Example:

```
"True"
"TRUE"
"true"
```

All become:

```
"true"
```

---

### 2. Where is score stored?

Inside the `QuizBrain` class.

Example:

```
self.score = 0
```

---

### 3. When is score updated?

After a correct answer.

Example:

```
self.score += 1
```

---

### 4. Why show the correct answer?

To provide learning opportunities and immediate feedback.

Example:

```
The correct answer was: True
```

---

### 5. What is the purpose of `check_answer()`?

To validate user responses and update the score.

Responsibilities:

- Compare answers
- Display feedback
- Update score

---

## Key Takeaways

- User answers should be validated after every question.
- Score begins at zero.
- Correct answers increase the score.
- `check_answer()` handles answer validation.
- `lower()` prevents case sensitivity problems.
- Feedback improves the learning experience.
- Current score should be displayed continuously.
- Final score summarizes quiz performance.
- Scoring increases engagement and motivation.
- `QuizBrain` manages both quiz flow and score tracking.