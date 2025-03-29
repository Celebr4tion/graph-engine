"""
Example module with nested functions and classes for testing instrumentation.

This module provides various constructs to demonstrate function call tracking,
including nested functions, class methods, and closures.
"""

def outer_function(value):
    """
    A function containing a nested inner function.
    
    Args:
        value: Any value to be processed
    """
    print(f"Outer function called with {value}")
    
    def inner_function(inner_value):
        """
        A nested function inside outer_function.
        
        Args:
            inner_value: Value to process
        """
        result = f"Processed: {inner_value}"
        print(result)
        return result
    
    # Call the inner function
    return inner_function(value)


class Person:
    """
    A simple Person class with methods for demonstration.
    """
    
    def __init__(self, name, age):
        """
        Initialize a Person object.
        
        Args:
            name: The person's name
            age: The person's age
        """
        self.name = name
        self.age = age
        print(f"Created person: {name}, age {age}")
    
    def greet(self):
        """
        Method to greet the person.
        """
        def generate_greeting(name):
            """
            Nested function to generate a greeting.
            
            Args:
                name: The name to include in the greeting
            """
            return f"Hello, {name}!"
        
        greeting = generate_greeting(self.name)
        print(greeting)
        return greeting
    
    def celebrate_birthday(self):
        """
        Method to celebrate a birthday and increment age.
        """
        self.age += 1
        message = f"Happy birthday! {self.name} is now {self.age} years old."
        print(message)
        return message


def create_counter():
    """
    Create a counter function using a closure.
    
    Returns:
        A function that increments and returns a counter.
    """
    count = 0
    
    def increment():
        """
        Increment the counter and return the new value.
        
        Returns:
            The current count after incrementing
        """
        nonlocal count
        count += 1
        return count
    
    return increment 