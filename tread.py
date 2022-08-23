from tkinter import *
import keyboard
from time import sleep
import threading


def main():
    while pause.wait():
        print("work")
        sleep(1)

        def click_button():
            global clicks
            clicks += 1
            root.title("Clicks {}".format(clicks))

        root = Tk()
        root.title("GUI на Python")
        root.geometry("300x250")

        btn = Button(text="Click Me", background="#555", foreground="#ccc",
                     padx="20", pady="8", font="16", command=pause.clear())
        btn.pack()

        root.mainloop()


def off():
    while True:
        if keyboard.wait('Ctrl + 1') is None: # активация цикла на Ctrl + 1
            pause.set()
        if keyboard.wait('Ctrl + 2') is None: # остановка цикла на Ctrl + 2
            pause.clear()




pause = threading.Event()
thread1 = threading.Thread(target=main)
thread2 = threading.Thread(target=off)

thread1.start()
thread2.start()

thread1.join()
thread2.join()