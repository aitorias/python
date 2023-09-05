# Lists

Lists are sequences of elements of ny type and are used to store multiple items in a single variable. They are **mutable**, that means that it is possible to modify the content of the list. Their elements are usually **homogeneous** and are accessed by **iterating** over the list.

## List comprehension

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it

Examples:

```python
# Transform this code in list comprehension:
multiples_of_7 = []
for x in range(1,11):
    multiples_of_7.append(x*7)

print(multiples_of_7) # Should print [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# With list comprehension:
multiples_of_7 = [x*7 for x in range(1,11)]

print(multiples_of_7) # Should print [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Transform this code in list comprehension:
squares = []
for x in range(10):
    squares.append(x**2)

print(squares) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With list comprehension:
squares = [x**2 for x in range(10)]

print(squares) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Print the length of the strings:
coding_languages = ["Python", "C++", "Java", ".NET"]
lengths = [len(coding_language) for coding_language in languages]
print(lengths) # Should print [6, 3, 4, 4]

# Print all numbers that are divisible by 3 between 0 and 100
divisible_by_3 = [x for x in range(0,101) if x%3 == 0]
print(divisible_by_3) # Should print [0, 3, 6, 9, 12, 15, 18, 21, 24, ...]
```

## Indexing

Examples:

```python
list1 = ["This", "is", "a", "list"]
print(list1[0]) # Should print "This"
print(list1[1:3]) # Should print ["is", "a"]
print(list1[:2]) # Should print ["This", "is"]
print(list1[2:]) # Should print ["a", "list"]
```

## Iterating

Examples:

```python
list1 = ["One", "Two", "Three", "Four"]
characters = 0
for element in list1:
    characters += len(element)

print("Total characters: {} | Average length: {}".format(characters, characters/len(list1))) # Should print Total characters: 15 | Average length: 3.75
```

## Mutation

Examples:

```python
list1 = ["This", "is", "a", "list"]
list1[1] = "isn't"
print(list1) # Should print ["This", "isn't", "a", "list"]
```

## Functions

### len()

Function to return the number of elements in a list.

Examples:

```python
list1 = ["2", "1"]
print(len(list1)) # Should print 2
```

## Keywords

## in

Examples:

```python
list1 = ["This", "is", "a", "list"]
print("is" in list1) # Should print True
print("are" in list1) # Should print False
```

## Methods

### .append()

Add an item to the end of the list. Equivalent to `a[len(a):] = [x].`

Examples:

```python
list1 = ["A", "B", "C", "D"]
list1.append("E")
print(list1) # Should print ["A", "B", "C", "D", "E"]
```

### .insert()

Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

Examples:

```python
list1 = ["A", "B", "C", "D"]
list1.insert(1, "A1")
print(list1) # Should print ["A", "A1, "B", "C", "D"]
```

### .pop()

Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list.

Examples:

```python
list1 = ["A", "B", "C", "D"]
list1.pop(2)
print(list1) # Should print ["A", "B", "D"]
```

### .remove()

Remove the first item from the list whose value is equal to x. It raises a `ValueError` if there is no such item.

Examples:

```python
list1 = ["A", "B", "C", "D"]
list1.remove("B")
print(list1) # Should print ["A", "C", "D"]
```
