# Creating a module named `mymodule.py`

def add(a, b):
    """Function to add two numbers"""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers"""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b

def divide(a, b):
    """Function to divide two numbers"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b
