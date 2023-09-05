# Sets

A set is an **unordered collection with no duplicate elements**. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Examples:

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # Should print {'orange', 'banana', 'pear', 'apple'}

print("orange" in basket) # Should print True

a = set('abracadabra')
print(a) # Should print {'a', 'r', 'b', 'c', 'd'}
```

# Set comprehension

Similar to list comprehension.

Examples:

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # Should print {'r', 'd'}
```
