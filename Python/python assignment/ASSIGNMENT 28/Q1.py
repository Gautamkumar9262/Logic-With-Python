#write a python script to remove all non int values from a list.
l1=[20,4.5,'abc',3+4j,True,30,40]
i=0
l2=[]
while(i<len(l1)):
    if type(l1[i])==int:
        l2.append(l1[i])
    i+=1
print(l2)