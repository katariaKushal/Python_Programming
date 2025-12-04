"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 4: Loops (for and while)
Learning Objective: Repeat code execution using loops
"""

# For loop with range
print("=== Counting with For Loop ===")
for i in range(1, 6):  # 1 to 5
    print(f"Count: {i}")

# For loop with list
print("\n=== Iterating through a list ===")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop
print("\n=== Countdown with While Loop ===")
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1  # Same as countdown = countdown - 1
print("Blast off! 🚀")

# Loop with user input
print("\n=== Number Guessing Game ===")
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You win!")

# Loop control: break and continue
print("\n=== Even Numbers Only ===")
for num in range(1, 11):
    if num % 2 != 0:  # If odd number
        continue      # Skip to next iteration
    print(f"Even number: {num}")
    if num == 8:
        break        # Exit loop early

"""
Example Output:
=== Counting with For Loop ===
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

=== Iterating through a list ===
I like apple
I like banana
I like orange
I like grape

=== Even Numbers Only ===
Even number: 2
Even number: 4
Even number: 6
Even number: 8

What you learned:
- for loops for iterating over sequences
- range() function for generating number sequences
- while loops for condition-based repetition
- Loop control with break and continue
- Modulo operator (%) for finding remainders
"""