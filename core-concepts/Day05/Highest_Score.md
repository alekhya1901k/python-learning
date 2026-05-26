2.Highest Score
    
    Quick Short Notes (10 Points)
    1. Python provides built-in numeric functions like sum(), max(), and min().
    2. sum() calculates the total of all numbers.
    3. max() returns the largest value.
    4. min() returns the smallest value.
    5. Loops can manually recreate these functions.
    6. A variable is used to track the current highest value.
    7. Conditionals compare values during iteration.
    8. Lists store multiple values together.
    9. Looping through scores is common in analytics and reports.
    10. Understanding internal logic improves programming skills.

# -------------------- Using sum() --------------------

# Create a list named student_scores
# It stores marks scored by students
student_scores = [180, 124, 165, 173, 189]

# sum() adds all numbers inside the list
# 180 + 124 + 165 + 173 + 189 = 831
total_score = sum(student_scores)

# Print the total score
print(total_score)

# Output:
# 831



# -------------------- How sum() Works Internally --------------------

# Create a list of student scores
student_scores = [180, 124, 165]

# Create a variable named total
# It starts with 0 because no scores are added yet
total = 0

# Loop through each score in the list
for score in student_scores:

    # Add the current score to total
    # Same as: total = total + score
    total += score

# Print the final total after the loop finishes
print(total)

# Output:
# 469



# -------------------- Highest Score Without max() --------------------

# Create a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64]

# Create a variable to store the highest score
# It starts with 0 because scores are positive numbers here
highest_score = 0

# Loop through each score one by one
for score in student_scores:

    # Check if the current score is greater than highest_score
    if score > highest_score:

        # If current score is greater, update highest_score
        highest_score = score

# Print the highest score found after checking all scores
print(highest_score)

# Output:
# 91

    Step-by-Step Logic
1. Start with highest_score = 0
2. Take first score from list.
3. Compare with current highest.
4. If bigger, replace highest value.
5. Continue until loop ends.
6. Final value becomes highest score.
