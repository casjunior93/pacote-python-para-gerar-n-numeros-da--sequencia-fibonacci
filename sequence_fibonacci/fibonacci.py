from math import sqrt


def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def get_sequence(startNumber, endNumber):
    n = 0
    cur = F(n)
    list = []
    while cur <= endNumber:
        if startNumber <= cur:
            list.append(int(cur))
        n += 1
        cur = F(n)
    return list
