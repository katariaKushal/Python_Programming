"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 3: Conditional Statements
Learning Objective: Make decisions in code using if, elif, else
"""

# Simple grade calculator
print("=== Grade Calculator ===")
score = int(input("Enter your test score (0-100): "))

# if-elif-else chain
if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Average performance"
elif score >= 60:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Please study more"

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Comment: {message}")

# Nested conditions
print("\n=== Age Category ===")
age = int(input("Enter your age: "))

if age >= 0:
    if age < 13:
        category = "Child"
    elif age < 20:
        category = "Teenager"
    elif age < 60:
        category = "Adult"
    else:
        category = "Senior"
    print(f"You are a {category}")
else:
    print("Invalid age!")

"""
Example Input/Output:
Enter your test score (0-100): 85
Score: 85
Grade: B
Comment: Good job!

Enter your age: 16
You are a Teenager

What you learned:
- if, elif, else statements for decision making
- Comparison operators: >=, <, ==, !=
- Nested if statements
- Logical flow and condition evaluation order
"""