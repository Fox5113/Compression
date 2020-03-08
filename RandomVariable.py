
import time
import os
from datetime import datetime

MAX_RAND = 2**16-1
prossec_id = int(os.getpid())
current_time_microsecond = int(datetime.now().microsecond)

rand =  1 /((prossec_id ** (current_time_microsecond + 1)) % MAX_RAND)



print(str(rand))
