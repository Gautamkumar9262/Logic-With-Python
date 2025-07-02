#write a python script to create a list of tuple from a given list of strings.where each tuple is a collection of string begin with the same character.

l1=['patna','bhopal','jaipur','pune','japan']
mylist=[]
temp=[]
alpha="abcdefghijklmnopqrstuvwxyz"
l1.sort()

for i in range(0,26):
    temp.clear()
    for j in l1:
        if j.startswith(alpha[i]):
            temp.append(j)
    if(len(temp)>0):
        mylist.append(tuple(temp))
print(mylist)