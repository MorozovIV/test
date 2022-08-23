from tkinter import *
from datetime import datetime

clicks = 0

def update_time():
    label1.config(text=f"{datetime.now():%H:%M:%S}")
    root.after(100, update_time)  # Запланировать выполнение этой же функции через 100 миллисекунд

def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
    label2.configure(text="Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()


label1 = Label(text=time, justify=LEFT)
# label1.place(relx=.2, rely=.3)
# label1.grid(column=0, row=0)
label1.pack()

poetry = "Clicks {}".format(clicks)
label2 = Label(text=poetry, justify=LEFT)
# label2.place(relx=.2, rely=.3)
label2.pack()

update_time()
root.update()
root.mainloop()