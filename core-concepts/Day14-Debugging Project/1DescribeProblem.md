1.Describe the Problem

    10 Quick Summary Points
    1. Before fixing code, first understand what the code is supposed to do.
    2. Read the code line by line.
    3. Identify the expected output.
    4. Identify the actual output.
    5. Compare expected vs actual behavior.
    6. Check loop ranges carefully.
    7. range(1, 20) starts at 1 and stops before 20.
    8. So i == 20 will never become true.
    9. The bug is not in the if; it is in the loop range.
    10. Fix the range to include 20.

Example:

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem:

# 1. What is the for loop doing?
# The for loop counts from 1 to 20.

# 2. When is the function meant to print "You got it"?
# When i becomes 20.

# 3. What are your assumptions about the value of i?
# I assumed i would reach 20, but range(1, 20) stops at 19.
# Changing it to range(1, 21) allows i to reach 20.


