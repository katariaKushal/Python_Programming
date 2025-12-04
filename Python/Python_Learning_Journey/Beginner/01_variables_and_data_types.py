"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 1: Variables and Data Types
Learning Objective: Understand Python's basic data types and variable assignment
"""

# Variables are containers for storing data values
name = "Alice"          # String (text)
age = 25               # Integer (whole number)
height = 5.6           # Float (decimal number)
is_student = True      # Boolean (True/False)

# Print variables and their types
print("Name:", name, "- Type:", type(name))
print("Age:", age, "- Type:", type(age))
print("Height:", height, "- Type:", type(height))
print("Is Student:", is_student, "- Type:", type(is_student))

# Variables can be reassigned
age = 26
print("Updated Age:", age)

# Multiple assignment
x, y, z = 1, 2, 3
print("x =", x, "y =", y, "z =", z)

"""
Example Output:
Name: Alice - Type: <class 'str'>
Age: 25 - Type: <class 'int'>
Height: 5.6 - Type: <class 'float'>
Is Student: True - Type: <class 'bool'>
Updated Age: 26
x = 1 y = 2 z = 3

What you learned:
- How to create variables in Python
- Python's main data types: str, int, float, bool
- Variables are dynamically typed (type can change)
- Multiple assignment in one line
"""