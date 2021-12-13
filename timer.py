import time
import sys
import main
from main import *


import time
print("ffdfsf")
counter= main.Counter
counter1= main.Counter1
counter2= main.Counter2
counter3= main.Counter3# define the countdown func.

def countdown(numberOfSecTrafficOne):
    x = time.time() + numberOfSecTrafficOne
    while time.time() < x:
        mins, secs = divmod(numberOfSecTrafficOne, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        numberOfSecTrafficOne -= 1
        if numberOfSecTrafficOne > 0:
            print("Green light for traffic two ")

    print('Traffic TWO IS RED  ')


def countdown1(numberOfSecTrafficTwo):
    x = time.time() + numberOfSecTrafficTwo
    while time.time() < x:
        mins, secs = divmod(numberOfSecTrafficTwo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        numberOfSecTrafficTwo -= 1
        if numberOfSecTrafficTwo > 0:
            print("Green light for traffic Three ")

    print('Traffic THREE IS RED')
# input time in seconds

def countdown2(numberOfSecTrafficThree):
    x = time.time() + numberOfSecTrafficThree
    while time.time() < x:
        mins, secs = divmod(numberOfSecTrafficThree, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        numberOfSecTrafficThree -= 1
        if numberOfSecTrafficThree >0:
            print("Green light for traffic Three ")

    print('Traffic THREE IS RED')


def countdown3(numberOfSecTrafficFour):
    x = time.time() + numberOfSecTrafficThree
    while time.time() < x:
        mins, secs = divmod(numberOfSecTrafficFour, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        numberOfSecTrafficFour -= 1
        if numberOfSecTrafficFour >0:
            print("Green light for traffic Four ")

    print('Traffic Four IS RED')
print(counter1)
# function call
while True:
    print(counter3)

    sum = counter + counter1 + counter2 + counter3
    timer_traffic_one = counter / sum if sum !=0 else 0
    timer_traffic_two = counter1 / sum  if sum !=0 else 0
    timer_traffic_three = counter2 / sum  if sum !=0 else 0
    timer_traffic_four = counter3 / sum  if sum !=0 else 0

    print(timer_traffic_one)
    print(timer_traffic_two)
    print(timer_traffic_three)
    print(timer_traffic_four)
    numberOfSecTrafficOne = int(timer_traffic_one * 60)
    numberOfSecTrafficTwo = int(timer_traffic_two * 60)
    numberOfSecTrafficThree = int(timer_traffic_three * 60)
    numberOfSecTrafficFour = int(timer_traffic_four * 60)
    print(numberOfSecTrafficOne)
    countdown(numberOfSecTrafficOne)
    countdown1(numberOfSecTrafficTwo)
    countdown2(numberOfSecTrafficThree)
    countdown3(numberOfSecTrafficFour)
    print(counter)
    print(counter1)
    print(counter2)




