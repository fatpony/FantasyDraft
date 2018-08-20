import time

default_time = 5

def timer(x):
    for i in range(x + 1):
        time.sleep(1)
        print(formatTime(x))
        x -= 1

def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))

timer(default_time)
