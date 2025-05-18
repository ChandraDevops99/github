#we are not sure how many variables passed to the functions(we use arbitary function )
def my_function(*kids):
  print("The youngest child is " , kids)
  print("The youngest child is " , kids[2])

my_function("Emil", "Tobias", "Linus")

"""Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter."""
def fun(ch1,ch2,ch3):
  print("the youngest child  " + ch3)
fun(ch1 ='Chandra',ch2 ='Mahanya',ch3 ='Vishwanya')  


"""Default Parameter Value
 how to use a default parameter value.
If we call the function without argument, it uses the default value:"""
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
The pass Statement
function definitions cannot be empty,
but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.
"""
def myfunction():
  pass
