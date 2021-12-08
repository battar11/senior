import time
counter1= 2
counter2= 2
counter3= 0
counter4= 0
timer = time.time()
crowded = time.time() +10
Medium = time.time()+5
Low = time.time()+2
def HightTraffic(pin,pin1,pin3):
    while time.time() < crowded:
        print("1 Green croweded")
        print("other red")

def MediumTraffic(pin,pin1,pin3):
    while time.time() < Medium:
        print("1 Green Meduim")
        print("other red")

def LowTraffic(pin,pin1,pin2):
    while time.time() < Low:
        print("1 Green LOW")
        print("other red")
         

def HightTraffic1(pin,pin1,pin3):
    while time.time() < crowded:
        print("2 Green croweded")
        print("other red")

def MediumTraffic1(pin,pin1,pin3):
    while time.time() < Medium:
        print("2 Green Meduim")
        print("other red")

def LowTraffic1(pin,pin1,pin2):
    while time.time() < Low:
        print("2 Green LOW")
        print("other red")
#if counter1>5:
 #   HightTraffic(1,0,0)

#if counter1>3 and counter1<5:
 #       MediumTraffic(1,0,0)
#if counter1>0 and counter1<3:
 #   LowTraffic(1,1,1)

#if counter2>5:
 #   HightTraffic(1,0,0)

while True:
    if counter1>0 and counter1<3:
        LowTraffic(1,1,1)
    elif counter1>3 and counter1<5:
        MediumTraffic(1,1,1)
    elif counter1>5:
        HightTraffic(1,1,1)

    if counter2>0 and counter2<3:
        LowTraffic1(1,1,1)
    elif counter2>3 and counter2<5:
        MediumTraffic1(1,1,1)
    elif counter2>5:
        HightTraffic1(1,1,1)
