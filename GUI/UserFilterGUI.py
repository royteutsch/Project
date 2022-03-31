#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 24, 2022 10:24:54 AM +0200  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *


# import ColourFilterGUI_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("227x313+660+303")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("User Filter")
        top.configure(background="#d9d9d9")

        self.top = top
        self.selectedButton = tk.IntVar()

        self.WhiteListButton = tk.Radiobutton(self.top)
        self.WhiteListButton.place(relx=0.0, rely=0.032, relheight=0.08
                                   , relwidth=0.476)
        self.WhiteListButton.configure(activebackground="#ececec")
        self.WhiteListButton.configure(activeforeground="#000000")
        self.WhiteListButton.configure(anchor='w')
        self.WhiteListButton.configure(background="#d9d9d9")
        self.WhiteListButton.configure(compound='left')
        self.WhiteListButton.configure(disabledforeground="#a3a3a3")
        self.WhiteListButton.configure(foreground="#000000")
        self.WhiteListButton.configure(highlightbackground="#d9d9d9")
        self.WhiteListButton.configure(highlightcolor="black")
        self.WhiteListButton.configure(justify='left')
        self.WhiteListButton.configure(text='''W''')
        self.WhiteListButton.configure(variable=self.selectedButton)

        self.BlackListButton = tk.Radiobutton(self.top)
        self.BlackListButton.place(relx=0.485, rely=0.032, relheight=0.08
                                   , relwidth=0.52)
        self.BlackListButton.configure(activebackground="#ececec")
        self.BlackListButton.configure(activeforeground="#000000")
        self.BlackListButton.configure(anchor='w')
        self.BlackListButton.configure(background="#d9d9d9")
        self.BlackListButton.configure(compound='left')
        self.BlackListButton.configure(disabledforeground="#a3a3a3")
        self.BlackListButton.configure(foreground="#000000")
        self.BlackListButton.configure(highlightbackground="#d9d9d9")
        self.BlackListButton.configure(highlightcolor="black")
        self.BlackListButton.configure(justify='left')
        self.BlackListButton.configure(text='''B''')
        self.BlackListButton.configure(variable=self.selectedButton)

        self.UserBox = ScrolledListBox(self.top)
        self.UserBox.place(relx=0.0, rely=0.16, relheight=0.623
                           , relwidth=0.974)
        self.UserBox.configure(background="white")
        self.UserBox.configure(cursor="xterm")
        self.UserBox.configure(disabledforeground="#a3a3a3")
        self.UserBox.configure(font="TkFixedFont")
        self.UserBox.configure(foreground="black")
        self.UserBox.configure(highlightbackground="#d9d9d9")
        self.UserBox.configure(highlightcolor="#d9d9d9")
        self.UserBox.configure(selectbackground="blue")
        self.UserBox.configure(selectforeground="white")

        self.AddUserButton = tk.Button(self.top)
        self.AddUserButton.place(relx=0.0, rely=0.799, height=64, width=227)
        self.AddUserButton.configure(activebackground="#ececec")
        self.AddUserButton.configure(activeforeground="#000000")
        self.AddUserButton.configure(background="#d9d9d9")
        self.AddUserButton.configure(compound='left')
        self.AddUserButton.configure(disabledforeground="#a3a3a3")
        self.AddUserButton.configure(font="-family {David} -size 30")
        self.AddUserButton.configure(foreground="#000000")
        self.AddUserButton.configure(highlightbackground="#d9d9d9")
        self.AddUserButton.configure(highlightcolor="black")
        self.AddUserButton.configure(pady="0")
        self.AddUserButton.configure(text='''Add''')


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
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


# def start_up():
#     ColourFilterGUI_support.main()


if __name__ == '__main__':
    root = tk.Tk()
    t = Toplevel1(root)
    root.mainloop()
