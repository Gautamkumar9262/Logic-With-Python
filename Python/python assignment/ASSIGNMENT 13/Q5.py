#write a python script to print greater among three numbers. print number only once even if the number are the same.
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))
if(x>y and x>z):print("greater is ",x)
elif(y>x and y>z):print("greater is ",y)
elif(z>x and z>y):print("greater is ",z)
else:print("all numbers are equal",z)
#second
print(x if x>z  else z if x>y else y if y>z else z)

#third
