chance=1
while chance<=3:
    x=int(input("enter a even number: "))
    if x%2==0:
        print("you win")
        break
    chance+=1


if chance==4:
 print("you lose")