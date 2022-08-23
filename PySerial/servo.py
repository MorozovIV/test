import pyfirmata
import time

port = 'COM8'
pin = 7
board = pyfirmata.Arduino(port)
print(port)
board.digital[pin].mode = pyfirmata.SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    time.sleep(0.0015)

while True:
    x = input("введи  x:")

    if x =="0":
        rotateservo(pin, 0)
    elif x =="1":
        for i in range(0, 45):
            rotateservo(pin, i)
    elif x=="2":
        for i in range(0, 90):
            rotateservo(pin, i)
    elif x=="3":
        for i in range(0, 134):
            rotateservo(pin, i)
    elif x=="4":
        for i in range(0, 180):
            rotateservo(pin, i)