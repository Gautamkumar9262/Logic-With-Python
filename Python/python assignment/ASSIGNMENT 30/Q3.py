#given a set of five player names. write a python script to form all possible pairs of players that is selecting two players at a time.

s1={'gautam','virat','dhoni','sachin','kapil'}
i=0
for p1 in s1:
    i+=i
    for p2 in list(s1)[1::]:
     print(p1,p2)
