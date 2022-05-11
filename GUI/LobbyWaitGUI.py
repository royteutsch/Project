#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 23, 2022 12:51:24 PM +0200  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

# import LobbyWaitGUI_support
from GUI import mainGUI
from GUI.BaselineGUI import GUI


class Toplevel1(GUI):
    def __init__(self, top=None, params=None):
        super(Toplevel1, self).__init__()
        if params is None:
            params = []
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        if params[0]:
            self.Client = params[0]
            # self.ID = params[1]

        # self.Client.inquire_lobby(str(self.ID).zfill(12))

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.25, rely=0.2, height=71, width=284)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {David} -size 20")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Connecting''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.333, rely=0.489, height=91, width=174)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {David} -size 20")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Please Wait...''')

        self.top.after(1000, self.wait)

    def wait(self):
        self.top.after(100, self.Client.wait_for_lobby)
        if self.Client.drawing == 1:
            print("Done Waiting")
            self.replaceGUI(mainGUI, self.top, [self.Client, "c"])
        else:
            print("Waiting...")
            self.top.after(1000, self.wait)

#def start_up():
#    LobbyWaitGUI_support.main()

if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()




