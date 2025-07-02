#function is block of code which has some name for identification and it only run after the calling.

#takes nothing return nothing

# def add():
#     print("enter two number: ")
#     a=int(input("Enter First no. "))
#     b=int(input("Enter Second no. "))
#     c=a+b
#     print("sum is ",c)

# def product():
#     print("enter two number: ")
#     a=int(input("Enter First no. "))
#     b=int(input("Enter Second no. "))
#     c=a*b
#     print("product is ",c)


# add()
# product()
# print("gautam kumar")
# add() 

# take something return something
def add(a,b):
    return a+b

def product(a,b):
    return a*b
#takes nothing return nothing. 
def f1():
    d=10
    f=20
    result=product(d,f)-add(d,f)
    print(result)

f1()