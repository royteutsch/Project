#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 17, 2022 11:15:50 AM +0200  platform: Windows NT

import sys
import tkinter as tk

import Client
import LobbyGUI
import webbrowser
from tkinter import *


# import LoginGUI_support
from GUI.BaselineGUI import GUI


class Toplevel1(GUI):
    def __init__(self, top=None):
        super(Toplevel1, self).__init__()
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

        self.Username = StringVar()
        self.Password = StringVar()

        self.Title = tk.Label(self.top)
        self.Title.place(relx=0.283, rely=0.022, height=61, width=254)
        self.Title.configure(anchor='w')
        self.Title.configure(background="#d9d9d9")
        self.Title.configure(compound='left')
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(font="-family {David} -size 20")
        self.Title.configure(foreground="#000000")
        self.Title.configure(text='''Please connect to User''')
        self.widgets.append(self.Title)

        self.LoginFrame = tk.Frame(self.top)
        self.LoginFrame.place(relx=0.2, rely=0.222, relheight=0.589
                              , relwidth=0.592)
        self.LoginFrame.configure(relief='groove')
        self.LoginFrame.configure(borderwidth="2")
        self.LoginFrame.configure(relief="groove")
        self.LoginFrame.configure(background="#d9d9d9")
        self.widgets.append(self.LoginFrame)

        self.UsernameLabel = tk.Label(self.LoginFrame)
        self.UsernameLabel.place(relx=0.085, rely=0.038, height=69, width=114)
        self.UsernameLabel.configure(anchor='w')
        self.UsernameLabel.configure(background="#d9d9d9")
        self.UsernameLabel.configure(compound='left')
        self.UsernameLabel.configure(disabledforeground="#a3a3a3")
        self.UsernameLabel.configure(font="-family {David} -size 18")
        self.UsernameLabel.configure(foreground="#000000")
        self.UsernameLabel.configure(text='''Username:''')
        self.widgets.append(self.UsernameLabel)

        self.UsernameEntry = tk.Entry(self.LoginFrame)
        self.UsernameEntry.place(relx=0.423, rely=0.113, height=30
                                 , relwidth=0.518)
        self.UsernameEntry.configure(background="white")
        self.UsernameEntry.configure(disabledforeground="#a3a3a3")
        self.UsernameEntry.configure(font="TkFixedFont")
        self.UsernameEntry.configure(foreground="#000000")
        self.UsernameEntry.configure(insertbackground="black")
        self.UsernameEntry.configure(textvariable=self.Username)
        self.widgets.append(self.UsernameEntry)

        self.PasswordLabel = tk.Label(self.LoginFrame)
        self.PasswordLabel.place(relx=0.085, rely=0.34, height=71, width=114)
        self.PasswordLabel.configure(anchor='w')
        self.PasswordLabel.configure(background="#d9d9d9")
        self.PasswordLabel.configure(compound='left')
        self.PasswordLabel.configure(disabledforeground="#a3a3a3")
        self.PasswordLabel.configure(font="-family {David} -size 18")
        self.PasswordLabel.configure(foreground="#000000")
        self.PasswordLabel.configure(text='''Password:''')
        self.widgets.append(self.PasswordLabel)

        self.PasswordEntry = tk.Entry(self.LoginFrame)
        self.PasswordEntry.place(relx=0.423, rely=0.415, height=30
                                 , relwidth=0.518)
        self.PasswordEntry.configure(background="white")
        self.PasswordEntry.configure(disabledforeground="#a3a3a3")
        self.PasswordEntry.configure(font="TkFixedFont")
        self.PasswordEntry.configure(foreground="#000000")
        self.PasswordEntry.configure(insertbackground="black")
        self.PasswordEntry.configure(textvariable=self.Password)
        self.widgets.append(self.PasswordEntry)

        self.ConnectButton = tk.Button(self.LoginFrame)
        self.ConnectButton.place(relx=0.338, rely=0.717, height=64, width=117)
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
        self.ConnectButton.configure(text='''Connect''')
        # TODO: CHECK IF USER EXISTS IN DATABASE
        self.ConnectButton.configure(command=lambda: self.connect_to_user(self.Username.get(), self.Password.get()))
        self.widgets.append(self.ConnectButton)

        self.CreateButton = tk.Button(self.top)
        self.CreateButton.place(relx=0.733, rely=0.911, height=34, width=147)
        self.CreateButton.configure(activebackground="#ececec")
        self.CreateButton.configure(activeforeground="#000000")
        self.CreateButton.configure(background="#d9d9d9")
        self.CreateButton.configure(compound='left')
        self.CreateButton.configure(disabledforeground="#a3a3a3")
        self.CreateButton.configure(font="-family {David} -size 15")
        self.CreateButton.configure(foreground="#000000")
        self.CreateButton.configure(highlightbackground="#d9d9d9")
        self.CreateButton.configure(highlightcolor="black")
        self.CreateButton.configure(pady="0")
        self.CreateButton.configure(text='''Create New User''')
        self.CreateButton.configure(command=lambda: webbrowser.open("www.google.com"))
        self.widgets.append(self.CreateButton)

    def connect_to_user(self, Username, Password):
        clientUser = Client.User(Username, Password)
        print(clientUser.success)
        if clientUser.success:  # If the Client was created successfully
            print("Client Creation Successful, switching GUI")
            self.replaceGUI(LobbyGUI, self.top, [self.Username, self.Password])
        else:
            # TODO: ADD POPUP ASKING FOR RETRY, CLEAN ENTRIES
            pass


# def start_up():
#    LoginGUI_support.main()

if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()
