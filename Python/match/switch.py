#match 
x=eval(input("enter a number "))
match x:
    case 1,2:
        print("A")
    case '2+3':
        print("B")
    case 'abc':
        print("C")
    case _:
        print("default")

print("outside match block")