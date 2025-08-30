#COUNTDOWN TIMER

import time

my_time = int(input("Enter time in sec: "))

for x in range(my_time, 0, -1):

    sec = x % 60         #modulus (%) - limit the value of sec to 60
    min = int(x / 60) % 60
    hour = int(x / 3600) % 24
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("Time's Up")





