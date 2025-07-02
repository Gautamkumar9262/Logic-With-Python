#write a python script to find first repeated string in a list of strings.
l1=["ab","bc","ab","bc","ab","bc","ca","ca"]
i=0
for x in l1:
    if l1.index(x)!=i:
        print(x," ",i)
        break
    i=i+1