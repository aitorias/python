# Data types
Classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)

Is not possible to mix two differents data types, like:

```python
print(1 + 2) # Output: 3

print ("1" + "2") # Output: "12"

print(1 + "2") # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## Boolean
One of two possible states: either true or false

Examples:

```python
variable_1 = false
variable_2 = true
```

## Float
Represents real numbers (numbers with a fractional part). Examples:
1.1, 2.5, 3.33;

## Integer
Whole numbers without a fraction. Examples:
1, 2, 10, 100, 100;

## None
A special data type in Python used to indicate that things are empty or that they returned nothing.

Examples:

```python
def functionA(parameter):
  print("parameter: " + parameter)

result = functionA("test")
print(result) # Output: None
```

## String
Array of bytes representing unicode characters. It can be written between single or doyuble quotes. Examples:
"String"; "1234"; "A1 B2";

## How to know the data type?
Using the `type()` function. Example:

```python
print(type(1.1)) # Output: <class 'float'>

print(type(1)) # Output: <class 'int'>

print(type("a")) # Output: <class 'str'>
```

## Implicit conversion
The interpreter automatically converts one data type into another.

Example:

```python
# Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

print("Value:",new_number)
print("Data Type:",type(new_number))

# Output
# Value: 124.23
# Data Type: <class 'float'>
```

# Explicit conversion
Manually conversion from one data type to another using a function for the data type we want to convert to.
- `float()`: Converts a value (usually an integer) to a float data type
- `int()`: Converts a value (usually a float) to an integer data type
- `str()`: Converts a value (often numeric) to a string data type

Examples:

```python
variable1 = 1
variable2 = 2
result = variable1 - variable2
print("Result: " + str(result))

# output
"Result: -1
```