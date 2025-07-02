#decorator
def f1(secret_fumctions):
    def f2():
        x=input(print("Enter your Name "))
        if x=='gautam':
          f1(secret_fumctions)
        else:
            print("you are not an authorize user, please try")






@f1
def reveal_secret():
    print("your password is 'khul ja sim sim'")
    return

