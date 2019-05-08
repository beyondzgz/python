import _thread
import time


# Define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

# _thread.start_new_thread ( function, args[, kwargs])
try:
    _thread.start_new_thread(print_time, ("one", 1))
    _thread.start_new_thread(print_time, ("tow", 1))
except:
    print("Error: unable to start thread")

while 1:
    pass
