# Make a function to replace the emails old domains for the new one
def replace_domain(email, old_domain, new_domain):
    # Check if the old domain is in the email.
    if "@" + old_domain in email:
        # Find the index of the old domain, as the email may not have the same length of characters.
        index = email.index("@" + old_domain)
        # Assign the new domain to the email from the index we got previously.
        new_email = email[:index] + "@" + new_domain
        # Return the email with the new domain.
        return new_email
    # If the old domain is not in the email, then return the email.
    return email


result = replace_domain("test@test.com", "test.com", "python.org")

# Should print "test@python.org"
print(result)


# Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


# Display the temperatures in Farenheit and Celsius up to 100 F and align Frarenheit values 3 spaces to the right and Celsius 6 to the right with 2 decimals.
def to_celsius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
