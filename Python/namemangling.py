"""name-mangling"""

# class test:
#     __x=5
#     y=7

# # print(test.y)
# # for g, k in test.__dict__.item():
# #     print(g,k)

# print(test._test__x)

# t1=test(6)
# print(t1.__test__a)

"""operator overloading"""
# class line:
#     def __init__(self,l):
#         self.length=l
#     def show_length(self):
#             print("length=",self.length)
#     def __add__(self,other):
        
#        return line(self.length+other.length)

# l1=line(10)
# l2=line(20)
# l1.show_length()
# l2.show_length()

# l3=l1+l2
# l3.show_length()

"""types of varibale"""
"""Global variable"""
"""Local variable"""

#example 1
def f1():
    x=10 #local variable
    print(x)

#example 2
x=20 #global variable
def f2():
    print(x)
f2()

#example 3
x=20
def f1():
    x=10
    print(x) #accessing local variable
f1()
print(x)#accessing global variable

#example 4
x=20
def f1():
    global x
    x=10
    print(x)
f1()
print(x)

#example 5
x=20
def f1():
    global_bariables=globals()
    