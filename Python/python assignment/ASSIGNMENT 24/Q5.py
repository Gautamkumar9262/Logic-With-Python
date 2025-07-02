#write a python script to create a list from a given list by selecting only even places elements.
l1=[int(e) for e in input("enter number sep by comma: ").split(',')]
l2=[x for x in l1[1::2]]
print(l2)