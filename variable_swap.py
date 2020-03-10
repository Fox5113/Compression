#!/bin/python3


if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))


    a = a + b
    b = a - b
    a = a - b


    print("a: " + str(a) + " b: " + str(b), end="");