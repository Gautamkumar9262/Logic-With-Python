#write a python script to count string which ends at character 's' in a list of strings.
l1=["places","white","fly","gags",'pass']
count=0
for s in l1:
    if s.endswith('s'):
        count+=1
print('count=',count)
print()