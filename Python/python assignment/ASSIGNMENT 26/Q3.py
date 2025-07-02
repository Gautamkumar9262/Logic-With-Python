#write a python script to count vowels in a given string.
s=input("enter a string: ")
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1
print(count)