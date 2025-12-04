"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 4: Error Handling and Exceptions
Learning Objective: Handle errors gracefully and create robust programs
"""

# Basic try-except structure
print("=== Basic Error Handling ===")

def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Please provide numbers only!")
        return None

# Test the function
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

# Multiple exception types
print("\n=== Handling Multiple Exceptions ===")

def process_user_input():
    """Get and process user input with error handling"""
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative!")
        
        # Simulate accessing a list
        categories = ["Child", "Teen", "Adult", "Senior"]
        if age < 13:
            category = categories[0]
        elif age < 20:
            category = categories[1]
        elif age < 65:
            category = categories[2]
        else:
            category = categories[3]
            
        return f"You are in the {category} category"
        
    except ValueError as e:
        return f"Invalid input: {e}"
    except IndexError:
        return "Error: Category not found"
    except Exception as e:
        return f"Unexpected error: {e}"

# Uncomment to test interactively
# print(process_user_input())

# Using finally block
print("\n=== Using Finally Block ===")

def read_file_safely(filename):
    """Read file with proper cleanup"""
    file = None
    try:
        print(f"Attempting to open {filename}")
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
    finally:
        # This always runs, even if an exception occurs
        if file:
            file.close()
            print("File closed successfully")
        print("Cleanup completed")

# Test with non-existent file
result = read_file_safely("nonexistent.txt")

# Custom exceptions
print("\n=== Custom Exceptions ===")

class InsufficientFundsError(Exception):
    """Custom exception for banking operations"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance ${balance}, Attempted ${amount}")

class BankAccount:
    """Simple bank account class with error handling"""
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        """Withdraw money with validation"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def deposit(self, amount):
        """Deposit money with validation"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

# Test custom exceptions
account = BankAccount(100)
print(f"Initial balance: ${account.balance}")

try:
    print(account.deposit(50))
    print(account.withdraw(30))
    print(account.withdraw(200))  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
except ValueError as e:
    print(f"Invalid amount: {e}")

# Assertion for debugging
print("\n=== Using Assertions ===")

def calculate_average(numbers):
    """Calculate average with assertion"""
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    
    return sum(numbers) / len(numbers)

# Test assertions
try:
    print(f"Average of [1,2,3,4,5]: {calculate_average([1,2,3,4,5])}")
    print(f"Average of empty list: {calculate_average([])}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

"""
Example Output:
=== Basic Error Handling ===
10 / 2 = 5.0
Error: Cannot divide by zero!
10 / 0 = None
Error: Please provide numbers only!
10 / 'a' = None

=== Using Finally Block ===
Attempting to open nonexistent.txt
Error: nonexistent.txt not found
Cleanup completed

=== Custom Exceptions ===
Initial balance: $100
Deposited $50. New balance: $150
Withdrew $30. New balance: $120
Transaction failed: Insufficient funds: Balance $120, Attempted $200

=== Using Assertions ===
Average of [1,2,3,4,5]: 3.0
Assertion failed: List cannot be empty

What you learned:
- try/except blocks for handling specific exceptions
- Multiple exception handling with different except blocks
- finally block for cleanup code that always runs
- Creating custom exception classes
- Using assertions for debugging and validation
- Exception hierarchy and catching parent exceptions
- Raising exceptions with raise keyword
- Best practices for error handling in functions
"""