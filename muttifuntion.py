def multif(a,b,c):
   sum = a + b +c
   sub = a-b-c
   mul = a*b*c
   return sum,sub,mul

a = int(input("enter a values:"))
b =  int(input("enter b values:"))
c =  int(input("enter c values:"))
sum ,sub, mul = multif(a,b,c)  
print(f"the sum of two numbers {sum}")
print(f"the sub of two numbers  {sub}")
print(f"the multi of two numbers {mul}")




