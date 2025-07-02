#write a python script to create a set of tuples,where each tuple has two elements representing dice upper face number. take a number N from the user and generate all possible tuples in such a way that tuple elemrnt sums to N.

n=int(input("enter sum of dice numbers "))
s1=set()
for i in range(1,7):
    for j in range(1,7):
        if i+j==n:
            s1.add((i,j))
print(s1)