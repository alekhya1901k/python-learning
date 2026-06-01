2.Nested Lists and Dictionaries
    
    Quick Short Notes
    1. Nesting means placing one data structure inside another.
    2. A list can be stored inside a dictionary.
        data = {
            "fruits": ["apple", "banana"]
        }
    3. A dictionary can be stored inside another dictionary.
    4. Nested structures help organize complex data.
    5. Access nested list items using:
        Dictionary key
        List index
    6. Access deeply nested values step-by-step.
    7. List indexing starts from 0.
    8. Nested dictionaries are commonly used in:
        APIs
        JSON data
        Databases
        Real-world applications
    9. Complex programs often combine:
        Lists
        Dictionaries
        Tuples
    10. Proper indentation and structure improve readability in nested data.
# -------------------- Example 1 – Nested List Inside Dictionary --------------------

# Create a dictionary named 'travel_log'
# Each key stores a list as its value
travel_log = {

    # Key = "France"
    # Value = list of cities
    "France": ["Paris", "Lille", "Dijon"],

    # Key = "Germany"
    # Value = another list of cities
    "Germany": ["Berlin", "Hamburg"]
}

# Access data step by step:
#
# travel_log["France"]
# gives:
# ["Paris", "Lille", "Dijon"]
#
# [1] accesses the item at index 1
# Index 1 = "Lille"
print(travel_log["France"][1])

# Output: Lille

# -------------------- Example 2 – Nested Dictionary --------------------

# Create a dictionary containing another dictionary
travel_log = {

    # Key = "Germany"
    # Value = nested dictionary
    "Germany": {

        # Key = "cities_visited"
        # Value = list of cities
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],

        # Key = "total_visits"
        # Value = integer
        "total_visits": 5
    }
}

# Step-by-step access:
#
# travel_log["Germany"]
# gives the nested dictionary
#
# ["cities_visited"]
# gives:
# ["Berlin", "Hamburg", "Stuttgart"]
#
# [2] accesses index 2 from the list
# Index 2 = "Stuttgart"
print(travel_log["Germany"]["cities_visited"][2])

# Output: Stuttgart


# -------------------- Example 3 – Nested List --------------------

# Create a nested list
# The third element itself is another list
nested_list = ["A", "B", ["C", "D"]]

# Step-by-step access:
#
# nested_list[2]
# gives:
# ["C", "D"]
#
# [1] accesses the second element
# Index 1 = "D"
print(nested_list[2][1])

# Output: D
