#write a python script to check if a given charater is present in a given string or not.
x=input("Please enter string: ")
y=input("Please enter character: ")
if y in x:
    print("Found")
else:print("not found")

#second 
x=input("Please enter string: ")
y=input("Please enter character: ")
if y in x:
    print("{} is in the string {}".format(y, x))
else:print("{} is not in the string {}".format(y,x))
