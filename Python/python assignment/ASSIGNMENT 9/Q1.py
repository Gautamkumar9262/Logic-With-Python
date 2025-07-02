#write a python script to calculate simple intrest.
print("this software made for calculate simple interest")
print("enter priciple: ")
x=int(input())
print("enter rate: ")
y=int(input())
print("enter time in year : ")
z=int(input())
SI=(x*y*z)/100
print("simple interest is ",SI)
print("sum of principle and interest is ",x+SI)
input()

#second method
print("enter p,r,t")
p=float(input())
r=float(input())
t=float(input())

si=p*r*t/100
print("simple interest is ",si)
