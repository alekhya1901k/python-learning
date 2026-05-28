FAQs – Dictionaries
1. What is a dictionary in Python?

A dictionary is a collection of key:value pairs used to store related data.

2. Why are dictionaries important?

Dictionaries provide:

Fast data access
Organized storage
Easy updates
Better readability
3. What is the difference between a list and a dictionary?
Feature	List	Dictionary
Access	Index	Key
Structure	Ordered values	Key:value pairs
Example	fruits[0]	student["name"]
4. Can dictionary values be duplicated?

Yes.

data = {
    "a": 10,
    "b": 10
}
5. Can dictionary keys be duplicated?

No. Duplicate keys overwrite old values.

6. What happens if a key does not exist?

Python raises a KeyError.

student["marks"]
7. Can dictionaries store different data types together?

Yes.

person = {
    "name": "Alex",
    "age": 12,
    "is_student": True
}
8. How do you loop through dictionary values?
for key in student:
    print(student[key])

9. What is nesting in Python?

Nesting means placing one data structure inside another data structure.

10. Why do we use nested data structures?

They help store complex and grouped information in an organized way.

Example:

Student details
Travel history
Product catalogs
11. How do you access nested list items?

Use multiple indexes.

my_list[2][1]
12. How do you access values inside nested dictionaries?

Use multiple keys.

data["Germany"]["cities_visited"]
13. What is the biggest challenge with nested structures?

Incorrect indexing or keys can cause:

IndexError
KeyError
14. Where are nested dictionaries commonly used?

They are heavily used in:

JSON responses
APIs
Configuration files
Real-world backend systems
15. What is the difference between list nesting and dictionary nesting?
Type	Access Method
List	Index
Dictionary	Key
16. How can nested data become difficult?

Deep nesting can reduce readability and make debugging harder if structure is not clear.