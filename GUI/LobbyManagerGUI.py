#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 17, 2022 11:55:11 AM +0200  platform: Windows NT
import ast
import sys
from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

# import LobbyManagerGUI_support
import Client
from GUI import mainGUI, LobbyUserListGUI
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

        top.geometry("808x450+560+213")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.sec_status = "Public"
        self.users = []
        self.users_string = ""
        self.user_list_text_variable = tk.StringVar()
        self.bg_file = tk.StringVar()

        if params[2]:
            self.client = params[2]

        if params[1].get():
            self.sec_status = "Private"

        if params[0].get():
            self.lobby_name = params[0].get()

        self.top = top

        if params is not None:
            print("Initiating Lobby")
            self.top.after(100, self.initiate_lobby(params[0].get(), params[1].get()))

        self.lobby_name_label = tk.Label(self.top)
        self.lobby_name_label.place(relx=0.025, rely=0.044, height=41, width=600)
        self.lobby_name_label.configure(anchor='w')
        self.lobby_name_label.configure(background="#d9d9d9")
        self.lobby_name_label.configure(compound='left')
        self.lobby_name_label.configure(disabledforeground="#a3a3a3")
        self.lobby_name_label.configure(font="-family {David} -size 18")
        self.lobby_name_label.configure(foreground="#000000")
        self.lobby_name_label.configure(text='''Name: ''' + params[0].get())
        self.widgets.append(self.lobby_name_label)

        self.lobbyIDLabel = tk.Label(self.top)
        self.lobbyIDLabel.place(relx=0.309, rely=0.156, height=101, width=314)
        self.lobbyIDLabel.configure(anchor='w')
        self.lobbyIDLabel.configure(background="#d9d9d9")
        self.lobbyIDLabel.configure(compound='left')
        self.lobbyIDLabel.configure(disabledforeground="#a3a3a3")
        self.lobbyIDLabel.configure(font="-family {David} -size 30")
        self.lobbyIDLabel.configure(foreground="#000000")
        self.lobbyIDLabel.configure(text='''ID:''' + self.lobby.id)
        self.widgets.append(self.lobbyIDLabel)

        self.SecLabel = tk.Label(self.top)
        self.SecLabel.place(relx=0.73, rely=0.044, height=41, width=203)
        self.SecLabel.configure(anchor='w')
        self.SecLabel.configure(background="#d9d9d9")
        self.SecLabel.configure(compound='left')
        self.SecLabel.configure(disabledforeground="#a3a3a3")
        self.SecLabel.configure(font="-family {David} -size 18")
        self.SecLabel.configure(foreground="#000000")
        self.SecLabel.configure(text='''Security: ''' + self.sec_status)
        self.widgets.append(self.SecLabel)

        self.UserListLabel = tk.Label(self.top)
        self.UserListLabel.place(relx=0.037, rely=0.378, height=51, width=604)
        self.UserListLabel.configure(anchor='w')
        self.UserListLabel.configure(background="#d9d9d9")
        self.UserListLabel.configure(compound='left')
        self.UserListLabel.configure(disabledforeground="#a3a3a3")
        self.UserListLabel.configure(font="-family {David} -size 18")
        self.UserListLabel.configure(foreground="#000000")
        self.UserListLabel.configure(textvariable=self.user_list_text_variable)
        self.widgets.append(self.UserListLabel)

        self.SeeAll = tk.Button(self.top)
        self.SeeAll.place(relx=0.804, rely=0.378, height=44, width=147)
        self.SeeAll.configure(activebackground="#ececec")
        self.SeeAll.configure(activeforeground="#000000")
        self.SeeAll.configure(background="#d9d9d9")
        self.SeeAll.configure(compound='left')
        self.SeeAll.configure(disabledforeground="#a3a3a3")
        self.SeeAll.configure(font="-family {David} -size 18")
        self.SeeAll.configure(foreground="#000000")
        self.SeeAll.configure(highlightbackground="#d9d9d9")
        self.SeeAll.configure(highlightcolor="black")
        self.SeeAll.configure(pady="0")
        self.SeeAll.configure(text='''See All''')
        self.SeeAll.configure(command=lambda :self.view_clients())
        self.widgets.append(self.SeeAll)

        self.BGFileLabel = tk.Label(self.top)
        self.BGFileLabel.place(relx=0.037, rely=0.6, height=41, width=2000)
        self.BGFileLabel.configure(anchor='w')
        self.BGFileLabel.configure(background="#d9d9d9")
        self.BGFileLabel.configure(compound='left')
        self.BGFileLabel.configure(disabledforeground="#a3a3a3")
        self.BGFileLabel.configure(font="-family {David} -size 16")
        self.BGFileLabel.configure(foreground="#000000")
        self.BGFileLabel.configure(text='''BG File:''' + self.bg_file.get())
        self.widgets.append(self.BGFileLabel)

        self.UploadButton = tk.Button(self.top)
        self.UploadButton.place(relx=0.037, rely=0.733, height=64, width=127)
        self.UploadButton.configure(activebackground="#ececec")
        self.UploadButton.configure(activeforeground="#000000")
        self.UploadButton.configure(background="#d9d9d9")
        self.UploadButton.configure(compound='left')
        self.UploadButton.configure(disabledforeground="#a3a3a3")
        self.UploadButton.configure(font="-family {David} -size 16")
        self.UploadButton.configure(foreground="#000000")
        self.UploadButton.configure(highlightbackground="#d9d9d9")
        self.UploadButton.configure(highlightcolor="black")
        self.UploadButton.configure(pady="0")
        self.UploadButton.configure(text='''Upload''')
        self.UploadButton.configure(command=lambda: self.choose_file())
        self.widgets.append(self.UploadButton)

        self.StartSessionButton = tk.Button(self.top)
        self.StartSessionButton.place(relx=0.347, rely=0.689, height=114
                                      , width=497)
        self.StartSessionButton.configure(activebackground="#ececec")
        self.StartSessionButton.configure(activeforeground="#000000")
        self.StartSessionButton.configure(background="#d9d9d9")
        self.StartSessionButton.configure(compound='left')
        self.StartSessionButton.configure(disabledforeground="#a3a3a3")
        self.StartSessionButton.configure(font="-family {David} -size 36")
        self.StartSessionButton.configure(foreground="#000000")
        self.StartSessionButton.configure(highlightbackground="#d9d9d9")
        self.StartSessionButton.configure(highlightcolor="black")
        self.StartSessionButton.configure(pady="0")
        self.StartSessionButton.configure(text='''Start Session''')
        self.StartSessionButton.configure(command=lambda: self.start_drawing())
        self.widgets.append(self.StartSessionButton)

    def initiate_lobby(self, lobby_name, lobby_security):
        self.lobby = Client.Lobby(lobby_name=lobby_name, priv_or_publ=lobby_security,
                                  client_name=self.client.username, ip=self.client.ip, port=self.client.port)
        self.top.after(1000, self.run_lobby_loop)

    def run_lobby_loop(self):
        self.lobby.one_loop()
        print("looping on lobby")
        self.top.after(1000, self.run_lobby_loop)
        # Update the user list
        self.users = self.lobby.connected_users.keys()
        self.update_users_string()

    def update_users_string(self):
        ret = ""
        for user in self.users:
            ret += str(user) + " ,"
        self.users_string = ret[:-1]
        self.user_list_text_variable.set('''Connected: ''' + self.users_string)

    def choose_file(self):
        filetypes = (
            ('svg files', '*.svg'),
        )

        filename = filedialog.askopenfilename(
            title='Open File',
            initialdir='/',
            filetypes=filetypes
        )

        self.bg_file.set(filename)
        self.BGFileLabel.configure(text='''BG File:''' + self.bg_file.get())  # Update text in the label

    def view_clients(self):
        t = tk.Toplevel(self.top)
        user_list_view = LobbyUserListGUI.Toplevel1(top=t, users=ast.literal_eval(self.lobby.send_names()))
        pass

    def start_drawing(self):
        self.lobby.send_to_everyone("D")
        if len(self.bg_file.get()) > 0:  # We have a selected bg file
            self.lobby.send_bg_file(self.bg_file.get())
        self.replaceGUI(mainGUI, self.top, [self.lobby, "l"])
# def start_up():
#     LobbyManagerGUI_support.main()

if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()




