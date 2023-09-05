# Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

# Write a function that creates a new list containing one string per and the email address between angled brackets like this Example <example@example.com>.
def full_email(users):
	result = []
	for email, user in users:
		result.append("{} <{}>".format(user, email))
	return result

print(full_email([("example@example.com", "Name Lastname"), ("example2@example.com", "Name2 Lastname2")])) # Should print ['Name Lastname <example@example.com', 'Name2 Lastname2 <example2@example.com>']

# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.
def skip_elements(elements):
	# code goes here
	result = []
	
	for index, element in enumerate(elements):
		if index % 2 == 0:
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should print ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should print ['Orange', 'Strawberry', 'Peach']

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
def guest_list(guests):
	for guest in guests:
		name, age, profession = guest
		print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Should print
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
#