#write a python script to create dictionary where key are cricket player names and data value are tuple of 4 elements matches played total runs, half centuries and centuiries. all data should be taken from user.

n=int(input("how many paleyers data you want to store? "))
players={}
for i in range(1,5):
    name=input("enter name of players")
    print("enter number of matches played")
    a=input()
    print("total runs")
    b=input()
    print("half centuries")
    c=input()
    print("centuiries")
    d=input()

    players[name]=(a,b,c,d)
for k,v in players.items():
    print(k,v)
