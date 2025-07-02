#write a python function to check if an year is leap year (tsrs)
def leap_year(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        if year%400==0:
            return True
        else:
            return False
        
x=leap_year(2001)
print(x)