1. What is a for loop in Python?

A for loop repeats code for every item in a sequence.

2. Why are loops important?

They reduce repetitive code and improve efficiency.

3. What does the loop variable do?

It stores the current item during each iteration.

Example:

for fruit in fruits:

fruit stores one fruit at a time.

4. Why is indentation important in loops?

Indentation decides which statements belong to the loop block.

5. Can for loops work with strings?

Yes.

for letter in "Python":
    print(letter)

6. Can we stop a loop early?

Yes, using break.

for i in range(5):
    if i == 3:
        break
    print(i)

7. Difference between for loop and while loop?

for loop → used when iterations are known.
while loop → used when condition-based repetition is needed.

8. What does sum() do?

It adds all numbers in a sequence.

9. What does max() do?

It returns the largest value from a list.

10. Why learn manual logic if built-in functions exist?

It improves problem-solving and interview skills.

11. How does the highest score logic work?

The program compares each number with the current highest value.

12. What is the role of conditionals here?

Conditionals decide whether the current value should replace the highest value.

13. What happens if the list has negative numbers?

Initialize using first list value instead of 0.

Example:

highest = student_scores[0]

14. Can we find the smallest value similarly?

Yes.

lowest = scores[0]

for score in scores:
    if score < lowest:
        lowest = score

15. What is range() in Python?

range() generates a sequence of numbers.

16. Why does range(1,10) stop at 9?

Because the upper limit is excluded.

17. What is the third parameter in range()?

It represents step size.

Example:

range(1, 10, 2)

18. Can range() generate reverse numbers?

Yes.

for i in range(10, 0, -1):
    print(i)

19. Why is range() memory efficient?

It generates values only when needed.

20. Difference between list and range?

List stores actual values.
Range generates values dynamically.

21. What is the Gauss formula used for?

To quickly calculate the sum of consecutive numbers.
