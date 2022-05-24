#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 24, 2022 02:21:05 PM +0300  platform: Windows NT
import socket
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from GUI import LoginGUI
from GUI.BaselineGUI import GUI


class Toplevel1(GUI):
    def __init__(self, top=None):
        super(Toplevel1, self).__init__()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+724+234")
        top.minsize(120, 1)
        top.maxsize(4484, 1133)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top
        self.port = 5555
        self.ip = tk.StringVar()

        self.ip_entry = tk.Entry(self.top)
        self.ip_entry.place(relx=0.317, rely=0.4, height=30, relwidth=0.49)
        self.ip_entry.configure(background="white")
        self.ip_entry.configure(disabledforeground="#a3a3a3")
        self.ip_entry.configure(font="TkFixedFont")
        self.ip_entry.configure(foreground="#000000")
        self.ip_entry.configure(insertbackground="black")
        self.ip_entry.configure(textvariable=self.ip)
        self.widgets.append(self.ip_entry)

        self.ip_entry_label = tk.Label(self.top)
        self.ip_entry_label.place(relx=0.25, rely=0.4, height=31, width=34)
        self.ip_entry_label.configure(anchor='w')
        self.ip_entry_label.configure(background="#d9d9d9")
        self.ip_entry_label.configure(compound='left')
        self.ip_entry_label.configure(disabledforeground="#a3a3a3")
        self.ip_entry_label.configure(font="-family {David} -size 18")
        self.ip_entry_label.configure(foreground="#000000")
        self.ip_entry_label.configure(text='''IP:''')
        self.widgets.append(self.ip_entry_label)

        self.ip_entry_button = tk.Button(self.top)
        self.ip_entry_button.place(relx=0.333, rely=0.667, height=74, width=187)
        self.ip_entry_button.configure(activebackground="#ececec")
        self.ip_entry_button.configure(activeforeground="#000000")
        self.ip_entry_button.configure(background="#d9d9d9")
        self.ip_entry_button.configure(compound='left')
        self.ip_entry_button.configure(disabledforeground="#a3a3a3")
        self.ip_entry_button.configure(font="-family {David} -size 23")
        self.ip_entry_button.configure(foreground="#000000")
        self.ip_entry_button.configure(highlightbackground="#d9d9d9")
        self.ip_entry_button.configure(highlightcolor="black")
        self.ip_entry_button.configure(pady="0")
        self.ip_entry_button.configure(text='''Attempt Entry''')
        self.ip_entry_button.configure(command=self.check_for_server_ip)
        self.widgets.append(self.ip_entry_button)

    def check_for_server_ip(self):
        self.ip_address = self.ip.get()
        print(self.ip_address)
        try:
            self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.my_socket.connect((self.ip_address, self.port))
        except:
            self.ip_entry_button.configure(text='''Unsuccessful!''')
        else:
            self.replaceGUI(LoginGUI, self.top, [self.ip, self.port])


if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()
