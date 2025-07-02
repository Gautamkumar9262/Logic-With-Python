#write a python function to calculate compound interest.(tsrs)

def compound_interest(p,t,r):
    a=p*(1+r/100)**t
    return a-p

x=compound_interest(10000,2,3)
print(x)