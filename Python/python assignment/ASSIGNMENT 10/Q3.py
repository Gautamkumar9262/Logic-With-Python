#write a python script to swap data of two varibles.
print("enter two number for swaping ")
a=int(input())
b=int(input())
print("before swaping ",a,b)
a=a+b
b=a-b
a=a-b
print("after swaping ",a,b)

#second
a,b=b,a
print("after swaping ",a,b)