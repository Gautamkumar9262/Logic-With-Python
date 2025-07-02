#write a python script to sort list elements in descending order.
# l1=[10,30,40,50,20]
# # print(sorted(l1))
# l1.reverse()
# print(l1)

#second 
l1=[int(e) for e in input("enter number sep by comma: ").split(',')]
l1.sort(reverse=True)
print(l1)