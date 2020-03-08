#!/bin/python3


if __name__ == '__main__':
   # while True: #if need infinitely
        count_ice_cream = int(input(">>>"))
        if count_ice_cream % 3 == 0  or count_ice_cream % 5 == 0:
            print("Yes", end="")
        else:
            print("No", end="");