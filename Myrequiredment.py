#create the list by accepting from user
user_input = input("please enter your details (separated by spaces): ")

# Split the input into individual values
values = user_input.split()
# Create a list from the values
Employeedetails = list(values)
for x in Employeedetails:
    print(x)