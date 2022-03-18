#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 17, 2022 11:26:49 AM +0200  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
import LoginGUI
import connectGUI
import LobbyCreationGUI
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Username = params[0].get()
        self.Password = params[1].get()

        self.UserLabel = tk.Label(self.top)
        self.UserLabel.place(relx=0.017, rely=0.022, height=31, width=584)
        self.UserLabel.configure(anchor='w')
        self.UserLabel.configure(background="#d9d9d9")
        self.UserLabel.configure(compound='left')
        self.UserLabel.configure(disabledforeground="#a3a3a3")
        self.UserLabel.configure(font="-family {David} -size 18")
        self.UserLabel.configure(foreground="#000000")
        self.UserLabel.configure(text="Current User:" + self.Username)
        self.widgets.append(self.UserLabel)

        self.DisconnectButton = tk.Button(self.top)
        self.DisconnectButton.place(relx=0.033, rely=0.089, height=44, width=117)
        self.DisconnectButton.configure(activebackground="#ececec")
        self.DisconnectButton.configure(activeforeground="#000000")
        self.DisconnectButton.configure(anchor='w')
        self.DisconnectButton.configure(background="#d9d9d9")
        self.DisconnectButton.configure(compound='left')
        self.DisconnectButton.configure(disabledforeground="#a3a3a3")
        self.DisconnectButton.configure(font="-family {David} -size 18")
        self.DisconnectButton.configure(foreground="#000000")
        self.DisconnectButton.configure(highlightbackground="#d9d9d9")
        self.DisconnectButton.configure(highlightcolor="black")
        self.DisconnectButton.configure(pady="0")
        self.DisconnectButton.configure(text='''Disconnect''')
        self.DisconnectButton.configure(command=lambda: self.replaceGUI(LoginGUI, self.top))
        self.widgets.append(self.DisconnectButton)

        self.LobbyFrame = tk.Frame(self.top)
        self.LobbyFrame.place(relx=0.183, rely=0.267, relheight=0.656
                              , relwidth=0.658)
        self.LobbyFrame.configure(relief='groove')
        self.LobbyFrame.configure(borderwidth="2")
        self.LobbyFrame.configure(relief="groove")
        self.LobbyFrame.configure(background="#d9d9d9")
        self.widgets.append(self.LobbyFrame)

        self.ConnectButton = tk.Button(self.LobbyFrame)
        self.ConnectButton.place(relx=0.025, rely=0.034, height=134, width=377)
        self.ConnectButton.configure(activebackground="#ececec")
        self.ConnectButton.configure(activeforeground="#000000")
        self.ConnectButton.configure(background="#d9d9d9")
        self.ConnectButton.configure(compound='left')
        self.ConnectButton.configure(disabledforeground="#a3a3a3")
        self.ConnectButton.configure(font="-family {David} -size 20 -weight bold")
        self.ConnectButton.configure(foreground="#000000")
        self.ConnectButton.configure(highlightbackground="#d9d9d9")
        self.ConnectButton.configure(highlightcolor="black")
        self.ConnectButton.configure(pady="0")
        self.ConnectButton.configure(text='''Connect to Existing Lobby''')
        self.ConnectButton.configure(command=lambda: self.replaceGUI(connectGUI, self.top))
        self.widgets.append(self.ConnectButton)

        self.CreateButton = tk.Button(self.LobbyFrame)
        self.CreateButton.place(relx=0.025, rely=0.508, height=134, width=377)
        self.CreateButton.configure(activebackground="#ececec")
        self.CreateButton.configure(activeforeground="#000000")
        self.CreateButton.configure(background="#d9d9d9")
        self.CreateButton.configure(compound='left')
        self.CreateButton.configure(disabledforeground="#a3a3a3")
        self.CreateButton.configure(font="-family {David} -size 20 -weight bold")
        self.CreateButton.configure(foreground="#000000")
        self.CreateButton.configure(highlightbackground="#d9d9d9")
        self.CreateButton.configure(highlightcolor="black")
        self.CreateButton.configure(pady="0")
        self.CreateButton.configure(text='''Create New Lobby''')
        self.CreateButton.configure(command=lambda: self.replaceGUI(LobbyCreationGUI, self.top))
        self.widgets.append(self.CreateButton)


# def start_up():
#    LobbyGUI_support.main()

if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()