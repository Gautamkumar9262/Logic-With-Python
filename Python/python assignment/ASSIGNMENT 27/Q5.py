#write a python script to find maximum length word in a given text.
s=input("Please enter string: ")
l1=[e for e in s.split(' ') if e!='']
lengths=[len(x) for x in l1]
print(l1[lengths.index(max(lengths))])

