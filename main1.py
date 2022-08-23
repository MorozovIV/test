#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

def On():
    print('Hello')

class Example(Frame):
    def __init__(self):
        super().__init__()
        # self.initUI()
        # self.On()
        # self.Off()
        self.button = ttk.Button(root, text = 'Click')
        self.button.place(x=10, y=10)



    def initUI(root):
        self.pack(fill=BOTH, expand=2)
        selfButton = Button(self, text="Выход", command=quit)
        selfButton.place(x=190, y=140)
    def On(root):
        On.pack(fill=BOTH, expand=1)
        OnButton = Button(self, text="On", command=quit)
        OnButton.place(x=10, y=10)

# BtnOn = Button(root, text='on')
# BtnOff = Button(root, text='off')
# BtnExit = Button(root, text='exit')

# BtnOn.grid()
# BtnOff.grid()
# BtnExit.grid()

def main():
    root = Tk()
    root.title("Курск AnyDesk")
    # photo = tkinter.PhotoImage(file='***.png') # иконка
    # root.iconphoto(False, photo)
    root.geometry("275x175+300+300")
    root.resizable(False, False)
    #app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()