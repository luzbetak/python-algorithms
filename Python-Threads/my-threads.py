import math
import threading
import time
import random


# -------------------------------------------------------------------#
def job1(msg, value):
    for x in range(100):
        i = math.factorial(int(value * random.random()))
        print("%i ... %s Job1 = %d" % (i, msg, x))
        time.sleep(0.1 * random.random())


# -------------------------------------------------------------------#
def job2(msg, value):
    for x in range(100):
        i = math.sqrt(int(value * random.random()))
        print("%i ... %s Job2 = %d" % (i, msg, x))
        time.sleep(0.1 * random.random())

    # -------------------------------------------------------------------#


th1 = threading.Thread(target=job1, args=("Glob  Crawler", 10))
th1.start()

th2 = threading.Thread(target=job2, args=("Image Crawler", 20))
th2.start()
