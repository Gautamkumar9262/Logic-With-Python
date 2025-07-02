#create two sets from a given set of numbers to separate even and odd numbers.

s1={10,22,49,17,53,28,60}
odd=set()
even=set()

for e in s1:
    if e%2==0:
        even.add(e)
    else:
        odd.add(e)

print(even,odd)