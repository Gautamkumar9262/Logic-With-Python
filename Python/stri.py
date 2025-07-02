#write program to count 'a' in a given string.
s=input("Enter a string: ")
count=0
for ch in s:
    if ch=='a':
        count+=1
print("Count=",count)