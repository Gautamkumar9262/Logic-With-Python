#write a python script to add two numbers 25(in octal) and 39 (in hexadecimal) and display the result in binary formate.
# a=oct(25)
# b=hex(39)
# print(a+b)
# print(bin(a+b))
# print(bin(int('25', 8) + int('39', 16))[2:])
x=0o25
y=0x39
z=x+y
print(bin(z))
