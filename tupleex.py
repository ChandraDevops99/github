"""
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds.
Change Tuple Values Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""
number = (10,40,50,30)
print(number)
#update the tuple add element in the tuple
list = list(number)
list.append(60)
print(list)
#add two tuple 
tuple1 = ("chandra","raju","rakesh","sukesh")
tuple2 =("Vineetha","Sindhu","Naresh")
print( tuple1 + tuple2)