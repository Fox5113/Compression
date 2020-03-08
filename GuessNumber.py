#!/bin/python3

import random

if __name__ == '__main__':

    target = random.randint(1, 100)# if  need any number  target = random.randint()
    shot =  -1
    count_shot = 1
    while target  != shot:
        shot =  int(input("Угадайте число:\n>>>"))
        if target > shot:
            print("Больше.")
            count_shot += 1
        elif target < shot:
            print("Меньше.")
            count_shot += 1
        else:
            print("Это загаданное число." + "\n  Количество попыток: " +  str(count_shot))
