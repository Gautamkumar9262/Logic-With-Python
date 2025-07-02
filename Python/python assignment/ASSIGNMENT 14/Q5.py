#write a python script to take a string from the user. if the string is a part of "mysirg" then print "One",if the string is a part of"education" then print "two" and if the string is a part of "service"then print"three".
print("mysirg(one),education(two),services(three)")
x=int(input("press 1 for next process:"))
match x:
    case 1:
        a=input("Enter a string: ")
        if a in "mysirg":
            print("One")
        elif a in "education":
            print("Two")
        elif a in "service":
            print("Three")
        else:
            print("not matching by any string")


    




        

