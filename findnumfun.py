def findnumber(numbers):
    if not numbers:
       return "nothing value"
      
    largest = numbers[0]  
    for value in numbers:
        if value > largest:
            largest = value
    return largest

result = findnumber([2,5,6,8,2])
print("Largest number:", result)