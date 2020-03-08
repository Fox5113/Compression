#!/bin/python3
import math



if __name__ == '__main__':
    a =  float(input("a: "))
    b =  float(input("b: "))
    c =  float(input("c: "))


    D =  b ** 2 - 4 * a * c

    if D < 0 :
        print("No solutions")
    elif D == 0:
        print(  str( -b / 2 * a )  )
    else:
        print( str((-b + math.sqrt(D)) / (2 * a)) + " " + str((-b - math.sqrt(D)) / (2 * a)) )