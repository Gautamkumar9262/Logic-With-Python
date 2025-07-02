#write a python script to print distinct elements along with their frequencies of occurences in the list.
l1=[20,20,30,40,30,20,40,50,20,40]
i=0
for x in l1:
    if i==l1.index(x):
        print(x," ",l1.count(x))
    i+=1

