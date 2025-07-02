#write a python script to reverse a string word wise(for example -"mysirg eduvation services" is a given string and resulting string should be "services education Mysirg")
s=input("Please enter strings: ")
print(' '.join([e for e in s.split(' ') if e!=' '][::-1]))