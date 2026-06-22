# Day 14 Project: Higher Lower Game – Quick Notes

# 1. Project Overview

### Quick Summary Points

1. The game compares two Instagram accounts.
2. Player guesses which account has more followers.
3. Account data is stored as dictionaries inside a list.
4. Random accounts are selected using `random.choice()`.
5. Account details are formatted before displaying.
6. User enters either `A` or `B`.
7. Follower counts are compared internally.
8. Correct guesses increase the score.
9. Wrong guesses end the game.
10. The game runs repeatedly using a `while` loop.

### Example

**A:** Cristiano Ronaldo (215M)

**B:** Taylor Swift (131M)

Answer: **A**

---

# 2. Data Structure (game_data.py)

### Quick Summary Points

1. Data is stored as a list.
2. Each item is a dictionary.
3. Dictionary keys are name, follower_count, description, country.
4. Each dictionary represents one account.
5. Easy to access using keys.
6. Supports random selection.
7. Stores related information together.
8. Flexible and scalable.
9. Real-world dataset simulation.
10. Used throughout the game.

### Example

```python
{
    "name": "Instagram",
    "follower_count": 346,
    "description": "Social media platform",
    "country": "United States"
}
```

---

# 3. format_data() Function

### Quick Summary Points

1. Receives one account dictionary.
2. Extracts name.
3. Extracts description.
4. Extracts country.
5. Creates readable text.
6. Hides follower count.
7. Improves user experience.
8. Prevents repetitive code.
9. Returns formatted string.
10. Used before displaying accounts.

### Example

Input:

```python
{
"name":"NASA",
"description":"Space agency",
"country":"United States"
}
```

Output:

```text
NASA, a Space agency, from United States
```

---

# 4. check_answer() Function

### Quick Summary Points

1. Checks user guess.
2. Receives follower counts.
3. Compares A and B.
4. Returns True or False.
5. Uses Boolean logic.
6. Separates game logic.
7. Improves code readability.
8. Avoids duplicate comparisons.
9. Simplifies main loop.
10. Core decision-making function.

### Example

```python
check_answer("a", 215, 131)
```

Output:

```python
True
```

---

# 5. Random Account Selection

### Quick Summary Points

1. Uses `random.choice()`.
2. Picks account randomly.
3. Makes gameplay unpredictable.
4. Keeps game interesting.
5. Selects Account A.
6. Selects Account B.
7. Prevents same sequence.
8. Uses game data list.
9. Provides variety.
10. Essential for replayability.

### Example

```python
account = random.choice(data)
```

---

# 6. While Loop Game Flow

### Quick Summary Points

1. Controls game repetition.
2. Runs while answer is correct.
3. Stops after wrong guess.
4. Uses Boolean variable.
5. Updates accounts each round.
6. Displays new comparison.
7. Takes user input.
8. Checks answer.
9. Updates score.
10. Ends gracefully.

### Example

```python
while game_should_continue:
```

---

# 7. Score Keeping

### Quick Summary Points

1. Score starts at 0.
2. Correct answer adds 1.
3. Wrong answer ends game.
4. Score shown after every round.
5. Uses integer variable.
6. Tracks user performance.
7. Encourages competition.
8. Simple implementation.
9. Easy to maintain.
10. Common game feature.

### Example

```python
score += 1
```

---

# 8. Preventing Duplicate Accounts

### Quick Summary Points

1. A and B should not be identical.
2. Comparison becomes meaningless otherwise.
3. Uses equality check.
4. Random account regenerated.
5. Improves fairness.
6. Avoids confusion.
7. Keeps game logical.
8. Ensures unique comparisons.
9. Increases quality.
10. Common validation step.

### Example

```python
if account_a == account_b:
    account_b = random.choice(data)
```

---

# Interview FAQs

### 1. Why is a list of dictionaries used in this project?

A list stores multiple records, while dictionaries store related data as key-value pairs.

---

### 2. Why does `format_data()` return a string instead of printing?

Returning allows the value to be reused anywhere in the program.

---

### 3. Why is `random.choice()` used?

To randomly select accounts and make the game different every time.

---

### 4. What does `check_answer()` return?

It returns a Boolean value (`True` or `False`).

---

### 5. Why use a `while` loop instead of a `for` loop?

Because the number of rounds is unknown and depends on user performance.

---

### 6. What is the purpose of `score += 1`?

It increments the score by one after every correct answer.

---

### 7. Why check if `account_a == account_b`?

To prevent comparing the same account against itself.

---

### 8. What programming concepts are demonstrated in this project?

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Random Module
* Boolean Logic
* User Input
* Variable Scope
* Return Values

---

# 10 Key Concepts Learned

1. Functions
2. Return Statements
3. Lists
4. Dictionaries
5. Nested Data Structures
6. Random Module
7. While Loops
8. Conditional Statements
9. Boolean Values
10. Game Logic Design
