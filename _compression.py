#!/bin/python3




if __name__ == '__main__':
    a = list(map(int, input("Введите список для сжатия ").split()))
    count_zero = a.count(0)
    while count_zero > 0  :
        d  = a.remove(0)
        count_zero -= 1
        a.append(0)

    print(a)