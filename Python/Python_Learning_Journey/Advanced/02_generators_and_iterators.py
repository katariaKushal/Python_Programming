"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 2: Generators and Iterators
Learning Objective: Create memory-efficient iterators and generators
"""

# Basic generator function
print("=== Basic Generator ===")

def count_up_to(max_count):
    """Generator that counts from 1 to max_count"""
    count = 1
    while count <= max_count:
        yield count  # yield makes this a generator
        count += 1

# Using the generator
counter = count_up_to(5)
print(f"Generator object: {counter}")

for num in counter:
    print(f"Count: {num}")

# Generator expressions
print("\n=== Generator Expressions ===")

# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in range(10)]
print(f"List: {squares_list}")

# Generator expression (creates items on demand)
squares_gen = (x**2 for x in range(10))
print(f"Generator: {squares_gen}")

# Convert generator to list to see values
print(f"Generator values: {list(squares_gen)}")

# Memory efficiency demonstration
print("\n=== Memory Efficiency ===")

def fibonacci_generator():
    """Generate fibonacci numbers infinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 fibonacci numbers
fib_gen = fibonacci_generator()
fibonacci_numbers = []
for _ in range(10):
    fibonacci_numbers.append(next(fib_gen))

print(f"First 10 Fibonacci numbers: {fibonacci_numbers}")

# Generator with send() method
print("\n=== Generator with send() ===")

def accumulator():
    """Generator that accumulates sent values"""
    total = 0
    while True:
        value = yield total  # Receive value and yield current total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # Prime the generator
print(f"Initial total: {acc.send(10)}")
print(f"After adding 5: {acc.send(5)}")
print(f"After adding 3: {acc.send(3)}")

# Custom iterator class
print("\n=== Custom Iterator Class ===")

class CountDown:
    """Custom iterator that counts down from a number"""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Using custom iterator
countdown = CountDown(5)
for num in countdown:
    print(f"Countdown: {num}")

# Generator for file processing
print("\n=== File Processing Generator ===")

def read_large_file(filename):
    """Generator to read large files line by line"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return

# Create a test file
test_filename = "test_data.txt"
with open(test_filename, 'w') as f:
    for i in range(5):
        f.write(f"Line {i+1}: This is test data\n")

# Process file with generator
print("Processing file with generator:")
for line in read_large_file(test_filename):
    print(f"Read: {line}")

# Pipeline of generators
print("\n=== Generator Pipeline ===")

def numbers(max_num):
    """Generate numbers from 1 to max_num"""
    for i in range(1, max_num + 1):
        yield i

def squares(nums):
    """Square each number from input generator"""
    for num in nums:
        yield num ** 2

def even_only(nums):
    """Filter only even numbers"""
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators together
pipeline = even_only(squares(numbers(10)))
result = list(pipeline)
print(f"Even squares from 1-10: {result}")

# Generator with exception handling
print("\n=== Generator with Exception Handling ===")

def safe_divide_generator(numbers, divisor):
    """Generator that safely divides numbers"""
    for num in numbers:
        try:
            yield num / divisor
        except ZeroDivisionError:
            yield f"Cannot divide {num} by zero"

numbers_list = [10, 20, 30, 40]
results = list(safe_divide_generator(numbers_list, 2))
print(f"Division results: {results}")

zero_results = list(safe_divide_generator(numbers_list, 0))
print(f"Division by zero results: {zero_results}")

# Clean up test file
import os
try:
    os.remove(test_filename)
except:
    pass

"""
Example Output:
=== Basic Generator ===
Generator object: <generator object count_up_to at 0x...>
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

=== Generator Expressions ===
List: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Generator: <generator object <genexpr> at 0x...>
Generator values: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

=== Memory Efficiency ===
First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

=== Generator with send() ===
Initial total: 10
After adding 5: 15
After adding 3: 18

=== Generator Pipeline ===
Even squares from 1-10: [4, 16, 36, 64, 100]

What you learned:
- Generator functions with yield keyword
- Generator expressions vs list comprehensions
- Memory efficiency of generators (lazy evaluation)
- next() function and StopIteration exception
- Generator methods: send(), throw(), close()
- Custom iterator classes with __iter__ and __next__
- Generator pipelines for data processing
- Infinite generators and their applications
- Exception handling in generators
"""