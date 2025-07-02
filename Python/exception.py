class Account:
   def __init__(self,balance):
      self.balance = balance
   def deposit(self )


















try:

   a=int(input("enter first number: "))
   b=int(input("enter second number: "))
   c=a/b
   print("result is:",c)
except ZeroDivisionError:
   print("cannot divide a number by zero")
# except (ValueError, TypeError):
#    print("cannot divide a number by str")
except:
   print("saaluke kuchh to gadbad hai")
finally:
   print("done")

d=int(input("enter first number: "))
e=int(input("enter second number: "))
f=d*e
print("result is:",f)