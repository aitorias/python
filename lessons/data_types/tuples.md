# Tuples

A tuple consists of a number of values or sequences of elements of any type, separated by commas that are **immutable**, and usually contain a heterogeneous sequence of elements that are accessed via **unpacking** or **indexing**. The order inside the tuples is important and **matters**.

We can use tuples to return value of functions.

Examples:

```python
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result)) # Should print <class `tuple`>
print(result) # Should print (1, 23, 20)
```

## Unpacking

Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence.

Examples:

```python
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
hours, minutes, seconds = result
print(hours, minutes, seconds) # Should print (1, 23, 20)
```

## Functions

### enumerate()

Return an enumerate object. Iterable must be a sequence, an iterator, or some other object which supports iteration. The \_\_next\_\_() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

Examples:

```python
list1 = ["One", "Two", "Three"]
for index, value in enumerate(list1):
    print("{} - {}".format(index + 1, value))
    # Should print:
    # 1 - One
    # 2 - Two
    # 3 - Three
```
