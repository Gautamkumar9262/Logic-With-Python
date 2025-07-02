#write a python script to check whether a given number is a thre digit number or not.
print("press 1 for next process.")
x=int(input("Enter a number:"))
match x:
    case 1:
     x=int(input("Enter a number"))
     if x>99 and x<=999:
        print("it three digit number")
     else:print("it is not three digit number")


