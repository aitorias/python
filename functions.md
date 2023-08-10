# Functions
 We start a function definition with the `def` keyword, followed by the **name** we want to give our function. After the name, we have the **parameters**, also called **arguments**, for the function enclosed in parentheses. A function **can have no parameters**, or it can have **multiple parameters**. Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters. Lastly, we put a colon at the end of the line.

After the colon, the function body starts. It's important to note that in Python the function body is **delimited by indentation**. This means that all code indented to the right following a function definition is part of the function body. The first line that's no longer indented is the boundary of the function body. It's up to you how many spaces you use when indenting -- just make sure to be consistent. So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.

Examples:

```python
def firstFunction(parameter):
  print("The parameter:", parameter)

firstFunction("test")
```

## Parameters (arguments)
A value passed into a function for use within the function.


## Return value
The return value is the value or variable returned as the end result of a function.
The return keyword tells the function to pass data back. When we call the function, we can store the returned value in a variable. Return values allow our functions to be more flexible and powerful, so they can be reused and called multiple times.

Functions can even return multiple values. Just don't forget to store all returned values in variables! You could also have a function return nothing, in which case the function simply exits.

Examples:

```python
# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))
```