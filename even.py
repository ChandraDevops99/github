#check wether the given number is even or odd
def evenodd(n):
    if n/2==0:
        print(f"The given  number: {n} is even")
    else:
        print(f"the given number :{n} is odd" )    

n = int(input("enter a number"))
evenodd(n)       