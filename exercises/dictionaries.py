# Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for index, values in cool_beasts.items():
    print("{} have {}".format(index, values))
    # Should print
    # octopuses have tentacles
    # dolphins have fins
    # rhinos have horns

# Calculate how mny times each letter appears in a text
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaaaa")) # Should print {'a': 7}
print(count_letters("This is an example")) # Should print {'T': 1, 'h': 1, 'i': 2, 's': 2, ' ': 3, 'a': 2, 'n': 1, 'e': 2, 'x': 1, 'm': 1, 'p': 1, 'l': 1}

# Iterate over the key and value pairs of a dictionary using a for loop with the dict.items() method to calculate the sum of the values in a dictionary.
# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.
def sum_server_use_time(Server):

    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items 
    # using a for loop.
    for key,value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]
        
    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)  

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1

# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, domain))
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]})) # Should print ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']

# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			if user in user_groups:
				user_groups[user].append(group)
			else:
				user_groups[user] = [group]

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] })) # Should print {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}

# The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44