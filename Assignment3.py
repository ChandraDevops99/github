""" 
Create a list with at least 5 different elements (e.g., integers, strings).
Add a new element to the end of the list.
Remove the second element from the list.
Print the length of the list.
"""
#Create a list with at least 5 different elements (e.g., integers, strings).
EmployeeDetails = [4017 , "Chandra" ,"Python Developer" ,50000.00 , "HBK client"]
#Add a new element to the end of the list(append)function
print(EmployeeDetails.append("CES Ltd Company"))
print(EmployeeDetails)

#Remove the second element from the list()
#use remove funtion to delete the exact value in the list
print(EmployeeDetails)
EmployeeDetails.remove("Chandra")
print(EmployeeDetails)
#Print the length of the list.
print("length of the list" ,len(EmployeeDetails))

