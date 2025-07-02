#write a python script to count words in a given string
s=input("enter a string: ")
count=0
for i in s:
    if i in " ":
        count+=1
print(count+1)

#second
s=input("enter string: ")
print("total words are: ",len([e for e in s.split(' ') if e!=' ']))