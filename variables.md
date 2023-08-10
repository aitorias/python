# Variables
Variables are an **instance of a data type class**, represented by a **unique name** within the code, that stores changeable values of the specific data type.
Those values can be of any data type (numbers, strings, even results of operations, etc.).

Examples:

```python
x = 1
y = 2
result = x + y
floatVariable = 1.2
emptyVariable = ""
stringVariable = "test"
```

Variables are **case sensitive**, so **capitalization** matters. Lowercasename, uppercasename and allcapsname are **all differents variable names**.

Examples:

```python
x = 1
X = 2
variable = "test"
Variable = "test2"
VARIABLE = "test3"
```

## Restrictions
- Don't use keywords or functions that Python reserves for its own
- Don't use spaces
- Must start with a letter or an underscore (__variable_)
- Must be made up of only letters, numbers, and underscores (__variable_)

Examples:

```python
variable # is valid
variable2 # is valid
variable_3 # is valid
1_variable # is NOT valid
var_&_one # is NOT valid
```