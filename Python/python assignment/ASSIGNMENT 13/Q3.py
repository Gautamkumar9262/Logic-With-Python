#write a python script to check whether a given quadratic equation has two real & distinct roots ,real & equal roots or imaginary roots.
# import math
b=int(input("enter b number: "))
a=int(input("enter a number: "))
c=int(input("enter c number: "))
d=b**2-4*a*c

if d > 0: print("Two real & distinct roots.")
elif d == 0: print("Real & equal roots.")
else: print("Imaginary roots.")