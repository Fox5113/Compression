#!/bin/python3


if __name__ == '__main__':
   # while True: #if need infinitely
        count_ice_cream = int(input(">>>"))

        while True:
            if count_ice_cream % 5 == 0  or count_ice_cream % 3  == 0:
                print("Yes", end="")
                break
            if count_ice_cream > 5 and  count_ice_cream - 5  >= 5 :
                count_ice_cream -=5
            elif count_ice_cream > 5 and  count_ice_cream - 5  < 5 :
                count_ice_cream -=3
            elif count_ice_cream > 5 and  count_ice_cream - 5  <= 3:
                count_ice_cream -=3
            
            elif  (count_ice_cream > 3 and  count_ice_cream < 5 ) or  count_ice_cream < 3 :
                print("No", end="")
                break
            elif count_ice_cream == 5 or count_ice_cream == 3 :
                print("Yes", end="")
                break
            else:
                print(count_ice_cream)
            