#write a python script to extract number from a given text and store all the numbers in a list.
s=input("enter string: ")
print([eval(x) for x in [e for e in s.split(' ') if e!=''] if x.isdigit() or not x.isalpha() and type(eval(x))==float])