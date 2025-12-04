"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 1: Decorators
Learning Objective: Understand and create decorators to modify function behavior
"""

import time
import functools

# Basic decorator concept
print("=== Basic Decorator ===")

def my_decorator(func):
    """A simple decorator that adds functionality to a function"""
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    """Function decorated with my_decorator"""
    print("Hello!")

say_hello()

# Decorator with arguments
print("\n=== Decorator with Arguments ===")

def timing_decorator(func):
    """Decorator to measure function execution time"""
    @functools.wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function(n):
    """A function that takes some time to execute"""
    total = 0
    for i in range(n):
        total += i * i
    return total

result = slow_function(100000)
print(f"Result: {result}")

# Decorator with parameters
print("\n=== Parameterized Decorator ===")

def repeat(times):
    """Decorator factory that repeats function execution"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    """Function that will be repeated"""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

final_result = greet("Alice")

# Class-based decorator
print("\n=== Class-based Decorator ===")

class CountCalls:
    """Decorator class to count function calls"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"10 + 7 = {add_numbers(10, 7)}")
print(f"Total calls: {add_numbers.count}")

# Multiple decorators
print("\n=== Multiple Decorators ===")

def bold(func):
    """Decorator to make output bold"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic(func):
    """Decorator to make output italic"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

@bold
@italic
def format_text(text):
    """Function to format text"""
    return text.upper()

print(format_text("hello world"))

# Practical decorator example: Caching
print("\n=== Caching Decorator ===")

def memoize(func):
    """Decorator to cache function results"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        
        print(f"Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate fibonacci number (inefficient without caching)"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10) = {fibonacci(10)}")
print(f"Fibonacci(10) = {fibonacci(10)}")  # Should use cache

"""
Example Output:
=== Basic Decorator ===
Something before the function
Hello!
Something after the function

=== Decorator with Arguments ===
slow_function took 0.0156 seconds
Result: 333283335000

=== Parameterized Decorator ===
Hello, Alice!
Hello, Alice!
Hello, Alice!

=== Class-based Decorator ===
Call #1 to add_numbers
5 + 3 = 8
Call #2 to add_numbers
10 + 7 = 17
Total calls: 2

=== Multiple Decorators ===
***HELLO WORLD***

What you learned:
- Decorator syntax with @ symbol
- Creating decorators that modify function behavior
- Using *args and **kwargs for flexible decorators
- functools.wraps to preserve function metadata
- Parameterized decorators (decorator factories)
- Class-based decorators with __call__ method
- Stacking multiple decorators
- Practical applications: timing, caching, logging
- Decorator execution order (bottom to top)
"""