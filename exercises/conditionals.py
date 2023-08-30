# Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))

# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return block_size * full_blocks


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192

# Fill in the blanks to complete the function. The “make_positive” function takes in a number and converts that number to its positive equivalent.  Complete the function to accomplish the following tasks:
# - use an if statement to test if the number is negative
# - use a calculation inside the if statement to change the negative number to be positive
# - use a calculation in the else statement to return any positive “number” unchanged.


def make_positive(number):
    if number < 0:
        result = number * -1
    else:
        result = number
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25))  # Should print 0.25
print(make_positive(5))    # Should print 5
