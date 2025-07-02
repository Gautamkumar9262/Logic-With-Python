#write a python script to make a menu driven in which user has to choose one of the option from four given option -1) odd-even,2) positive -non positive,3) simple interest and 4) find roots of quaratic equation. match and execute appropriate code on user selection.
print("You have 4 options choose your choice:- \nfor finding odd-even press 1. \nfor finding positive-non positive press 2. \nfor finding simple interest press 3. \nfor finding roots of quaratic equation press 4.")

x=int(input("\nEnter your choice: "))
match x:
    case 1 :
       a=int(input("Enter a number: "))
       print("Even" if a%2==0 else "Odd")
       x=input()
    

    case 2 :
        b=int(input("Enter a number: "))
        print("Positive" if b>0 else "Non-postive")

        x=input()

    case 3 :
        i=int(input("Enter a capital: "))
        j=int(input("Enter a Rate : "))
        k=int(input("Enter a time in month: "))
        SI=i*j*(k/12)/100
        print("Simple interest is ",SI)
        print("Total capital+interest is",SI+i)
        x=input()
    
    case 4:
        b=int(input("enter number b: "))
        a=int(input("enter number a: "))
        c=int(input("enter number c: "))
        d=b**2-4*a*c
        if d>0:print("two real & distinct roots")
        elif d==0:print("real & equal roots")
        else:print("two imagianry roots")
        x=input()

    case 5:
        print("Invalid choice")
        x=input()

        


    




        

