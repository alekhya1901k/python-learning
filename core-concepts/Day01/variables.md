1. Variables store data values for later use.

2. = is assignment operator.

3. Variables can store strings, numbers, lists, etc.

4. Python variables are dynamically typed.

5. len() calculates length.

6. Variables reduce code repetition.
 Example:
    
    a. name = "Alekhya" (Variable is 'name' & with '=' "Alekhya" value is assigned to the variable)

    b. username = input("What is your name? ") #Taking input from user assigning to username
       length = len(username) #using len() function, finding no:of characters in the "username" variable and assigning to "length" variable.
       print(length) #printing length.
    c. One-Line Version:
       print(len(input("What is your name? ")))

7. Variable Naming Rules:
    Rules for Naming Variables:
        Correct Rules
            Use meaningful names
            Use lowercase and underscores if needed
            Start with letters or underscore
         Avoid:
            Spaces
            Starting with numbers
            Special characters
            Python keywords
Examples: 
    Good Examples:
        user_name = "Alekhya"
        age = 10
        city_name = "Dallas"
    Bad Examples:
        2name = "Sam"
        user-name = "Sam"
        print = "Hello"