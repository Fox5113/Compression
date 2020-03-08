#!/bin/python3


#[4, 0, 5, 0, 3, 0, 0, 5]
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

if __name__ == '__main__':
    #n = int(input(""))
    a = list(map(int, input("Введите список для сжатия").split()))
    a.sort(key=lambda v: v == 0)
    print(a)