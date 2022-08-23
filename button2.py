import tkinter
from tkinter import *
from datetime import datetime

clicks = 0

def update_time():
    time_now.config(text=f"{datetime.now():%H:%M:%S}")
    root.after(100, update_time)  # Запланировать выполнение этой же функции через 100 миллисекунд

def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
    label22.configure(text="Clicks {}".format(clicks))

def auto():
    pass

root = tkinter.Tk()
root.geometry('400x150+{}+{}'.format(500, 400))

time_now = Label(root,text="Time", font=("helvetica", 15))
time_now.grid(column=0, row=1)

label1 = Label(root,text="Температура воздуха:", font=("helvetica", 15))
label1.grid(column=0, row=2)

label11 = Label(root,text="xx't", font=("helvetica", 15))
label11.grid(column=1, row=2)

label2= Label(root,text="Влажность воздуха:", font=("helvetica", 15))
label2.grid(column=0, row=3)

label22 = Label(root,text="xx%", font=("helvetica", 15))
label22.grid(column=1, row=3)

clk = "Clicks {}".format(clicks)
label22 = Label(root, text=clk, justify=LEFT)
label22.grid(column=7, row=7)

btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.grid(column=8, row=7)

btn1 = Button(text="Auto", background="#777", foreground="#ccc",
             padx="20", pady="8", font="16", command=auto)
btn1.grid(column=0, row=7)


update_time()
root.mainloop()