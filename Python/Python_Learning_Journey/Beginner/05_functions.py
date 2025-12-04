"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 5: Functions
Learning Objective: Create reusable code blocks with functions
"""

# Simple function without parameters
def greet():
    """Function to display a greeting message"""
    print("Hello! Welcome to Python functions!")

# Function with parameters
def greet_person(name, age):
    """Function that greets a specific person"""
    print(f"Hello {name}! You are {age} years old.")

# Function with return value
def add_numbers(a, b):
    """Function that adds two numbers and returns the result"""
    result = a + b
    return result

# Function with default parameters
def introduce(name, hobby="reading"):
    """Function with a default parameter value"""
    return f"Hi, I'm {name} and I enjoy {hobby}."

# Function that returns multiple values
def calculate_circle(radius):
    """Calculate area and circumference of a circle"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

# Using the functions
print("=== Function Examples ===")

# Call simple function
greet()

# Call function with parameters
greet_person("Alice", 25)

# Use return value
sum_result = add_numbers(10, 15)
print(f"10 + 15 = {sum_result}")

# Default parameter
print(introduce("Bob"))
print(introduce("Carol", "painting"))

# Multiple return values
area, circumference = calculate_circle(5)
print(f"Circle with radius 5: Area = {area:.2f}, Circumference = {circumference:.2f}")

# Local vs Global variables
global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

scope_example()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error!

"""
Example Output:
=== Function Examples ===
Hello! Welcome to Python functions!
Hello Alice! You are 25 years old.
10 + 15 = 25
Hi, I'm Bob and I enjoy reading.
Hi, I'm Carol and I enjoy painting.
Circle with radius 5: Area = 78.54, Circumference = 31.42
Inside function: I'm global
Inside function: I'm local
Outside function: I'm global

What you learned:
- How to define functions with def keyword
- Parameters and arguments
- Return statements and return values
- Default parameter values
- Multiple return values with tuple unpacking
- Variable scope (local vs global)
- Docstrings for function documentation
"""