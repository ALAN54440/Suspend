import time
import math
def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stay focused!")

focus_time = int(input("请输入专注时长（分钟）："))
focus_timer(focus_time)
