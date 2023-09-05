# Dictionaries

Dictionaries are sometimes found in other languages as "associative memories" or "associative arrays". They re mutable, and, unlike sequences, which are indexed by a range of numbers, dictionaries are **indexed by keys**, which can be any **immutable** type; **strings and numbers** can always be **keys**. Tuples can be used as keys if they contain **only strings, numbers, or tuples**; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You **can't use lists as keys**, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

Dictionaries are a **set of {key: value} pairs**, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

Performing `list(d)` on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use `sorted(d)` instead). To check whether a single key is in the dictionary, use the in keyword.

Examples:

```python
x = {}
print(type(x)) # Should print <clss 'dict'>

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts) # Should print {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts["txt"]) # Should print 14

# If a key does not exists, it will be added at the end of the dictionary
file_counts["doc"] = 8
print(file_counts) # Should print {"jpg": 10, "txt": 14, "csv": 2, "py": 23, "doc": 8}

# If a key exists, its value will be replaced and updated
file_counts["csv"] = 17
print(file_counts) # Should print {"jpg": 10, "txt": 14, "csv": 17, "py": 23, "doc": 8}
```

## Iterating

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)
    # Should print
    # jpg
    # txt
    # csv
    # py
```

## Keywords

### del

Remove elements from the dictionary.

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
del file_counts["py"]
print(file_counts) # Should print {"jpg": 10, "txt": 14, "csv": 17}
```

### in

Check if the key exists in the dictionary.

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print("jpg" in file_counts) # Should print True
print("html" in file_counts) # Should print False
```

## Methods

### .clear()

Deletes all items from a dictionary.

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

print(file_counts.clear()). # Should print None
```

### .copy()

Makes a copy of a dictionary.

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

file_copy = file_counts.copy()

print(file_copy). # Should print {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
```

### .get()

Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

print(file_counts.get("jpg")). # Should print 10


pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}

print(pet_dictionary.get("dogs", 3)) # Should print ['Yorkie', 'Collie', 'Bulldog']
```

### .keys()

Return a new view of the dictionary's keys.

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

print(file_counts.keys()). # Should print dict_keys(["jpg", "txt", "csv", "py"])
```

### .items()

Return a new view of the dictionary's items ((key, value) pairs).

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

for extension, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, extension))
    # Should print
    # "There are 10 files with the .jpg extension"
    # "There are 14 files with the .txt extension"
    # "There are 2 files with the .csv extension"
    # "There are 23 files with the .py extension"
```

### .update()

Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

Accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

file_copy = {}

print(file_copy) # Should print {}

file_copy.update(file_counts)

print(file_copy). # Should print {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
```

### .values()

Return a new view of the dictionary's values.

An equality comparison between one `dict.values()` view and another will always return `False`. This also applies when comparing `dict.values()` to itself:

Examples:

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

print(file_counts.values()). # Should print dict_values([10, 14, 2, 23])

for value in file_counts.values():
    print(value)
    # Should print
    # 10
    # 14
    # 2
    # 23
```
