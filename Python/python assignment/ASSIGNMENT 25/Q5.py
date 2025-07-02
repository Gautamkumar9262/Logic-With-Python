#write a python script to create two lists from a given list a given list of numbers in such a way that the first list can have only positive numbers and second list can have only non positive numbers.
l1=[int(e) for e in input("enter number sep by comma: ").split(',')]
positive=[x for x in l1 if x>0]
non_positive=[x for x in l1 if x<=0]
print(positive)
print(non_positive)
