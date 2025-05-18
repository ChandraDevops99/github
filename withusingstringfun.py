class MyClass:
    x = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = MyClass("Chandra", 36)
print(p1)  # with using string function