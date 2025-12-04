"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              Kataria Kushal                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Program 2: Classes and Objects (OOP Basics)
Learning Objective: Understand Object-Oriented Programming fundamentals
"""

# Basic class definition
class Dog:
    """A simple class representing a dog"""
    
    # Class variable (shared by all instances)
    species = "Canis lupus"
    
    # Constructor method
    def __init__(self, name, age, breed):
        """Initialize a new dog instance"""
        self.name = name      # Instance variables
        self.age = age
        self.breed = breed
        self.is_hungry = True
    
    # Instance methods
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def eat(self):
        """Feed the dog"""
        if self.is_hungry:
            self.is_hungry = False
            return f"{self.name} is eating. Nom nom!"
        else:
            return f"{self.name} is not hungry right now."
    
    def get_info(self):
        """Return dog information"""
        return f"{self.name} is a {self.age}-year-old {self.breed}"

# Creating objects (instances)
print("=== Creating Dog Objects ===")
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

# Using object methods
print(dog1.bark())
print(dog2.bark())
print(dog1.get_info())
print(dog2.get_info())

# Accessing and modifying attributes
print(f"\n{dog1.name} is hungry: {dog1.is_hungry}")
print(dog1.eat())
print(f"{dog1.name} is hungry: {dog1.is_hungry}")

# Class variables
print(f"\nSpecies: {Dog.species}")
print(f"Dog1 species: {dog1.species}")

# More advanced class with inheritance
class ServiceDog(Dog):
    """A service dog class that inherits from Dog"""
    
    def __init__(self, name, age, breed, service_type):
        # Call parent constructor
        super().__init__(name, age, breed)
        self.service_type = service_type
        self.is_working = False
    
    def start_work(self):
        """Start working"""
        self.is_working = True
        return f"{self.name} is now working as a {self.service_type} dog"
    
    def bark(self):
        """Override parent method"""
        if self.is_working:
            return f"{self.name} is working and stays quiet"
        else:
            return super().bark()  # Call parent method

# Using inheritance
print("\n=== Service Dog Example ===")
service_dog = ServiceDog("Rex", 4, "Labrador", "Guide")
print(service_dog.get_info())
print(service_dog.bark())
print(service_dog.start_work())
print(service_dog.bark())

"""
Example Output:
=== Creating Dog Objects ===
Buddy says Woof!
Max says Woof!
Buddy is a 3-year-old Golden Retriever
Max is a 5-year-old German Shepherd

Buddy is hungry: True
Buddy is eating. Nom nom!
Buddy is hungry: False

Species: Canis lupus
Dog1 species: Canis lupus

=== Service Dog Example ===
Rex is a 4-year-old Labrador
Rex says Woof!
Rex is now working as a Guide dog
Rex is working and stays quiet

What you learned:
- Class definition with class keyword
- Constructor method (__init__)
- Instance variables vs class variables
- Instance methods and self parameter
- Object creation and method calling
- Inheritance with super()
- Method overriding
- Basic OOP principles: encapsulation and inheritance
"""