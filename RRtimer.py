import time
counter1= 1
counter2= 1
counter3= 1
counter4= 1
sum = counter1+counter2+counter3+counter4
timer_traffic_one = counter1/sum
timer_traffic_two = counter2/sum
timer_traffic_three = counter3/sum
timer_traffic_four = counter4/sum

print(timer_traffic_one)
print(timer_traffic_two)
print(timer_traffic_three)
print(timer_traffic_four)
numberOfSecTrafficOne = int(timer_traffic_one*60)
numberOfSecTrafficTwo = int(timer_traffic_two*60)
numberOfSecTrafficThree = int(timer_traffic_three*60)
numberOfSecTrafficFour = int(timer_traffic_four*60)
print(numberOfSecTrafficOne)
# define the countdown func.
def countdown(numberOfSecTrafficOne):
    while numberOfSecTrafficOne:
        mins, secs = divmod(numberOfSecTrafficOne, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        numberOfSecTrafficOne -= 1
        if numberOfSecTrafficOne >0:
            print("Green light for traffic One ")

    print('TRAFFIC ONE IS RED!!')

def countdown1(numberOfSecTrafficTwo):
    while numberOfSecTrafficTwo:
        mins, secs = divmod(numberOfSecTrafficTwo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        numberOfSecTrafficTwo -= 1
        if numberOfSecTrafficTwo >0:
            print("Green light for traffic two ")

    print('Traffic TWO IS RED  ')
# input time in seconds

def countdown2(numberOfSecTrafficThree):
    while numberOfSecTrafficThree:
        mins, secs = divmod(numberOfSecTrafficThree, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        numberOfSecTrafficThree -= 1
        if numberOfSecTrafficThree >0:
            print("Green light for traffic Three ")

    print('Traffic THREE IS RED')


def countdown3(numberOfSecTrafficFour):
    while numberOfSecTrafficFour:
        mins, secs = divmod(numberOfSecTrafficFour, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        numberOfSecTrafficFour -= 1
        if numberOfSecTrafficFour >0:
            print("Green light for traffic Four ")

    print('Traffic Four IS RED')

# function call
while True:


    countdown(numberOfSecTrafficOne)



    countdown1(numberOfSecTrafficTwo)


    countdown2(numberOfSecTrafficThree)
    countdown3(numberOfSecTrafficFour)

