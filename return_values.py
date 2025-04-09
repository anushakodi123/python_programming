import math

def hypot(x, y):
    return math.sqrt(x**2 + y**2)

hypot(2, 3)

def is_between(x, y, z):
    if x<y<z or z<x<y:
        return True
    else:
        return False


def ackermann(m, n):
    if m == 0:
        return ackermann(m-1, n)
    if m > 0 and n == 0:
        return ackermann(m-1, 1)
    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))
    
print(ackermann(5, 5))