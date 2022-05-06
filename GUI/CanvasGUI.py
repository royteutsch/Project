#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 19, 2022 11:05:59 AM +0300  platform: Windows NT
import os
import webbrowser
import sys
import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        # canvas part of the canvas. used to display strokes and to draw
        b = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s &')

        b.open("file://"+os.path.realpath("canvas.html"))

        # Tkinter part of the canvas. used for filters, and stroke selection

        top.geometry("261x669+1389+238")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.FilterFrame = tk.Frame(self.top)
        self.FilterFrame.place(relx=0.441, rely=0.015, relheight=0.951
                               , relwidth=0.544)
        self.FilterFrame.configure(relief='groove')
        self.FilterFrame.configure(borderwidth="2")
        self.FilterFrame.configure(relief="groove")
        self.FilterFrame.configure(background="#d9d9d9")
        self.FilterFrame.configure(highlightbackground="#d9d9d9")
        self.FilterFrame.configure(highlightcolor="black")

        self.FilterLabel = tk.Label(self.FilterFrame)
        self.FilterLabel.place(relx=0.07, rely=0.02, height=101, width=121)
        self.FilterLabel.configure(activebackground="#f9f9f9")
        self.FilterLabel.configure(activeforeground="black")
        self.FilterLabel.configure(background="#d9d9d9")
        self.FilterLabel.configure(disabledforeground="#a3a3a3")
        self.FilterLabel.configure(font="-family {David} -size 20")
        self.FilterLabel.configure(foreground="#000000")
        self.FilterLabel.configure(highlightbackground="#d9d9d9")
        self.FilterLabel.configure(highlightcolor="black")
        self.FilterLabel.configure(text='''Filters''')

        self.TimeFilterFrame = tk.Frame(self.FilterFrame)
        self.TimeFilterFrame.place(relx=0.0, rely=0.178, relheight=0.228
                                   , relwidth=1.0)
        self.TimeFilterFrame.configure(relief='groove')
        self.TimeFilterFrame.configure(borderwidth="2")
        self.TimeFilterFrame.configure(relief="groove")
        self.TimeFilterFrame.configure(background="#d9d9d9")
        self.TimeFilterFrame.configure(highlightbackground="#d9d9d9")
        self.TimeFilterFrame.configure(highlightcolor="black")

        self.FromLabel = tk.Label(self.TimeFilterFrame)
        self.FromLabel.place(relx=0.07, rely=0.09, height=39, width=53)
        self.FromLabel.configure(activebackground="#f9f9f9")
        self.FromLabel.configure(activeforeground="black")
        self.FromLabel.configure(anchor='w')
        self.FromLabel.configure(background="#d9d9d9")
        self.FromLabel.configure(compound='left')
        self.FromLabel.configure(disabledforeground="#a3a3a3")
        self.FromLabel.configure(font="-family {David} -size 12")
        self.FromLabel.configure(foreground="#000000")
        self.FromLabel.configure(highlightbackground="#d9d9d9")
        self.FromLabel.configure(highlightcolor="black")
        self.FromLabel.configure(text='''From:''')

        self.FromEntry = tk.Entry(self.TimeFilterFrame)
        self.FromEntry.place(relx=0.486, rely=0.09, height=30, relwidth=0.451)
        self.FromEntry.configure(background="white")
        self.FromEntry.configure(disabledforeground="#a3a3a3")
        self.FromEntry.configure(font="TkFixedFont")
        self.FromEntry.configure(foreground="#000000")
        self.FromEntry.configure(highlightbackground="#d9d9d9")
        self.FromEntry.configure(highlightcolor="black")
        self.FromEntry.configure(insertbackground="black")
        self.FromEntry.configure(selectbackground="blue")
        self.FromEntry.configure(selectforeground="white")

        self.ToLabel = tk.Label(self.TimeFilterFrame)
        self.ToLabel.place(relx=0.07, rely=0.345, height=40, width=43)
        self.ToLabel.configure(activebackground="#f9f9f9")
        self.ToLabel.configure(activeforeground="black")
        self.ToLabel.configure(anchor='w')
        self.ToLabel.configure(background="#d9d9d9")
        self.ToLabel.configure(compound='left')
        self.ToLabel.configure(disabledforeground="#a3a3a3")
        self.ToLabel.configure(font="-family {David} -size 12")
        self.ToLabel.configure(foreground="#000000")
        self.ToLabel.configure(highlightbackground="#d9d9d9")
        self.ToLabel.configure(highlightcolor="black")
        self.ToLabel.configure(text='''To:''')

        self.ToEntry = tk.Entry(self.TimeFilterFrame)
        self.ToEntry.place(relx=0.486, rely=0.345, height=30, relwidth=0.451)
        self.ToEntry.configure(background="white")
        self.ToEntry.configure(disabledforeground="#a3a3a3")
        self.ToEntry.configure(font="TkFixedFont")
        self.ToEntry.configure(foreground="#000000")
        self.ToEntry.configure(highlightbackground="#d9d9d9")
        self.ToEntry.configure(highlightcolor="black")
        self.ToEntry.configure(insertbackground="black")
        self.ToEntry.configure(selectbackground="blue")
        self.ToEntry.configure(selectforeground="white")

        self.ExplanationLabel = tk.Label(self.TimeFilterFrame)
        self.ExplanationLabel.place(relx=0.07, rely=0.697, height=39, width=121)
        self.ExplanationLabel.configure(activebackground="#f9f9f9")
        self.ExplanationLabel.configure(activeforeground="black")
        self.ExplanationLabel.configure(anchor='w')
        self.ExplanationLabel.configure(background="#d9d9d9")
        self.ExplanationLabel.configure(compound='left')
        self.ExplanationLabel.configure(disabledforeground="#a3a3a3")
        self.ExplanationLabel.configure(font="-family {David} -size 9")
        self.ExplanationLabel.configure(foreground="#000000")
        self.ExplanationLabel.configure(highlightbackground="#d9d9d9")
        self.ExplanationLabel.configure(highlightcolor="black")
        self.ExplanationLabel.configure(text='''Leave Empty for Present''')

        self.ColourFilterFrame = tk.Frame(self.FilterFrame)
        self.ColourFilterFrame.place(relx=0.0, rely=0.396, relheight=0.286
                                     , relwidth=1.0)
        self.ColourFilterFrame.configure(relief='groove')
        self.ColourFilterFrame.configure(borderwidth="2")
        self.ColourFilterFrame.configure(relief="groove")
        self.ColourFilterFrame.configure(background="#d9d9d9")
        self.ColourFilterFrame.configure(highlightbackground="#d9d9d9")
        self.ColourFilterFrame.configure(highlightcolor="black")

        self.ColourLabel = tk.Label(self.ColourFilterFrame)
        self.ColourLabel.place(relx=0.204, rely=0.071, height=64, width=83)
        self.ColourLabel.configure(activebackground="#f9f9f9")
        self.ColourLabel.configure(activeforeground="black")
        self.ColourLabel.configure(background="#d9d9d9")
        self.ColourLabel.configure(compound='left')
        self.ColourLabel.configure(disabledforeground="#a3a3a3")
        self.ColourLabel.configure(font="-family {David} -size 20")
        self.ColourLabel.configure(foreground="#000000")
        self.ColourLabel.configure(highlightbackground="#d9d9d9")
        self.ColourLabel.configure(highlightcolor="black")
        self.ColourLabel.configure(text='''Colour''')

        self.ColourButton = tk.Button(self.ColourFilterFrame)
        self.ColourButton.place(relx=0.141, rely=0.549, height=54, width=107)
        self.ColourButton.configure(activebackground="#ececec")
        self.ColourButton.configure(activeforeground="#000000")
        self.ColourButton.configure(background="#d9d9d9")
        self.ColourButton.configure(compound='left')
        self.ColourButton.configure(disabledforeground="#a3a3a3")
        self.ColourButton.configure(font="-family {David} -size 20")
        self.ColourButton.configure(foreground="#000000")
        self.ColourButton.configure(highlightbackground="#d9d9d9")
        self.ColourButton.configure(highlightcolor="black")
        self.ColourButton.configure(pady="0")
        self.ColourButton.configure(text='''Choose''')

        self.UserFilterFrame = tk.Frame(self.FilterFrame)
        self.UserFilterFrame.place(relx=0.0, rely=0.673, relheight=0.327
                                   , relwidth=1.0)
        self.UserFilterFrame.configure(relief='groove')
        self.UserFilterFrame.configure(borderwidth="2")
        self.UserFilterFrame.configure(relief="groove")
        self.UserFilterFrame.configure(background="#d9d9d9")
        self.UserFilterFrame.configure(highlightbackground="#d9d9d9")
        self.UserFilterFrame.configure(highlightcolor="black")

        self.UserLabel = tk.Label(self.UserFilterFrame)
        self.UserLabel.place(relx=0.07, rely=0.063, height=77, width=121)
        self.UserLabel.configure(activebackground="#f9f9f9")
        self.UserLabel.configure(activeforeground="black")
        self.UserLabel.configure(background="#d9d9d9")
        self.UserLabel.configure(compound='left')
        self.UserLabel.configure(disabledforeground="#a3a3a3")
        self.UserLabel.configure(font="-family {David} -size 20")
        self.UserLabel.configure(foreground="#000000")
        self.UserLabel.configure(highlightbackground="#d9d9d9")
        self.UserLabel.configure(highlightcolor="black")
        self.UserLabel.configure(text='''Users''')

        self.UserButton = tk.Button(self.UserFilterFrame)
        self.UserButton.place(relx=0.141, rely=0.606, height=54, width=107)
        self.UserButton.configure(activebackground="#ececec")
        self.UserButton.configure(activeforeground="#000000")
        self.UserButton.configure(background="#d9d9d9")
        self.UserButton.configure(compound='left')
        self.UserButton.configure(disabledforeground="#a3a3a3")
        self.UserButton.configure(font="-family {David} -size 20")
        self.UserButton.configure(foreground="#000000")
        self.UserButton.configure(highlightbackground="#d9d9d9")
        self.UserButton.configure(highlightcolor="black")
        self.UserButton.configure(pady="0")
        self.UserButton.configure(text='''Choose''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.077, rely=0.136, relheight=0.67, relwidth=0.322)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.StraightButton = tk.Button(self.Frame1)
        self.StraightButton.place(relx=0.0, rely=0.0, height=94, width=87)
        self.StraightButton.configure(activebackground="#ececec")
        self.StraightButton.configure(activeforeground="#000000")
        self.StraightButton.configure(background="#d9d9d9")
        self.StraightButton.configure(compound='left')
        self.StraightButton.configure(disabledforeground="#a3a3a3")
        self.StraightButton.configure(foreground="#000000")
        self.StraightButton.configure(highlightbackground="#d9d9d9")
        self.StraightButton.configure(highlightcolor="black")
        photo_location = "./straightLine.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.StraightButton.configure(image=_img0)
        self.StraightButton.configure(pady="0")

        self.CurvedButton = tk.Button(self.Frame1)
        self.CurvedButton.place(relx=0.0, rely=0.201, height=94, width=87)
        self.CurvedButton.configure(activebackground="#ececec")
        self.CurvedButton.configure(activeforeground="#000000")
        self.CurvedButton.configure(background="#d9d9d9")
        self.CurvedButton.configure(compound='left')
        self.CurvedButton.configure(disabledforeground="#a3a3a3")
        self.CurvedButton.configure(foreground="#000000")
        self.CurvedButton.configure(highlightbackground="#d9d9d9")
        self.CurvedButton.configure(highlightcolor="black")
        photo_location = "./curvedLine.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.CurvedButton.configure(image=_img1)
        self.CurvedButton.configure(pady="0")

        self.RectButton = tk.Button(self.Frame1)
        self.RectButton.place(relx=0.0, rely=0.402, height=94, width=87)
        self.RectButton.configure(activebackground="#ececec")
        self.RectButton.configure(activeforeground="#000000")
        self.RectButton.configure(background="#d9d9d9")
        self.RectButton.configure(compound='left')
        self.RectButton.configure(disabledforeground="#a3a3a3")
        self.RectButton.configure(foreground="#000000")
        self.RectButton.configure(highlightbackground="#d9d9d9")
        self.RectButton.configure(highlightcolor="black")
        photo_location = "./rectangle.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.RectButton.configure(image=_img2)
        self.RectButton.configure(pady="0")

        self.PolyButton = tk.Button(self.Frame1)
        self.PolyButton.place(relx=0.0, rely=0.603, height=94, width=87)
        self.PolyButton.configure(activebackground="#ececec")
        self.PolyButton.configure(activeforeground="#000000")
        self.PolyButton.configure(background="#d9d9d9")
        self.PolyButton.configure(compound='left')
        self.PolyButton.configure(disabledforeground="#a3a3a3")
        self.PolyButton.configure(foreground="#000000")
        self.PolyButton.configure(highlightbackground="#d9d9d9")
        self.PolyButton.configure(highlightcolor="black")
        photo_location = "./polyhedron.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.PolyButton.configure(image=_img3)
        self.PolyButton.configure(pady="0")

        self.CircleButton = tk.Button(self.Frame1)
        self.CircleButton.place(relx=0.0, rely=0.804, height=94, width=87)
        self.CircleButton.configure(activebackground="#ececec")
        self.CircleButton.configure(activeforeground="#000000")
        self.CircleButton.configure(background="#d9d9d9")
        self.CircleButton.configure(compound='left')
        self.CircleButton.configure(cursor="fleur")
        self.CircleButton.configure(disabledforeground="#a3a3a3")
        self.CircleButton.configure(foreground="#000000")
        self.CircleButton.configure(highlightbackground="#d9d9d9")
        self.CircleButton.configure(highlightcolor="black")
        photo_location = "./circle.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.CircleButton.configure(image=_img4)
        self.CircleButton.configure(pady="0")

        self.ParamButton = tk.Button(self.top)
        self.ParamButton.place(relx=0.077, rely=0.818, height=94, width=89)
        self.ParamButton.configure(activebackground="#ececec")
        self.ParamButton.configure(activeforeground="#000000")
        self.ParamButton.configure(background="#d9d9d9")
        self.ParamButton.configure(compound='left')
        self.ParamButton.configure(disabledforeground="#a3a3a3")
        self.ParamButton.configure(foreground="#000000")
        self.ParamButton.configure(highlightbackground="#d9d9d9")
        self.ParamButton.configure(highlightcolor="black")
        photo_location = "./painter.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.ParamButton.configure(image=_img5)
        self.ParamButton.configure(pady="0")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


if __name__ == '__main__':
    root = tkinter.Tk()
    t = Toplevel1(root)
    root.mainloop()