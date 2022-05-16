#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 24, 2022 10:50:55 AM +0200  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

# import UserFilterAddGUI_support

class Toplevel1:
    def __init__(self, top=None, users=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("483x347+645+402")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top
        if users is not None:
            self.user_list = users  # A list of all users that we put in
        else:
            self.user_list = []

        self.listvar = self.list_to_stringvar(self.user_list)
        self.name_of_chosen = tk.StringVar()
        self.final_name = ""

        self.UserListBox = ScrolledListBox(self.top)
        self.UserListBox.place(relx=0.0, rely=0.0, relheight=0.793
                , relwidth=0.996)
        self.UserListBox.configure(background="white")
        self.UserListBox.configure(cursor="xterm")
        self.UserListBox.configure(disabledforeground="#a3a3a3")
        self.UserListBox.configure(font="TkFixedFont")
        self.UserListBox.configure(foreground="black")
        self.UserListBox.configure(highlightbackground="#d9d9d9")
        self.UserListBox.configure(highlightcolor="#d9d9d9")
        self.UserListBox.configure(selectbackground="blue")
        self.UserListBox.configure(selectforeground="white")
        self.UserListBox.configure(listvariable=self.listvar)

        self.UserNameLabel = tk.Label(self.top)
        self.UserNameLabel.place(relx=0.0, rely=0.807, height=61, width=84)
        self.UserNameLabel.configure(anchor='w')
        self.UserNameLabel.configure(background="#d9d9d9")
        self.UserNameLabel.configure(compound='left')
        self.UserNameLabel.configure(disabledforeground="#a3a3a3")
        self.UserNameLabel.configure(font="-family {David} -size 24")
        self.UserNameLabel.configure(foreground="#000000")
        self.UserNameLabel.configure(text='''User:''')

        self.UserNameEntry = tk.Entry(self.top)
        self.UserNameEntry.place(relx=0.186, rely=0.836, height=40
                , relwidth=0.567)
        self.UserNameEntry.configure(background="white")
        self.UserNameEntry.configure(disabledforeground="#a3a3a3")
        self.UserNameEntry.configure(font="TkFixedFont")
        self.UserNameEntry.configure(foreground="#000000")
        self.UserNameEntry.configure(insertbackground="black")
        self.UserNameEntry.configure(textvariable=self.name_of_chosen)

        self.UserNameAddButton = tk.Button(self.top)
        self.UserNameAddButton.place(relx=0.766, rely=0.807, height=64
                , width=107)
        self.UserNameAddButton.configure(activebackground="#ececec")
        self.UserNameAddButton.configure(activeforeground="#000000")
        self.UserNameAddButton.configure(background="#d9d9d9")
        self.UserNameAddButton.configure(compound='left')
        self.UserNameAddButton.configure(disabledforeground="#a3a3a3")
        self.UserNameAddButton.configure(font="-family {David} -size 14")
        self.UserNameAddButton.configure(foreground="#000000")
        self.UserNameAddButton.configure(highlightbackground="#d9d9d9")
        self.UserNameAddButton.configure(highlightcolor="black")
        self.UserNameAddButton.configure(pady="0")
        self.UserNameAddButton.configure(text='''Add/Remove''')
        self.UserNameAddButton.configure(command=lambda :self.decide_on_name())

    def list_to_stringvar(self, lst) -> tk.StringVar:
        strvar = ''
        for item in lst:
            strvar += str(item) + " "
        strvar = strvar[:-1]
        listvar = tk.StringVar(value=strvar)
        print(listvar.get())
        return listvar

    def decide_on_name(self):
        if self.name_of_chosen.get() in self.user_list:
            self.final_name = self.name_of_chosen.get()
        else:
            t = tk.Toplevel(self.top)
            t.geometry("232x191+660+210")
            t.title("Popup")
            t.resizable(0, 0)
            tk.Label(t, text="Invalid user!", font=('-family {David} -size 20 -weight bold')).place(x=40, y=80)
            pass

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
#def start_up():
#    UserFilterAddGUI_support.main()

if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()




