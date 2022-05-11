#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 23, 2022 02:05:48 PM +0200  platform: Windows NT
import select
import sys
import tkinter
import tkinter as tk
import json
import tkinter.ttk as ttk
from tkinter.constants import *


# import mainGUI_support
from GUI import BrushSelectGUI


class Toplevel1:
    def __init__(self, top: tk.Tk = None, params=None):
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

        top.geometry("885x531+479+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Project")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Drawings = []  # This will be updated as people draw
        self.drawn_drawings = []  # Used to remember which drawings have already been rendered, to not redraw everything
        self.brush = "lineS"  # The current brush
        self.colour = '#000000'  # The current color
        self.fill = '#ffffff'  # The current fill
        self.width = 5
        self.mouseCoords = []  # Used for multi-stroke drawing

        if params[0]:
            self.net = params[0]  # Either a lobby or a client
        if params[1]:
            self.status = params[1]  # Whether we are a lobby or a client

        self.top = top

        self.Canvas = tk.Canvas(self.top)
        self.Canvas.place(relx=0.102, rely=0.019, relheight=0.947
                          , relwidth=0.715)
        self.Canvas.configure(background="#d9d9d9")
        self.Canvas.configure(borderwidth="2")
        self.Canvas.configure(highlightbackground="#d9d9d9")
        self.Canvas.configure(highlightcolor="black")
        self.Canvas.configure(insertbackground="black")
        self.Canvas.configure(relief="ridge")
        self.Canvas.configure(selectbackground="blue")
        self.Canvas.configure(selectforeground="white")
        self.Canvas.bind('<Button-1>', lambda x: self.draw(1))
        self.Canvas.bind('<Button-3>', lambda x: self.draw(2))

        self.FilterFrame = tk.Frame(self.top)
        self.FilterFrame.place(relx=0.825, rely=0.019, relheight=0.951
                               , relwidth=0.164)
        self.FilterFrame.configure(relief='groove')
        self.FilterFrame.configure(borderwidth="2")
        self.FilterFrame.configure(relief="groove")
        self.FilterFrame.configure(background="#d9d9d9")
        self.FilterFrame.configure(highlightbackground="#d9d9d9")
        self.FilterFrame.configure(highlightcolor="black")

        self.FilterLabel = tk.Label(self.FilterFrame)
        self.FilterLabel.place(relx=0.069, rely=0.02, height=81, width=124)
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
        self.FromLabel.place(relx=0.069, rely=0.087, height=31, width=54)
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
        self.FromEntry.place(relx=0.483, rely=0.087, height=30, relwidth=0.441)
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
        self.ToLabel.place(relx=0.069, rely=0.348, height=31, width=44)
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
        self.ToEntry.place(relx=0.483, rely=0.348, height=30, relwidth=0.441)
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
        self.ExplanationLabel.place(relx=0.069, rely=0.696, height=31, width=124)

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
        self.ColourFilterFrame.place(relx=0.0, rely=0.396, relheight=0.287
                                     , relwidth=1.0)
        self.ColourFilterFrame.configure(relief='groove')
        self.ColourFilterFrame.configure(borderwidth="2")
        self.ColourFilterFrame.configure(relief="groove")
        self.ColourFilterFrame.configure(background="#d9d9d9")
        self.ColourFilterFrame.configure(highlightbackground="#d9d9d9")
        self.ColourFilterFrame.configure(highlightcolor="black")

        self.ColourLabel = tk.Label(self.ColourFilterFrame)
        self.ColourLabel.place(relx=0.207, rely=0.069, height=51, width=84)
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
        self.ColourButton.place(relx=0.138, rely=0.552, height=54, width=107)
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
        self.UserLabel.place(relx=0.069, rely=0.061, height=61, width=124)
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
        self.UserButton.place(relx=0.138, rely=0.606, height=54, width=107)
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
        self.Frame1.place(relx=0.0, rely=0.038, relheight=0.838, relwidth=0.096)
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
        self.StraightButton.configure(command=lambda: self.changeBrush("lineS"))
        photo_location = "./straightLine.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.StraightButton.configure(image=_img0)
        self.StraightButton.configure(pady="0")

        self.CurvedButton = tk.Button(self.Frame1)
        self.CurvedButton.place(relx=0.0, rely=0.202, height=94, width=87)
        self.CurvedButton.configure(activebackground="#ececec")
        self.CurvedButton.configure(activeforeground="#000000")
        self.CurvedButton.configure(background="#d9d9d9")
        self.CurvedButton.configure(compound='left')
        self.CurvedButton.configure(disabledforeground="#a3a3a3")
        self.CurvedButton.configure(foreground="#000000")
        self.CurvedButton.configure(highlightbackground="#d9d9d9")
        self.CurvedButton.configure(highlightcolor="black")
        self.CurvedButton.configure(command=lambda: self.changeBrush("lineC"))
        photo_location = "./curvedLine.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.CurvedButton.configure(image=_img1)
        self.CurvedButton.configure(pady="0")

        self.RectButton = tk.Button(self.Frame1)
        self.RectButton.place(relx=0.0, rely=0.404, height=94, width=87)
        self.RectButton.configure(activebackground="#ececec")
        self.RectButton.configure(activeforeground="#000000")
        self.RectButton.configure(background="#d9d9d9")
        self.RectButton.configure(compound='left')
        self.RectButton.configure(disabledforeground="#a3a3a3")
        self.RectButton.configure(foreground="#000000")
        self.RectButton.configure(highlightbackground="#d9d9d9")
        self.RectButton.configure(highlightcolor="black")
        self.RectButton.configure(command=lambda: self.changeBrush("rect"))
        photo_location = "./rectangle.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.RectButton.configure(image=_img2)
        self.RectButton.configure(pady="0")

        self.PolyButton = tk.Button(self.Frame1)
        self.PolyButton.place(relx=0.0, rely=0.607, height=94, width=87)
        self.PolyButton.configure(activebackground="#ececec")
        self.PolyButton.configure(activeforeground="#000000")
        self.PolyButton.configure(background="#d9d9d9")
        self.PolyButton.configure(compound='left')
        self.PolyButton.configure(disabledforeground="#a3a3a3")
        self.PolyButton.configure(foreground="#000000")
        self.PolyButton.configure(highlightbackground="#d9d9d9")
        self.PolyButton.configure(highlightcolor="black")
        self.PolyButton.configure(command=lambda: self.changeBrush("poly"))
        photo_location = "./polyhedron.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.PolyButton.configure(image=_img3)
        self.PolyButton.configure(pady="0")

        self.CircleButton = tk.Button(self.Frame1)
        self.CircleButton.place(relx=0.0, rely=0.809, height=94, width=87)
        self.CircleButton.configure(activebackground="#ececec")
        self.CircleButton.configure(activeforeground="#000000")
        self.CircleButton.configure(background="#d9d9d9")
        self.CircleButton.configure(compound='left')
        self.CircleButton.configure(disabledforeground="#a3a3a3")
        self.CircleButton.configure(foreground="#000000")
        self.CircleButton.configure(highlightbackground="#d9d9d9")
        self.CircleButton.configure(highlightcolor="black")
        self.CircleButton.configure(command=lambda: self.changeBrush("oval"))
        photo_location = "./circle.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.CircleButton.configure(image=_img4)
        self.CircleButton.configure(pady="0")

        self.ParamButton = tk.Button(self.top)
        self.ParamButton.place(relx=0.723, rely=0.791, height=84, width=79)
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
        self.ParamButton.configure(command=lambda: self.open_brush_params())

        self.update()
        if self.status == "c":
            self.top.after(100, lambda: self.client_update())
        else:
            self.net.get_gui_drawing(self.Drawings)

    def draw(self, mouse_click):
        """
        This Function adds one drawing to the self.drawings object through detecting mouse position at the time of click

        In the case of a polyhedron, the program will continue to record the mouse clicks as vertices of the polyhedron
        until mouse 2 is pressed, at which point the polyhedron will be drawn

        In the case of a curved Line, the program will record the mouse clicks as splines of the line until mouse 2 is
        pressed, at which point the curve will be drawn

        In all other cases, only 2 clicks with mouse 1 are necessary

        In order to know which mouse button was pressed, the mouse_click parameter is used with either 1 or 2 for
        the 2 mouse buttons
        """
        print("Mouse Clicked")
        if mouse_click == 1:
            self.mouseCoords += [list((self.top.winfo_pointerx()-self.top.winfo_rootx()-self.Canvas.winfo_x(),
                                       self.top.winfo_pointery()-self.top.winfo_rooty()-self.Canvas.winfo_y()))]
            if len(self.mouseCoords) == 2 and self.brush != "poly" and self.brush != "lineC":
                Drawing = [[self.brush, self.colour, self.fill, self.width, self.mouseCoords]]
                Drawing_string = json.dumps(Drawing)
                if self.status == "c":  # We're a client
                    self.net.my_socket.send(("D"+Drawing_string).encode())
                else:
                    self.net.update_clients(Drawing_string)
                self.Drawings += Drawing
                self.mouseCoords = []
        if mouse_click == 2:
            if self.brush == "poly" or self.brush == "lineC":
                Drawing = [[self.brush, self.colour, self.fill, self.width, self.mouseCoords]]
                Drawing_string = json.dumps(Drawing)
                if self.status == "c":  # We're a client
                    self.net.my_socket.send(("D" + Drawing_string).encode())
                else:
                    self.net.update_clients(Drawing_string)
                self.Drawings += Drawing
                self.mouseCoords = []

    def update(self):
        """
        This function renders all drawings in the self.drawings list that arent already drawn
        """
        self.Drawings=[self.Drawings[x] for x in range(len(self.Drawings)) if not(self.Drawings[x] in self.Drawings[:x])]
        print("Drawing...")
        print(self.Drawings)
        for drawing in self.Drawings:
            if drawing not in self.drawn_drawings:
                # New drawing, draw it
                print(drawing)
                b = drawing[0]  # brush
                if b == "oval":
                    self.Canvas.create_oval(drawing[-1:][0], fill=drawing[2], outline=drawing[1], width=drawing[3])
                if b == "rect":
                    self.Canvas.create_rectangle(drawing[-1:][0], fill=drawing[2], outline=drawing[1], width=drawing[3])
                if b == "lineS":
                    self.Canvas.create_line(drawing[-1:][0], fill=drawing[1], width=drawing[3])
                if b == "poly":
                    self.Canvas.create_polygon(drawing[-1:][0], fill=drawing[2], width=drawing[3], outline=drawing[1])
                if b == "lineC":
                    self.Canvas.create_line(drawing[-1:][0], fill=drawing[1], width=drawing[3], smooth=True)
                self.drawn_drawings += [drawing]
        self.top.after(1000, lambda: self.update())

    def client_update(self):
        self.rlist, wlist, xlist = select.select([self.net.my_socket], [], [], 0.01)
        for current_socket in self.rlist:
            new_drawing_string = current_socket.recv(1024).decode()
            print("New Drawing: "+new_drawing_string)
            new_drawing = json.loads(new_drawing_string)
            self.Drawings += new_drawing
        self.top.after(1000, lambda: self.client_update())

    def changeBrush(self, new_brush):
        self.brush = new_brush

    def open_brush_params(self):
        to = tk.Toplevel(self.top)
        t = BrushSelectGUI.Toplevel1(top=to, outline_colour=self.colour, fill_colour=self.fill, width=self.width)
        self.top.after(100, lambda :self.await_brush_change(t))

    def await_brush_change(self, t):
        if t.Changed == 1:
            self.width = t.Width
            self.fill = t.FillC
            self.colour = t.LineC
            t.Changed = 0
        self.top.after(100, lambda :self.await_brush_change(t))


# def start_up():
#     mainGUI_support.main()

if __name__ == '__main__':
    root = tkinter.Tk()
    t = Toplevel1(root)
    root.mainloop()
