#write a python script to add two matrices each of order 3 x 3. store matrix elements in a list of lists.
print("enter values row wise for first matrix: ")
A=[]
for i in range(3):
    A.append([int(e) for e in input("enter three number sep by comma: ").split(',')])

print("enter values row wise for second matrix: ")
B=[]
for i in range(3):
    B.append([int(e) for e in input("enter three number sep by comma: ").split(',')])

C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        C[i][j]=A[i][j]+B[i][j]

for i in range(3):
    for j in range(3):
        print(C[i][j],end=' ')
    print()
