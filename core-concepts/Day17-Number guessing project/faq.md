## Interview FAQs

### 1. Why do we use `random.randint(1, 100)`?

It generates a random integer between 1 and 100, including both 1 and 100.

### 2. Why are `EASY_LEVEL_TURNS` and `HARD_LEVEL_TURNS` written in uppercase?

Uppercase variable names usually represent constants. These values are not expected to change during the program.

### 3. Why does `check_answer()` return `turns - 1`?

Because every wrong guess should reduce the number of remaining attempts by one.

### 4. Why do we use a `while` loop?

The game must continue until either the user guesses correctly or runs out of attempts.

### 5. What is the purpose of `return` inside the game?

`return` immediately exits the function. Here, it stops the game when the user loses.

### 6. Why is `guess = 0` written before the loop?

It gives `guess` an initial value so the loop condition `guess != answer` can be checked safely.

### 7. What happens if the user enters text instead of a number?

The program will crash with a `ValueError`. A better version should use input validation.

### 8. Why do we separate code into functions?

Functions make the code easier to read, test, reuse, and debug.

### 9. What is one weakness in this code?

The difficulty input is not fully validated. Anything other than `"easy"` becomes hard mode.

### 10. How can this project be improved?

Add input validation, replay option, better error handling, and a visible answer only for debugging.

[1]: https://appbrewery.github.io/python-day12-demo/ "Demo"
