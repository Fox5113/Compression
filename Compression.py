#!/bin/python3




if __name__ == '__main__':
    a = list(map(int, input("Введите список для сжатия").split()))
    a.sort(key=lambda v: v == 0)
    print(a)