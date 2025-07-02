#write a progranm to count a digit 9 present in mobile number entered by the user.
x=int(input("Enter a mobile: "))
count=0
for digit in str(x):
    if digit=='9':
        count+=1
print("count=",count)
