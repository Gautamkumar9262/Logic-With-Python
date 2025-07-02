#write a python script to create a list of square of number of given list.
# list=[10,20,30,40]
# l2=[x**2 for x in list]
# print(l2)

#second
l1=[int(e) for e in input("enter number sep by comma: ").split(',')]
l2=[r**2 for r in l1]
print(l2)