#write a python script to print unique digit of a given integer.
x=input("enter a number: ")
u=''
for ch in x:
        if ch not in u:
                u+=ch
    
print(u)