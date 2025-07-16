# Iterables and Iterators

# Any object you can loop over is iterable:
for char in "marcos":
    print(char)

# Sorted example with string
print(sorted("python"))

# List comprehension example: double numbers 1 to 10
doubled = [i * 2 for i in range(1, 11)]
print(doubled)

"""
An iterable is an object that returns an iterator via the __iter__ method.
An iterator returns values one at a time via the __next__ method.
"""

# Fibonacci sequence as an iterator class
class Fibonacci:
    def __init__(self, max_value):
        self.max = max_value

    def __iter__(self):
        self.x, self.y = 1, 1
        return self

    def __next__(self):
        fib = self.x
        if fib > self.max:
            raise StopIteration
        self.x, self.y = self.y, self.x + self.y
        return fib

fib_sequence = Fibonacci(100)
for num in fib_sequence:
    print(num)

# Generators: lazy evaluation using yield
def fib_generator(max_value):
    x, y = 1, 1
    while x < max_value:
        yield x  # Pause here and resume on next() call
        x, y = y, x + y

gen = fib_generator(100)
print(next(gen))  # Get next Fibonacci number lazily

# Iterate through generator
for value in gen:
    print(value)

# Decorators
"""
A decorator is a design pattern that allows you to extend behavior of functions
without permanently modifying them. They wrap a function and add functionality.
"""

def modify(func):
    def wrapper(a, b):
        # Replace original function behavior with subtraction
        return a - b
    return wrapper

@modify
def add(a, b):
    return a + b

print(add(10, 20))  # Outputs  -10 due to decorator

# Decorator with conditional logic
def even_adder(func):
    def wrapper(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return "No even numbers"
    return wrapper

@even_adder
def subtract(a, b):
    return a - b

print(subtract(2, 3))  # 5
print(subtract(1, 3))  # No even numbers

# Simple decorator that prints before function call
def simple_decorator(func):
    def wrapper():
        print("Decorator says hello!")
        func()
    return wrapper

@simple_decorator
def greet():
    print("Original greet function.")

greet()

# Metaclasses
"""
Metaclasses are the 'classes of classes'.
They control the creation of classes.
"""

# Basic class
class MyClass:
    var = True

print(MyClass)  # <class '__main__.MyClass'>
obj = MyClass()
print(obj.var)  # True

# Equivalent creation via type()
MyClassType = type("MyClassType", (), {"var": True})
print(MyClassType)
obj2 = MyClassType()
print(obj2.var)

# Checking class and metaclass
print(type(10))  # <class 'int'>
print(type(int))  # <class 'type'>

# Custom metaclass example
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name}")
        print(f"Bases: {bases}")
        print(f"Attributes: {attrs}")
        return super().__new__(cls, name, bases, attrs)

class Parent:
    pass

class Child(Parent, metaclass=MyMeta):
    pass

print(type(Child))  # <class '__main__.MyMeta'>
