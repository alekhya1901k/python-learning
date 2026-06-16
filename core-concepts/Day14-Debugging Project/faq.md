**FAQs**

1. What is the first step in debugging?

Understanding and describing the problem clearly.

2. Why did the original code not print anything?

Because range(1, 20) stops at 19, so i == 20 never happens.

3. Is range() inclusive or exclusive?

The start value is included, but the stop value is excluded.

4. How do you include 20 in a range?

Use range(1, 21).

5. Why is describing the problem important?

Because fixing code without understanding the issue can create more bugs.

6. What does reproduce the bug mean?

It means making the bug happen again so we can study it.

7. What was the bug in the dice program?

The random number could become 6, but list index 6 does not exist.

8. What error does Python give for invalid list index?

IndexError.

9. Why does Python list indexing start at 0?

Python follows zero-based indexing, meaning the first item is at index 0.

10. How should random numbers be used with lists?

The random number should stay within valid index positions.

11. What does “play computer” mean?

It means manually tracing the code line by line.

12. Why did 1994 not work?

Because both conditions excluded 1994.

13. What is a boundary value?

A value at the edge of a condition, such as 1994.

14. What is the difference between < and <=?

< excludes the value. <= includes the value.

15. Why are boundary values important in debugging?

Many bugs happen at edge cases like first value, last value, minimum, or maximum.

16. What is a syntax error?

A mistake in code structure that prevents Python from running.

17. Why was indentation wrong?

The print() statement should be inside the if block.

18. Why do we use f-strings?

To insert variable values inside strings.

19. What does try/except do?

It catches errors and prevents the program from crashing.

20. What error happens if user enters text instead of number?

ValueError.

21. Why is print useful in debugging?

It shows the actual value of variables while the program runs.

22. What was the bug in this program?

The code used == instead of =.

23. What is the difference between = and ==?

= assigns a value. == checks equality.

24. Why was output wrong?

Because word_per_page remained 0.

25. Should debug print statements stay forever?

No. Use them while debugging, then remove unnecessary ones.

26. What is a debugger?

A tool that lets you pause and inspect code while it runs.

27. What is a breakpoint?

A marker where the program pauses during debugging.

28. What does Step Over do?

It executes the current line and moves to the next line.

29. What was the bug in the mutate function?

b_list.append(new_item) was outside the loop.

30. Why should append be inside the loop?

Because each calculated value should be added to the list.
