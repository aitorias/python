# Strings

Strings are sequences of chracters and are **immutable**, this means that they **cannot be modified**. To modify a string, we need to create a new one, but we can also reassign the value of the variable string.

Example:

```python
string1 = "Testt with typo"
new_string1 = string1[0:4] + string1[5:]

print(new_string1) # Should print "Test with typo"

string2 = "I nade a mistake in this string"
new_string2 = string2[0:2] + "m" + string2[3:]

print(new_string2) # Should print "I made a mistake in this string"

string3 = "Hello"
string3 = "Hi"

print(string3) ## Should print "Hi"
```

## Concatenation

Example:

```python
string1 = "One"
string2 = "Two"

result = string1 + string2
print(result) # Should print OneTwo
print(string1 + ", " + string2) # Should print One, Two
```

## Indexing

Indexing allows you to **access individual characters** in a string. You can do this by using square brackets and the location, or index, of the character you want to access

Example:

```python
name = "String"

print(name[1]) # Should print "t"

print(name[-2]) # Should print "n"

# How to get the first character of a string
print(name[0]) # Should print "S"

# How to get the last character of a string:
print(name[len(name)-1]) # Should print "g"
```

## Slice

A slice is the portion of a string that can contain more than one character, also sometimes called a **substring**

Example:

```python
name = "String"

print(name[1:2]) # Should print "tr"

print(name[2:4]) # Should print "rin"

# How to get the 4 first characters of a string
print(name[:3]) # Should print "Stri"

# How to get the every character starting from index 2
print(name[2:]) # Should print "ring"
```

## Functions

### int()

We can convert a numeric string into a number using `int()` function.

Example:

```python
string1 = "1236512"

print(int(string1)) # Should print 1236512

print(int(string1) + 234215) # Should print 1470727
```

## Keywords

### in

The `in` keyword returns True if a substring is contained in a string.

Example:

```python
string1 = "Blue, red, yellow"

print("red" in string1) # Should print True

print("black" in string1) # Should print False
```

## Methods

### .count()

Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation. If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.

Example:

```python
string1 = "Example"

print(string1.count("x")) # Should print 1

print("This is an example of count".count("i")) # Should print 2

print("This is an example of count".count("a")) # Should print 2
```

### .endswith()

Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.

Example:

```python
string1 = "Example"

print(string1.endswith("le")) # Should print True

print(string1.endswith("r")) # Should return False
```

### .format()

Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.

Example:

```python
"The sum of 1 + 2 is {0}".format(1+2) # Should print "The sum of 1 + 2 is 3"

name = "Test"
number = len(name) * 3
print("Hello {}, your lucky number is {}.".format(name,number)) # Should print "Hello Test, your lucky number is 12."
print("{name}, your lucky number is {number}.".format(name=name,number=len(name)*3)) # Should print "Test, your lucky number is 12."

price = 5
with_tax = price * 1.67
print("Base price: ${:.2f}. With tax: ${:.2f}.".format(price, with_tax)) # Should print "Base price: $5.00. With tax: $8.35."
print("Base price: {:.2f}€. With tax: {:.2f}€.".format(price, with_tax)) # Should print "Base price: 5.00€. With tax: 8.35€."
```

### .index()

Then `index()` function displays the index of a certain character or substring, and its justs returns the **first position that matches**.

Example:

```python
string1 = "Example"

print(string1.index("x")) # Should print 1

print(string1.index("mple")) # Should print 3

string2 = "Test of strings"

print(string2.index("t")) # Should print 3
```

### .isnumeric()

Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property.

Example:

```python
string1 = "testt"

print(string1.isnumeric()) # Should print False

print("1265126".isnumeric()) # Should print True
```

### .join()

Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.

Example:

```python
print(" ".join(["This", "is", "an", "example"])) # Should print "This is an example"

print("...".join(["This", "is", "an", "example"])) # Should print "This...is...an...example"
```

### .len()

Then `len()` function tells the number of characters contained in the string.

Example:

```python
string1 = "testt"

print(len(string1)) # Should print 5
```

### .lower()

Example:

```python
string1 = "Test"

print(string1.lower()) # Should print "test"

answer = "YES"

if answer.lower() == "yes":
    print("User answered yes")
```

### .lstrip()

Return a copy of the string with leading characters removed.

Example:

```python
print('   spacious   '.lstrip()) # Should print "spacious   "

print('www.example.com'.lstrip('cmowz.')) # Should print "example.com"
```

### .rstrip()

Return a copy of the string with trailing characters removed.

Example:

```python
print('   spacious   '.rstrip()) # Should print "   spacious"

print('www.example.com'.rstrip('cmowz.')) # Should print "www.example"
```

### .split()

Return a **list of the words in the string**, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

**If sep is given**, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].

**If sep is not specified or is None**, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].

Example:

```python
print('1,2,3'.split(',')) # Should print ['1', '2', '3']

print('1,2,3'.split(',', maxsplit=1)) # Should print ['1', '2,3']

print('1,2,,3,'.split(',')) # Should print ['1', '2', '', '3', '']

print('   1   2   3   '.split()) # Should print ['1', '2', '3']
```

### .strip()

Return a copy of the string with the leading and trailing characters removed.

Example:

```python
print('   spacious   '.strip()) # Should print "spacious"

print('www.example.com'.strip('cmowz.')) # Should print "example"
```

### .upper()

Example:

```python
string1 = "Test"

print(string1.upper()) # Should print "TEST"
```
