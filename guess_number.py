#!/bin/python3


import random


if __name__ == '__main__':
    target = random.randint(1, 100)# if  need any number  target = random.randint()
    _try =  -1
    count_shot = 1
    while target  != _try:
        _try =  int(input("Угадайте число:\n>>>"))
        if target > _try:
            print("Больше.")
            count_shot += 1
        elif target < _try:
            print("Меньше.")
            count_shot += 1
        else:
            print("Это загаданное число." + "\n  Количество попыток: " +  str(count_shot))
