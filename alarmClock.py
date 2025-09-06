#ALARM CLOCK IN PYTHON
import time
import datetime
#import pygame - used to import sound tracks


def setAlarm(alarmTime):
    print(f"Alarm is set for {alarmTime}")

    while True:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)
        if currentTime == alarmTime:
            print("*****WAKE UP*****")
            break

        time.sleep(1)

        

if __name__ == '__main__':
    alarmTime = input("Enter the alarm time in HH:MM:SS - ")
    setAlarm(alarmTime)

