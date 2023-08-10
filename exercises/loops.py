# In Python, what do while loops do?
# CORRECT: while loops tell the computer to repeatedly execute a set of instructions while a condition is true.
# while loops instruct the computer to execute a piece of code a set number of times.
# while loops branch execution based on whether or not a condition is true.
# while loops initialize variables in Python.

# The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. To solve the problem, you will need to:
# 1. Find the error in the code
# 2. Fix the while loop so there is an exit condition
def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number != 0 and number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# Fill in the blanks to complete the while loop so that it returns the sum of all the divisors of a number, without including the number itself. As a reminder, a divisor is a number that divides into another without a remainder. To do this, you will need to:
# 1. Initialize the "divisor" and "total" variables with starting values
# 2. Complete the while loop condition
# 3. Increment the "divisor" variable inside the while loop
# 4. Complete the return statement
def sum_divisors(number):
# Initialize the appropriate variables
  divisor = 1
  total = 0

  # Avoid dividing by 0 and negative numbers 
  # in the while loop by exiting the function
  # if "number" is less than one
  if number < 1:
    return 0 

  # Complete the while loop
  while divisor < number:
    if number % divisor == 0:
      total += divisor
    # Increment the correct variable
    divisor += 1

  # Return the correct variable 
  return total


print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114
