"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 2: Input and Output
Learning Objective: Learn to get user input and display formatted output
"""

# Getting input from user
print("=== Personal Information Collector ===")
name = input("Enter your name: ")
age = input("Enter your age: ")

# Convert string input to integer for calculations
age = int(age)
birth_year = 2024 - age

# Different ways to display output
print("Hello,", name)
print("You are", age, "years old")
print("You were born in", birth_year)

# Formatted string (f-string) - modern Python way
print(f"Summary: {name} is {age} years old and was born in {birth_year}")

# String formatting with .format()
print("Alternative: {} is {} years old".format(name, age))

"""
Example Input/Output:
Enter your name: John
Enter your age: 20

Hello, John
You are 20 years old
You were born in 2004
Summary: John is 20 years old and was born in 2004
Alternative: John is 20 years old

What you learned:
- input() function always returns a string
- Converting strings to numbers with int(), float()
- Different ways to format output: comma separation, f-strings, .format()
- Basic arithmetic operations
"""