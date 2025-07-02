#write a python script to take one data from user and evaluate type of data if the data is of int type then print Monday, if the data is of float type the print tuesday, if the data is complex type then print wednesday, if the data is type bool then print thursday.

print("press 1 for next processing")

x=int(input("enter a number: "))
match x:
    case 1:
        a=eval(input("Enter a number: "))
        if int==type(a):
            print("Monday")
        elif float==type(a):
            print("Tuesday")
        elif bool==type(a):
            print("Wednesday")
        else:
            print("Thursday")

       




