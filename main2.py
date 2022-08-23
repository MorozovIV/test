from tkinter import *
from tkinter import ttk

def pr():
    print("ntxt")

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('GUI')
        self.minsize(275, 175)

        self.button1 = ttk.Button(self, text = 'Click1', command= pr())
        self.button1.place(x=10, y=10)
        self.button2 = ttk.Button(self, text = 'Click2')
        self.button2.place(x=10, y=50)
        self.button3 = ttk.Button(self, text = 'Click3', command=quit)
        self.button3.place(x=190, y=140)




root = Root()
root.mainloop()