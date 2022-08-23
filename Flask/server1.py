from flask import Flask, render_template
import threading
from tkinter import *
from datetime import datetime

clicks = 0

root = Tk()
app = Flask(__name__)


def flask_main():
    # код для фласка писать тут
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/my-link/')
    def my_link():
        print('I got clicked!')

        return 'Click.'

    if __name__ == '__main__':
        app.run(debug=False)

def tk_main():
    # код для тк тут
    root = tkinter.Tk()
    root.geometry('400x150+{}+{}'.format(500, 400))

    time_now = Label(root, text="Time", font=("helvetica", 15))
    time_now.grid(column=0, row=1)

    label1 = Label(root, text="Температура воздуха:", font=("helvetica", 15))
    label1.grid(column=0, row=2)

    label11 = Label(root, text="xx't", font=("helvetica", 15))
    label11.grid(column=1, row=2)

    label2 = Label(root, text="Влажность воздуха:", font=("helvetica", 15))
    label2.grid(column=0, row=3)

    label22 = Label(root, text="xx%", font=("helvetica", 15))
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
    root.mainloop()  # запуск лупа тк

if __name__ == "__main__":
    pause = threading.Event()
    thread1 = threading.Thread(target=flask_main)

  # flt = threading.Thread(target=flask_main)
    thread1.daemon = False
    thread1.start() #фоновый процесс


    thread2 = threading.Thread(target=tk_main())
    thread2.start()
    # tk_main() #основной поток
thread1.join()
thread2.join()