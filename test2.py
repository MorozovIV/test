from tkinter import *
from netmiko import ConnectHandler
from netmiko import Netmiko
from netmiko.mikrotik import MikrotikRouterOsSSH
import sys
import time
import select
import paramiko
import re


def sh_ver():
    my_device = {'host': '10.10.21.254',
                 'username': 'scripts',
                 'password': 'JG65Ode0wnJHycmr74hfy&ujh4nf74hHuycj!',
                 'global_delay_factor': 3}

    net_conn = Netmiko(**my_device)
    sh_ver = net_conn.send_command('show ver')

    tl = Toplevel()
    tl.rowconfigure(0, weight=1)
    tl.columnconfigure(0, weight=1)
    scroll = Scrollbar(tl, orient=VERTICAL)
    txt = Text(tl, width=20, height=20)
    txt.config(yscrollcommand=scroll.set)
    scroll.config(command=txt.yview)
    txt.insert(1.0, sh_ver)
    txt.grid(column=0, row=0)
    scroll.grid(column=1, row=0, sticky="ns")


root = Tk()
root.title("Управление Cisco")
root.geometry('350x200')

btn = Button(root,
             text="Cisco",
             bg="yellow",
             fg="black",
             command=sh_ver,
             width=20,
             height=2)
btn.grid(column=0, row=0)

root.mainloop()