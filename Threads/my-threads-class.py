import threading
import random
import time


class Job1(threading.Thread):

    def __init__(self, msg, task):
        self.msg = msg
        self.task = task
        threading.Thread.__init__(self)

    def run(self):
        for x in range(10):
            print(self.msg, " job1 task=%d running ..." % self.task)
            time.sleep(2 * random.random())

        print("Done = %s" % self.msg)


class Job2(threading.Thread):

    def __init__(self, msg, task):
        self.msg = msg
        self.task = task
        threading.Thread.__init__(self)

    def run(self):
        for x in range(10):
            print(self.msg, " job2 task=%d running ..." % self.task)
            time.sleep(1 * random.random())

        print("Done = %s" % self.msg)


thread1 = Job1("Thread-1: ", 1)
thread1.start()

thread2 = Job1("Thread-2: ", 2)
thread2.start()

thread3 = Job2("Thread-3: ", 3)
thread3.start()

print("Waiting for threads to finish.\n\n")
