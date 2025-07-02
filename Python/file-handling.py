import os
#writing text in a file.
def writing(filename, text):
    file=open(filename,'w')
    file.write(text)
    file.close()

writing('for_loop.py','gautam kumar')

#Append data in a file.
def append(filename, text):
    file=open(filename,'a')
    file.write(text)
    file.close()

append('for_loop.py','welcome')

# reading data from a file.
def reading(filename):
    try:
        file=open(filename,'r')
        text=file.read()
        print(text)
        file.close()
    except FileNotFoundError:
        print('File not found')

    reading('for_loop.py')

# Search a word in a txt file.
def search(filename, word):
    try:
        file=open(filename,'r')
        line_count=0
        for line in file.readlines():
            line_count+=1
            strlist=line.split(' ')
            word_count=0
            for w in strlist:
                word_count+=1
                if w==word:
                    return (line_count, word_count)
        else:
            return None
        file.close()

    except FileNotFoundError:
        print('File not found')

print(search('index.txt','bihar'))

#modify content of file.
def modify_file(filename,oldword,newword):
    t=search('index.txt','gautam')
    if t!=None:
        l1=[]

        try:
            file=open(filename,'r')
            for line in file.readlines():
                line=line.replace(oldword,newword)
                l1.append(line)
            file.close()
            file=open(filename,'w')
            file.write(''.join(l1))
            file.close()

        except FileNotFoundError:
            print('File not found')
    else:
        print("search failed")


modify_file('index.txt','gautam','Gautam')

#delete a word from a file
modify_file('index.txt','bihar','')

#rename a file
