"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 3: Design Patterns
Learning Objective: Implement common design patterns in Python
"""

from abc import ABC, abstractmethod
import copy

# Singleton Pattern
print("=== Singleton Pattern ===")

class DatabaseConnection:
    """Singleton class ensuring only one database connection exists"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.connection_string = "database://localhost:5432"
            self.is_connected = False
            self._initialized = True
            print("Database connection initialized")
    
    def connect(self):
        if not self.is_connected:
            self.is_connected = True
            print(f"Connected to {self.connection_string}")
    
    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            print("Disconnected from database")

# Test Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance? {db1 is db2}")
db1.connect()

# Factory Pattern
print("\n=== Factory Pattern ===")

class Animal(ABC):
    """Abstract base class for animals"""
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def get_type(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def get_type(self):
        return "Dog"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
    def get_type(self):
        return "Cat"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"
    
    def get_type(self):
        return "Bird"

class AnimalFactory:
    """Factory class to create animals"""
    
    @staticmethod
    def create_animal(animal_type):
        """Create animal based on type"""
        animals = {
            "dog": Dog,
            "cat": Cat,
            "bird": Bird
        }
        
        animal_class = animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Test Factory Pattern
factory = AnimalFactory()
animals = []

for animal_type in ["dog", "cat", "bird"]:
    animal = factory.create_animal(animal_type)
    animals.append(animal)
    print(f"{animal.get_type()} says: {animal.make_sound()}")

# Observer Pattern
print("\n=== Observer Pattern ===")

class Subject:
    """Subject that notifies observers of changes"""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """Add an observer"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        """Remove an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers of state change"""
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        """Change state and notify observers"""
        self._state = state
        print(f"Subject state changed to: {state}")
        self.notify()
    
    def get_state(self):
        return self._state

class Observer(ABC):
    """Abstract observer class"""
    
    @abstractmethod
    def update(self, subject):
        pass

class EmailNotifier(Observer):
    """Observer that sends email notifications"""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"EmailNotifier {self.name}: Received update - {subject.get_state()}")

class SMSNotifier(Observer):
    """Observer that sends SMS notifications"""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"SMSNotifier {self.name}: SMS alert - {subject.get_state()}")

# Test Observer Pattern
news_agency = Subject()

email_notifier = EmailNotifier("John")
sms_notifier = SMSNotifier("Alice")

news_agency.attach(email_notifier)
news_agency.attach(sms_notifier)

news_agency.set_state("Breaking News: Python 4.0 Released!")
news_agency.set_state("Weather Alert: Heavy Rain Expected")

# Strategy Pattern
print("\n=== Strategy Pattern ===")

class PaymentStrategy(ABC):
    """Abstract payment strategy"""
    
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        return f"Paid ${amount} using PayPal account {self.email}"

class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number):
        self.account_number = account_number
    
    def pay(self, amount):
        return f"Paid ${amount} via bank transfer from account {self.account_number}"

class ShoppingCart:
    """Shopping cart that uses different payment strategies"""
    
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        total = sum(price for item, price in self.items)
        if self.payment_strategy:
            result = self.payment_strategy.pay(total)
            print(f"Checkout complete: {result}")
            return result
        else:
            print("No payment method selected")
            return None

# Test Strategy Pattern
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)

# Try different payment strategies
strategies = [
    CreditCardPayment("1234567890123456"),
    PayPalPayment("user@example.com"),
    BankTransferPayment("ACC123456789")
]

for strategy in strategies:
    cart.set_payment_strategy(strategy)
    cart.checkout()

# Decorator Pattern (different from Python decorators)
print("\n=== Decorator Pattern ===")

class Coffee(ABC):
    """Abstract coffee class"""
    
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_cost(self):
        pass

class SimpleCoffee(Coffee):
    """Basic coffee implementation"""
    
    def get_description(self):
        return "Simple Coffee"
    
    def get_cost(self):
        return 2.00

class CoffeeDecorator(Coffee):
    """Base decorator class"""
    
    def __init__(self, coffee):
        self._coffee = coffee
    
    def get_description(self):
        return self._coffee.get_description()
    
    def get_cost(self):
        return self._coffee.get_cost()

class MilkDecorator(CoffeeDecorator):
    """Milk decorator"""
    
    def get_description(self):
        return self._coffee.get_description() + ", Milk"
    
    def get_cost(self):
        return self._coffee.get_cost() + 0.50

class SugarDecorator(CoffeeDecorator):
    """Sugar decorator"""
    
    def get_description(self):
        return self._coffee.get_description() + ", Sugar"
    
    def get_cost(self):
        return self._coffee.get_cost() + 0.25

class WhipDecorator(CoffeeDecorator):
    """Whipped cream decorator"""
    
    def get_description(self):
        return self._coffee.get_description() + ", Whipped Cream"
    
    def get_cost(self):
        return self._coffee.get_cost() + 0.75

# Test Decorator Pattern
coffee = SimpleCoffee()
print(f"{coffee.get_description()}: ${coffee.get_cost():.2f}")

# Add decorators
coffee = MilkDecorator(coffee)
print(f"{coffee.get_description()}: ${coffee.get_cost():.2f}")

coffee = SugarDecorator(coffee)
print(f"{coffee.get_description()}: ${coffee.get_cost():.2f}")

coffee = WhipDecorator(coffee)
print(f"{coffee.get_description()}: ${coffee.get_cost():.2f}")

# Command Pattern
print("\n=== Command Pattern ===")

class Command(ABC):
    """Abstract command class"""
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Light:
    """Receiver class"""
    
    def __init__(self, location):
        self.location = location
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.location} light is ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.location} light is OFF")

class LightOnCommand(Command):
    """Command to turn light on"""
    
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    """Command to turn light off"""
    
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
    
    def undo(self):
        self.light.turn_on()

class RemoteControl:
    """Invoker class"""
    
    def __init__(self):
        self.commands = {}
        self.last_command = None
    
    def set_command(self, slot, command):
        self.commands[slot] = command
    
    def press_button(self, slot):
        if slot in self.commands:
            command = self.commands[slot]
            command.execute()
            self.last_command = command
    
    def press_undo(self):
        if self.last_command:
            self.last_command.undo()

# Test Command Pattern
living_room_light = Light("Living Room")
bedroom_light = Light("Bedroom")

living_room_on = LightOnCommand(living_room_light)
living_room_off = LightOffCommand(living_room_light)
bedroom_on = LightOnCommand(bedroom_light)

remote = RemoteControl()
remote.set_command(1, living_room_on)
remote.set_command(2, living_room_off)
remote.set_command(3, bedroom_on)

remote.press_button(1)  # Turn on living room light
remote.press_button(3)  # Turn on bedroom light
remote.press_undo()     # Undo last command

"""
Example Output:
=== Singleton Pattern ===
Database connection initialized
Same instance? True
Connected to database://localhost:5432

=== Factory Pattern ===
Dog says: Woof!
Cat says: Meow!
Bird says: Tweet!

=== Observer Pattern ===
Subject state changed to: Breaking News: Python 4.0 Released!
EmailNotifier John: Received update - Breaking News: Python 4.0 Released!
SMSNotifier Alice: SMS alert - Breaking News: Python 4.0 Released!

=== Strategy Pattern ===
Checkout complete: Paid $1029.98 using Credit Card ending in 3456
Checkout complete: Paid $1029.98 using PayPal account user@example.com
Checkout complete: Paid $1029.98 via bank transfer from account ACC123456789

=== Decorator Pattern ===
Simple Coffee: $2.00
Simple Coffee, Milk: $2.50
Simple Coffee, Milk, Sugar: $2.75
Simple Coffee, Milk, Sugar, Whipped Cream: $3.50

=== Command Pattern ===
Living Room light is ON
Bedroom light is ON
Bedroom light is OFF

What you learned:
- Singleton pattern for ensuring single instance
- Factory pattern for object creation
- Observer pattern for event notification
- Strategy pattern for interchangeable algorithms
- Decorator pattern for adding functionality
- Command pattern for encapsulating requests
- Abstract base classes for defining interfaces
- When and how to apply different design patterns
- Benefits of loose coupling and high cohesion
"""