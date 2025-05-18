#list is collection of elements and it is ordered ,changable,allow duplicates
Employeenames = ["Chandra" ,"Vineetha" ,"Sukesh","Sindhu" ,"Nymisha"]
print(Employeenames)
#length of the list
print("Total length of list") 
print(len(Employeenames))

#different types of data types
EmployeeDetails = [40172440 ,"Chandra" ,"Aplication Support Engineer" , "50000.00"]
print(EmployeeDetails)

#retrived data in list with specified 
print(Employeenames[3])

#use nagative indexing
print(EmployeeDetails[-3])
#change list Item
EmployeeDetails[3] = "Naresh"
print(EmployeeDetails)

#list functions
#append-Add item at the last item 
Employeenames.append("Shivam")
print(Employeenames)

#insert function is used to insert the element in the specified location
Employeenames.insert(6,"pavan")
print(Employeenames)

#extend funtion is used to add the another list to existing list 
Employeenames2 = ["Abhi" ,"Naresh"]
Employeenames.extend(Employeenames2)
print(Employeenames)
 #add two list using concatination operator "+"
Edetails = Employeenames2 + EmployeeDetails
print(Edetails)

#delete the elements in the list
#use remove funtion to delete the exact value in the list
print(Employeenames)
Employeenames.remove("Sindhu")
print(Employeenames)

#pop function is use to delete the value in the list with specified index number
#delete the item in the list (Nymisha)
print(Employeenames)
Employeenames.pop(3)# specified the index number which we need to delete
print(Employeenames)

#Using list comprehension: Creates a new list excluding the specified value
Employeenames = [x for x in Employeenames if x != ('Abhi') and  x != ('Naresh')]
print(Employeenames)  

#Using filter(): This method creates a new list excluding the specified items
items_to_remove = ['Shivam', 'pavan']
Employeenames = list(filter(lambda x: x not in items_to_remove, Employeenames))
print(Employeenames)  # Output: [1, 3, 5]

