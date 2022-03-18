#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 17, 2022 11:45:44 AM +0200  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

# import connectGUI_support
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

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        self.IDLabel = tk.Label(self.top)
        self.IDLabel.place(relx=0.183, rely=0.289, height=41, width=144)
        self.IDLabel.configure(anchor='w')
        self.IDLabel.configure(background="#d9d9d9")
        self.IDLabel.configure(compound='left')
        self.IDLabel.configure(disabledforeground="#a3a3a3")
        self.IDLabel.configure(font="-family {David} -size 20")
        self.IDLabel.configure(foreground="#000000")
        self.IDLabel.configure(text='''Lobby ID:''')
        self.widgets.append(self.IDLabel)

        self.IDEntry = tk.Entry(self.top)
        self.IDEntry.place(relx=0.383, rely=0.289, height=40, relwidth=0.473)
        self.IDEntry.configure(background="white")
        self.IDEntry.configure(disabledforeground="#a3a3a3")
        self.IDEntry.configure(font="TkFixedFont")
        self.IDEntry.configure(foreground="#000000")
        self.IDEntry.configure(insertbackground="black")
        self.widgets.append(self.IDEntry)

        self.ConnectButton = tk.Button(self.top)
        self.ConnectButton.place(relx=0.25, rely=0.556, height=94, width=307)
        self.ConnectButton.configure(activebackground="#ececec")
        self.ConnectButton.configure(activeforeground="#000000")
        self.ConnectButton.configure(background="#d9d9d9")
        self.ConnectButton.configure(compound='left')
        self.ConnectButton.configure(disabledforeground="#a3a3a3")
        self.ConnectButton.configure(font="-family {David} -size 20")
        self.ConnectButton.configure(foreground="#000000")
        self.ConnectButton.configure(highlightbackground="#d9d9d9")
        self.ConnectButton.configure(highlightcolor="black")
        self.ConnectButton.configure(pady="0")
        self.ConnectButton.configure(text='''Connect''')
        self.widgets.append(self.ConnectButton)

# def start_up():
#    connectGUI_support.main()

if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()



