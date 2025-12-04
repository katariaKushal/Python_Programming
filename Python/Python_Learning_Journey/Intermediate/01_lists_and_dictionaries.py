"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 1: Lists and Dictionaries
Learning Objective: Master Python's most important data structures
"""

# Lists - ordered, mutable collections
print("=== Working with Lists ===")
fruits = ["apple", "banana", "orange"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("grape")          # Add to end
fruits.insert(1, "mango")       # Insert at index 1
print(f"After adding: {fruits}")

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing

# List slicing
print(f"First 3 fruits: {fruits[:3]}")
print(f"Last 2 fruits: {fruits[-2:]}")

# List methods
fruits.remove("banana")         # Remove by value
popped = fruits.pop()          # Remove and return last item
print(f"After removal: {fruits}")
print(f"Popped item: {popped}")

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Dictionaries - key-value pairs
print("\n=== Working with Dictionaries ===")
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print(f"Student info: {student}")
print(f"Name: {student['name']}")
print(f"Subjects: {student['subjects']}")

# Adding/updating dictionary items
student["email"] = "john@email.com"
student["age"] = 21
print(f"Updated student: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# Iterating through dictionary
print("\nStudent details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Nested data structures
classroom = {
    "teacher": "Ms. Smith",
    "students": [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Carol", "grade": "A"}
    ]
}

print(f"\nClassroom: {classroom['teacher']}")
for student in classroom["students"]:
    print(f"- {student['name']}: {student['grade']}")

"""
Example Output:
=== Working with Lists ===
Original list: ['apple', 'banana', 'orange']
After adding: ['apple', 'mango', 'banana', 'orange', 'grape']
First fruit: apple
Last fruit: grape
First 3 fruits: ['apple', 'mango', 'banana']
After removal: ['apple', 'mango', 'orange']
Popped item: grape
Squares: [1, 4, 9, 16, 25]

=== Working with Dictionaries ===
Student info: {'name': 'John', 'age': 20, 'grade': 'A', 'subjects': ['Math', 'Science', 'English']}
Name: John
Subjects: ['Math', 'Science', 'English']

What you learned:
- List operations: append, insert, remove, pop, slicing
- List comprehensions for creating new lists
- Dictionary creation and access
- Dictionary methods: keys(), values(), items()
- Nested data structures (lists in dictionaries)
- Iterating through dictionaries
"""