a=int(input("enter a number"))
if(a>0):
    print("positive")
else:
    print("non positive")

#second
a=int(input("enter a number"))
if a>0:
    print("positive")
if a<=0:
    print("non positive")

#2 method
print("positive" if a>0 else "non positive")