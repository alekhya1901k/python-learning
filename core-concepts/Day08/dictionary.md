1.Dictionaries
    
    Quick Short Notes
    1. A dictionary stores data in key:value pairs.
    2. Dictionaries are written using curly brackets {}.
        student = {
            "name": "Alex",
            "age": 12
        }
    3. Keys must be unique inside a dictionary.
        data = {
            "name": "Tom",
            "name": "John"
        }
        
        Output: {'name': 'John'}
    4. Values can be any data type:
        String
        Integer
        Float
        List
        Dictionary
        Boolean
    5. Dictionary items are accessed using keys.
        print(student["name"])
    6. Dictionaries are mutable.
        You can:
        Add items
        Update items
        Delete items
    7. Add a new item using a new key.
        student["grade"] = "A"
    8. Update existing values using the same key.
        student["age"] = 13
    9. Looping through a dictionary gives keys by default.
        for key in student:
            print(key)
    10. Use dictionary values for fast data lookup instead of long if-else conditions.
# -------------------- Example 1 – Creating and Accessing Dictionary --------------------

# Create a dictionary named 'fruits'
# Dictionaries store data in key:value pairs
fruits = {

    # Key      : Value
    "apple": "red",
    "banana": "yellow",
    "grapes": "purple"
}

# Access the value using its key
# "banana" is the key
# Its value is "yellow"
print(fruits["banana"])

# Output: yellow

# -------------------- Example 2 – Adding and Updating Data --------------------

# Create an empty dictionary named 'car'
# Empty dictionaries are created using {}
car = {}

# Add a new key:value pair to the dictionary
# Key = "brand"
# Value = "Toyota"
car["brand"] = "Toyota"

# Add another key:value pair
# Key = "year"
# Value = 2024
car["year"] = 2024

# Print the dictionary after adding values
print(car)

# Output: {'brand': 'Toyota', 'year': 2024}

# Update the value of the existing key "year"
# Old value: 2024
# New value: 2025
car["year"] = 2025

# Print the updated dictionary
print(car)

# Output: {'brand': 'Toyota', 'year': 2025}
