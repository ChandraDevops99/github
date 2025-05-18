class MyClass:
    x = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

p1 = MyClass("Chandra", 36)
print(p1)#without using string function
print("Name of the person:", p1.name)
print("Person's age is:", p1.age)

#with using string(__str()__)function
def __str__(self):
    return f"{self.name}({self.age})"

p1 = MyClass("Chandra", 36)
print(p1)#without using string function
print("Name of the person:", p1.name)
print("Person's age is:", p1.age)
print(p1)#without using string function

