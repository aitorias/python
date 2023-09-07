### Object-Oriented Programming

OOP (Object-oriented Progrmaming) is a flexible, powerful paradigm where **classes represent and define concepts**, while **objects are instances of classes**.

Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we're creating an object which is an instance of the list class, which represents the concept of a list. Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.

## Attributes

the attributes are characteristics associated to a type.

## Classes

Examples:

```python
class Example:
    attribute_1 = ""
    attribute_2 = ""

class_instance = Apple()
class_instance.attribute_1 = "test"
class_instance.attribute_2 = "test 2"

print(class_instnce.attribute_1) # Should print "test"
```

## Composition

Composition is where one class makes use of code contained in another class and are related but there is no inheritance between them.

Examples:

```python
class Example:
    def __init__(self):
        self.types = {}
    def add_type(self, type):
        self.types[type.name] = type
    def total_types(self):
        result = 0
        for type in self.types.values():
            result += type.size
        return result
```

## Docstring

A string literal which appears as the first expression in a class, function or module. While ignored when the suite is executed, it is recognized by the compiler and put into the \_\_doc\_\_ attribute of the enclosing class, function or module. Since it is available via introspection, it is the canonical place for documentation of the object.

Example:

```python
def function_1(parameter_1, parameter_2):
    """This is a docstring"""
    return parameter_1, parameter_2

help(function1)

# Help on function function_1 in module __main__:

# function_1(parameter_1, parameter_2)
#   This is a docstring
```

## Functions

### Built-in functions

#### dir()

Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

If the object has a method named \_\_dir\_\_(), this method will be called and must return the list of attributes. This allows objects that implement a custom \_\_getattr\_\_() or \_\_getattribute\_\_() function to customize the way dir() reports their attributes.

If the object does not provide \_\_dir\_\_(), the function tries its best to gather information from the object’s \_\_dict\_\_ attribute, if defined, and from its type object. The resulting list is not necessarily complete and may be inaccurate when the object has a custom \_\_getattr\_\_().

The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

If the object is a module object, the list contains the names of the module’s attributes.

If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.

Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.

Always initialize mutable attributes in the constructor.

Examples:

```python
dir("")
# Should print
# ['__add__', '__class__', '__contains__', '__delattr__', ...]
```

#### help()

Invoke the built-in help system or the documentation for the corresponding class. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.

Press **q** to quit the help.

## Inheritance

Inheritance is the relationships between objects, grouping together similar concepts and reducing code duplication.

Examples:

```python
class Example:
    """This is a parent clss"""
    def __init__(self, parameter_1, parameter_2):
        self.attribute_1 = parameter_1
        self.attribute_2 = parameter_2

class InheritedExample(Example):
    """This is an inherited class of Example clss"""
    pass

instance_1 = InheritedExample("A", "B")
print(instance_1.attribute_1) # Should print "A"
print(instance_1.attribute_2) # Should print "B"
```

## Methods

The methods are the functions associated to a type that operate on the attributes of a specific instance of a class.

Examples:

```python
class Example:
    attribute_1 = "test"
    attribute_2 = 0
    def method_1(self):
        print(f"This is a {self.attribute_1} example")
    def method_2(self):
        return self.attribute_2 * 2

instance_1 = Example()
print(instance_1.method_1("second test")) # Should print "This is a second test example"

instance_1.attribute_2 = 2
print(instance_1.method_2()) # Should print 4
```

## Modules

Modules are used to organize functions, classes and other data together in a structured way. Modules are used using the **import** keyword

Examples:

```python
import random

print(random.randint(1,10)) # Should print a number between 1 and 10


import datetime

now = datetime.datetime.now()

print(type(now)) # Should print <class 'datetime.datetime'>
print(now) # Should print a date with this format: YEAR-MONTH-DAY HOURS:MINUTES:SECONDS.XXXXXX
print(now.year) # Should print the year: 2023
print(now + datetime.timedelta(days=28)) # Should print the current exact date and time plus 28 days
```

### Specil Methods

#### \_\_init()\_\_ (Constructor)

Constructor is the method that's called when you call the name of the class using \_\_init()\_\_.

Examples:

```python
class Example:
    def __init__(self, parameter_1, parameter_2):
        self.attribute_1 = parameter_1
        self.attribute_2 = parameter_2

instance_1 = Example("A", "B")
print(instance_1.attribute_1) # Should print "A"
print(instance_1.attribute_2) # Should print "B"
```

#### \_\_str()\_\_

Compute the "informal" or nicely printable string representation of an object. The return value must be a string object. This method allows us to define how an instance of an object will be printed when it's passed to the print() function. If an object doesn't have this special method defined, it will wind up using the default representation, which will print the position of the object in memory.

Example:

```python
class Example:
    def __init__(self, attribute_1, attribute_2):
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
    def __str__(self)
        return f"This is a string representation of an object. It's attributes are:\nattribute 1: {self.attribute_1}\nattribute 2: {self.attribute_2}"

instance_1 = Example("A", "B")
print(instance_1)
# Should print
# This is a string representation of an object. It's attributes are:
# attribute 1: "A"
# attribute 2: "B"
```

## Objects

## self

self is a special parameter which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot notation.
