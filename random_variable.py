#!/bin/python3


import time
import os
from datetime import datetime


MAX_RAND = 2 ** 50 + 1


if __name__ == '__main__':
    prossec_id = int(os.getpid()) + 1
    current_time_microsecond = int(datetime.now().microsecond)

    print(prossec_id)
    print(current_time_microsecond)
    rand =  1 / (((prossec_id ** (current_time_microsecond + 1)) % MAX_RAND) + 1)


    print(str(rand))
