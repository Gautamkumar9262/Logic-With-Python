#write a python script to check if a given string has only alphabets in it.
x=input("enter a string: ")
for e in x: 
    if x>='a' and x<='z' or x>='A' and x>='Z':
        pass
    else:
       print("string has some characters other than alphabets")

else:
 print("string has only alphabets")
