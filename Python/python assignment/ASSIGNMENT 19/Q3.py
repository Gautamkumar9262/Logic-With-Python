#write a python script to count occurence of spaces in a given string.
x=input("enter a string: ")
count=0
for ch in x:

    if ch==' ':
        count+=1
        print("count",count)
