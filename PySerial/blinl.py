import pyfirmata
import time

board = pyfirmata.Arduino('COM8')
print('com8')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[12].write(1)
    print('on')
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[12].write(0)
    print('off')
    time.sleep(1)