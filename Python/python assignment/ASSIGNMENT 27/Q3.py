#write a python script to check whether it is a palindrome or not.
s=input("enter a string: ")
if s==s[::-1]:
    print("palindrome")

else:
    print("Not a palindrome")