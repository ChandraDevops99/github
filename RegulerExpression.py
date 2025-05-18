import  re
x = "Iam a good boy"
y = re.findall("[a-m]",x)
print(y)

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)