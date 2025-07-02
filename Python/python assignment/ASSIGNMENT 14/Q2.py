#write a python script to check whether a given number is positive ,nagtive, or zero.
x=int(input("enter a number:"))
match x:
    case 1:
      x=int(input("enter a number: "))
if(x>0):print("positive")
elif(x<0):print("negative")
else:print("zero")