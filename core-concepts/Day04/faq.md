1. What is a pseudorandom number?

A pseudorandom number is a number generated using algorithms that imitate randomness.

2. Why are PRNGs called “pseudo” random?

Because the numbers are mathematically generated and not truly random.

3. What is a seed in PRNG?

A seed is the starting value used by the random generator.

4. What happens if the same seed is used?

The same sequence of random numbers is generated.

5. Is Python random module secure?

No. For security or cryptography, use the secrets module instead.

6. Why do we import the random module?

To access random number generation functions.

7. Which function generates random integers?

random.randint()

8. Which function generates random floating numbers?

random.random() and random.uniform()

9. Can random module generate negative numbers?

Yes, if negative ranges are provided.

10. Where is the random module commonly used?

Games, simulations, password generation, and testing.

11. Is the upper limit included in randint()?

Yes.

12. What type of value does randint() return?

Integer.

13. Difference between randint() and random()?

randint() gives integers, random() gives floats.

14. Can randint() generate duplicate values?

Yes.

15. What happens if start value is greater than end value?

Python raises a ValueError.

16. What is a Python module?

A Python file containing reusable code.

17. Why are modules important?

They improve maintainability and reusability.

18. How do you import a module?

Using the import keyword.

19. Difference between module and package?

A package is a collection of modules.

20. Can we create custom modules?

Yes.

Important FAQs

21. What range does random.random() use?

0.0≤random.random()<1.0

22. What does uniform() do?

Generates random floating-point numbers in a given range.

23. Does uniform() include the upper bound?

It may include it depending on floating-point rounding.

24. How can you generate random floats between 0 and 5?

random.random() * 5

25. Difference between random() and uniform()?

random() gives 0–1 range only, uniform() allows custom ranges.

26. Are Python lists mutable?

Yes.

27. Which brackets are used in lists?

Square brackets [].

28. Can lists store different data types?

Yes.

29. Are duplicate items allowed?

Yes.

30. What is the difference between list and tuple?

Lists are mutable; tuples are immutable.

31. What does index -1 represent?

Last element.

32. Why use negative indexing?

To access elements from the end.

33. Does negative indexing work in strings?

Yes.

34. Can negative indexing cause errors?

Yes, if index exceeds range.

35. Which is easier for last item access?

Negative indexing.

36. Why can lists be modified?

Because lists are mutable.

37. Can tuples be modified similarly?

No.

38. What syntax is used?

list[index] = value

39. Does modification create a new list?

No.

40. What error occurs for invalid indexes?

IndexError

41. Where does append() add items?

At the end.

42. Does append() return the modified list?

No, it returns None.

43. Can append() add lists?

Yes.

44. Difference between append() and extend()?

append() adds one item; extend() adds multiple items.

45. Is append() efficient?

Yes, generally efficient for end insertions.

46. What does len() return?

Number of items.

47. Why does IndexError occur?

Because index is outside valid range.

48. What is the last valid index?

Last Valid Index=len(list)−1

49. Can len() work on strings?

Yes.

50. How can IndexError be avoided?

Check length before accessing indexes.

51. What is a nested list?

A list containing other lists.

52. Why are nested lists useful?

For storing structured/tabular data.

53. How do you access nested items?

Using multiple indexes.

54. What does food[0][1] mean?

First list, second item.

55. Where are nested lists used?

Matrices, game boards, tables, and data analysis.
