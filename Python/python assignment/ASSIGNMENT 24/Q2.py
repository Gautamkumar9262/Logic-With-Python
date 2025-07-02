#write a python script to calculate average of elements of a list.
# l1=[10,20,30,50,40]
# print(sum(l1)/5)

#second
l1=[int(e) for e in input("enter number sep by comma: ").split(',')]
avg=sum(l1)/len(l1)
print(avg)