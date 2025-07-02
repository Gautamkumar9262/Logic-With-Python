#write a python function to find greater among three numbers (tsrs)
def greater(x, y,z):
    if x>=y and x>=z: return x
    if y>=x and y>=z: return y
    if z>=x and z>=y: return z

x=greater(0,1,2)
print(x)


def greater(x,y,z):
    if x>y:
        if x>z: return x
        else: return y
    else:
        if y>z: return y
        else: return z

    