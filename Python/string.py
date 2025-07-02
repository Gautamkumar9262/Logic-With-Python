#print all the charchater of a string but stop printing if 'r' appeared in the sequence. if all the characters sucessfully printed then print the message  all the character are proessed.
x=input("Enter a string: ")
for i in x:
    if i=='r':
        break
    print(x,end='')

else:
    print("\nall the character are proessed")