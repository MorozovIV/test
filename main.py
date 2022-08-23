# -*- coding: utf-8 -*-
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

import paramiko
# Server related information, below enter your personal username, password, IP and other information
ip = "10.10.144.254"
port = 22
user = "scripts"
password = "JG65Ode0wnJHycmr74hfy&ujh4nf74hHuycj!"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.initOFF()
        self.initON()

    def initON(ON):
        ON.style = Style()
        ON.style.theme_use("default")

        ON.pack(fill=BOTH, expand=1)

        ONButton = Button(ON, text="Включить доступ по AnyDesk", command=ON)
        ONButton.place(x=10, y=10)

    def initUI(self):
        self.parent.title("Курский AnyDesk")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Закрыть окно", command=self.quit)
        quitButton.place(x=150, y=120)

    def initOFF(self):
        self.style = Style()
        self.style.theme_use("default")

        def OFF(self):

            # # Establish a connection
            ssh.connect(ip,port,user,password,timeout = 10)
            # # Enter the Linux command
            self.stdin,stdout,stderr = ssh.exec_command("system script run anydesk_off")
            #stdin,stdout,stderr = ssh.exec_command("system script run anydesk_on")
            ssh.close()

        self.pack(fill=BOTH, expand=1)

        OFFButton = Button(OFF, text="Выключить доступ по AnyDesk", command=OFF)
        OFFButton.place(x=10, y=50)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # Establish a connection
# ssh.connect(ip,port,user,password,timeout = 10)
# # Enter the Linux command
# #stdin,stdout,stderr = ssh.exec_command("system script run anydesk_off")
# #stdin,stdout,stderr = ssh.exec_command("system script run anydesk_on")
# # Close the connection
# ssh.close()