"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 3: File Handling
Learning Objective: Read from and write to files safely
"""

import os

# Writing to a file
print("=== Writing to Files ===")
filename = "student_data.txt"

# Method 1: Basic file writing
file = open(filename, "w")  # "w" for write mode
file.write("Student Records\n")
file.write("================\n")
file.write("Name: Alice, Grade: A\n")
file.write("Name: Bob, Grade: B\n")
file.close()  # Always close files!

print(f"Data written to {filename}")

# Method 2: Using 'with' statement (recommended)
with open(filename, "a") as file:  # "a" for append mode
    file.write("Name: Carol, Grade: A\n")
    file.write("Name: David, Grade: C\n")

print("Additional data appended")

# Reading from a file
print("\n=== Reading from Files ===")

# Method 1: Read entire file
with open(filename, "r") as file:  # "r" for read mode
    content = file.read()
    print("Full file content:")
    print(content)

# Method 2: Read line by line
print("Reading line by line:")
with open(filename, "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Method 3: Read all lines into a list
with open(filename, "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")

# Working with CSV-like data
print("\n=== Processing Structured Data ===")
csv_filename = "grades.csv"

# Create CSV data
students = [
    ["Name", "Math", "Science", "English"],
    ["Alice", "95", "88", "92"],
    ["Bob", "78", "85", "80"],
    ["Carol", "92", "90", "95"]
]

# Write CSV data
with open(csv_filename, "w") as file:
    for row in students:
        file.write(",".join(row) + "\n")

# Read and process CSV data
print("Grade Report:")
with open(csv_filename, "r") as file:
    lines = file.readlines()
    header = lines[0].strip().split(",")
    
    for line in lines[1:]:  # Skip header
        data = line.strip().split(",")
        name = data[0]
        grades = [int(grade) for grade in data[1:]]
        average = sum(grades) / len(grades)
        print(f"{name}: Average = {average:.1f}")

# Error handling with files
print("\n=== File Error Handling ===")
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: Permission denied!")
except Exception as e:
    print(f"Unexpected error: {e}")

# Check if file exists
if os.path.exists(filename):
    print(f"{filename} exists")
    # Get file size
    size = os.path.getsize(filename)
    print(f"File size: {size} bytes")

# Clean up - delete test files
try:
    os.remove(filename)
    os.remove(csv_filename)
    print("Test files cleaned up")
except:
    pass

"""
Example Output:
=== Writing to Files ===
Data written to student_data.txt
Additional data appended

=== Reading from Files ===
Full file content:
Student Records
================
Name: Alice, Grade: A
Name: Bob, Grade: B
Name: Carol, Grade: A
Name: David, Grade: C

Reading line by line:
Line 1: Student Records
Line 2: ================
Line 3: Name: Alice, Grade: A
Line 4: Name: Bob, Grade: B
Line 5: Name: Carol, Grade: A
Line 6: Name: David, Grade: C

Grade Report:
Alice: Average = 91.7
Bob: Average = 81.0
Carol: Average = 92.3

What you learned:
- File modes: "r" (read), "w" (write), "a" (append)
- Using 'with' statement for automatic file closing
- Different ways to read files: read(), readlines(), line by line
- Processing structured data (CSV format)
- Error handling with try/except for file operations
- os module for file system operations
- Always close files or use 'with' statement
"""