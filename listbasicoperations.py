#list is collection of elements and it is ordered ,changable,allow duplicates
Employeenames = ["Chandra" ,"Vineetha" ,"Sukesh","Sindhu" ,"Nymisha"]
print(Employeenames)
listex = [1,2,5]#,10,15,78,9,7,3]
#List basic operations
print(len(listex))#print length of the list
print(Employeenames + listex)# concatenation of the two lists
print("repitaion of the list", listex*4)
#print all elements at a time by using for loop
for x in Employeenames:
    print(x)
#reverse of the list
print(listex.reverse())    
#sort the assending order
print(Employeenames.sort())
print(listex.sort())