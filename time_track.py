import datetime
import time


def time_write():
    with open("current_time.txt", mode='a') as file:
        file.write('Current Time is  %s.\n' % (datetime.datetime.now()))
        file.close()

while True:
    time_write()
    time.sleep(60)
