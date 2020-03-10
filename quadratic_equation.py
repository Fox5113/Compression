#!/bin/python3
import math
from decimal import *

if __name__ == '__main__':
    a =  Decimal(input("a: "))
    b =  Decimal(input("b: "))
    c =  Decimal(input("c: "))


    if a == 0 :
        print(-c / b)
    else:

        D =  Decimal(b ** 2 - 4 * a * c)


        if D < 0 :
            print("No solutions")
        elif D < 0.000000000001:
            print(Decimal( -b / (2 * a)))
        else:
            print( str(((-b + Decimal(math.sqrt(D))) / (Decimal(2) * a))), end=" ")
            print( str(((-b - Decimal(math.sqrt(D))) / (Decimal(2) * a))), end=" ")