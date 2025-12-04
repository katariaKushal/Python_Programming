"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 3: Context Managers
Learning Objective: Create and use context managers for resource management
"""

import contextlib
import time

# Understanding the 'with' statement
print("=== Understanding 'with' Statement ===")

# Traditional file handling (not recommended)
def traditional_file_handling():
    """Example of manual resource management"""
    file = None
    try:
        file = open("test.txt", "w")
        file.write("Hello World")
    finally:
        if file:
            file.close()
            print("File closed manually")

# Using 'with' statement (recommended)
def context_manager_file_handling():
    """Example using context manager"""
    with open("test.txt", "w") as file:
        file.write("Hello World with context manager")
    # File is automatically closed here
    print("File closed automatically")

traditional_file_handling()
context_manager_file_handling()

# Custom context manager using class
print("\n=== Custom Context Manager (Class) ===")

class Timer:
    """Context manager to measure execution time"""
    
    def __init__(self, name="Operation"):
        self.name = name
    
    def __enter__(self):
        """Called when entering the 'with' block"""
        print(f"Starting {self.name}")
        self.start_time = time.time()
        return self  # Return self to be used as 'as' variable
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting the 'with' block"""
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"{self.name} completed in {duration:.4f} seconds")
        
        # Handle exceptions
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            return False  # Don't suppress the exception
        return True

# Using custom context manager
with Timer("Calculation") as timer:
    # Simulate some work
    result = sum(i**2 for i in range(100000))
    print(f"Calculation result: {result}")

# Context manager with exception handling
print("\n=== Context Manager with Exception ===")

try:
    with Timer("Error prone operation"):
        print("Starting operation...")
        raise ValueError("Something went wrong!")
        print("This won't be printed")
except ValueError as e:
    print(f"Caught exception: {e}")

# Context manager using contextlib
print("\n=== Context Manager with @contextmanager ===")

@contextlib.contextmanager
def database_connection():
    """Simulate database connection context manager"""
    print("Connecting to database...")
    connection = "DB_CONNECTION_OBJECT"  # Simulate connection
    
    try:
        yield connection  # This is what gets returned to 'as' variable
    finally:
        print("Closing database connection...")

# Using the contextlib-based context manager
with database_connection() as conn:
    print(f"Using connection: {conn}")
    print("Performing database operations...")

# Multiple context managers
print("\n=== Multiple Context Managers ===")

@contextlib.contextmanager
def log_operation(operation_name):
    """Context manager for logging operations"""
    print(f"[LOG] Starting: {operation_name}")
    try:
        yield
    finally:
        print(f"[LOG] Finished: {operation_name}")

# Using multiple context managers
with log_operation("File Processing"), open("test.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# Context manager for temporary changes
print("\n=== Temporary State Context Manager ===")

class TemporaryValue:
    """Context manager to temporarily change a value"""
    
    def __init__(self, obj, attr, temp_value):
        self.obj = obj
        self.attr = attr
        self.temp_value = temp_value
        self.original_value = None
    
    def __enter__(self):
        self.original_value = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.temp_value)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        setattr(self.obj, self.attr, self.original_value)

class Settings:
    """Example class with settings"""
    def __init__(self):
        self.debug_mode = False

settings = Settings()
print(f"Original debug mode: {settings.debug_mode}")

with TemporaryValue(settings, 'debug_mode', True):
    print(f"Temporary debug mode: {settings.debug_mode}")
    # Do something that needs debug mode

print(f"Restored debug mode: {settings.debug_mode}")

# Context manager for resource pooling
print("\n=== Resource Pool Context Manager ===")

class ResourcePool:
    """Simple resource pool implementation"""
    
    def __init__(self, resources):
        self.available = list(resources)
        self.in_use = []
    
    @contextlib.contextmanager
    def get_resource(self):
        """Get a resource from the pool"""
        if not self.available:
            raise RuntimeError("No resources available")
        
        resource = self.available.pop()
        self.in_use.append(resource)
        print(f"Acquired resource: {resource}")
        
        try:
            yield resource
        finally:
            self.in_use.remove(resource)
            self.available.append(resource)
            print(f"Released resource: {resource}")

# Using resource pool
pool = ResourcePool(["Resource1", "Resource2", "Resource3"])

with pool.get_resource() as resource:
    print(f"Using {resource} for important work")
    print(f"Available resources: {pool.available}")

print(f"Final available resources: {pool.available}")

# Cleanup test file
import os
try:
    os.remove("test.txt")
except:
    pass

"""
Example Output:
=== Understanding 'with' Statement ===
File closed manually
File closed automatically

=== Custom Context Manager (Class) ===
Starting Calculation
Calculation result: 333283335000
Calculation completed in 0.0156 seconds

=== Context Manager with Exception ===
Starting Error prone operation
Exception occurred: ValueError: Something went wrong!
Error prone operation completed in 0.0001 seconds
Caught exception: Something went wrong!

=== Context Manager with @contextmanager ===
Connecting to database...
Using connection: DB_CONNECTION_OBJECT
Performing database operations...
Closing database connection...

=== Multiple Context Managers ===
[LOG] Starting: File Processing
File content: Hello World with context manager
[LOG] Finished: File Processing

=== Temporary State Context Manager ===
Original debug mode: False
Temporary debug mode: True
Restored debug mode: False

What you learned:
- Context managers ensure proper resource cleanup
- __enter__ and __exit__ methods for custom context managers
- @contextlib.contextmanager decorator for simpler context managers
- Exception handling in context managers
- Multiple context managers in single 'with' statement
- Practical applications: file handling, database connections, temporary state changes
- Resource pooling with context managers
- yield in context managers returns the managed resource
"""