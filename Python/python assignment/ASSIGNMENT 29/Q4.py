#write a python script to create a list of tuples,where each tuples is a pair of elements, first eleement is uppercase character and second element is its unicode.

mylist=[]
for i in range(65,91):

    mylist.append((chr(i),i))
print(mylist)
