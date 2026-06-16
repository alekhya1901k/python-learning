5.Use Print
    
    10 Quick Summary Points
    1. print() helps reveal hidden values.
    2. It is useful for checking variables during execution.
    3. In debugging, print intermediate values.
    4. The original code used == instead of =.
    5. = assigns a value.
    6. == compares two values.
    7. word_per_page stayed 0.
    8. So total words became pages * 0.
    9. Use print statements to confirm values.
    10. Remove extra debug prints after fixing the issue.

# Buggy Code

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Debug Version
word_per_page = 0

pages = int(input("Number of pages: "))
print(f"Pages entered: {pages}")

word_per_page == int(input("Number of words per page: "))
print(f"Words per page: {word_per_page}")

total_words = pages * word_per_page
print(total_words)

This shows word_per_page is still 0.

# Fixed Code
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

total_words = pages * word_per_page

print(total_words)