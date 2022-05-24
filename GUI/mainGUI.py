#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 23, 2022 02:05:48 PM +0200  platform: Windows NT
import ast
import select
import sys
import time
import tkinter
import tkinter as tk
import json
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF, renderPM
# from PIL import Image, ImageTk



# import mainGUI_support
from GUI import BrushSelectGUI, ColourFilterGUI, UserFilterGUI


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

        self.start = time.time()

        self.Drawings = []  # This will be updated as people draw
        self.drawn_drawings = []  # Used to remember which drawings have already been rendered, to not redraw everything
        self.brush = "lineS"  # The current brush
        self.colour = '#000000'  # The current color
        self.fill = '#ffffff'  # The current fill
        self.width = 5
        self.mouseCoords = []  # Used for multi-stroke drawing
        self.blacklist = []

        self.time_var = tk.IntVar()
        self.colour_var = tk.IntVar()
        self.user_var = tk.IntVar()
        self.all_filter_var = tk.IntVar()

        self.colour_filter_list = []
        self.user_filter_list = []

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

        self.TimeFilterCheck = tk.Checkbutton(self.TimeFilterFrame)
        self.TimeFilterCheck.place(relx=0.069, rely=0.522, relheight=0.217, relwidth = 0.421)
        self.TimeFilterCheck.configure(activebackground="#ececec")
        self.TimeFilterCheck.configure(activeforeground="#000000")
        self.TimeFilterCheck.configure(anchor='w')
        self.TimeFilterCheck.configure(background="#d9d9d9")
        self.TimeFilterCheck.configure(compound='left')
        self.TimeFilterCheck.configure(disabledforeground="#a3a3a3")
        self.TimeFilterCheck.configure(foreground="#000000")
        self.TimeFilterCheck.configure(highlightbackground="#d9d9d9")
        self.TimeFilterCheck.configure(highlightcolor="black")
        self.TimeFilterCheck.configure(justify='left')
        self.TimeFilterCheck.configure(selectcolor="#d9d9d9")
        self.TimeFilterCheck.configure(text='''Active''')
        self.TimeFilterCheck.configure(variable=self.time_var)

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
        self.ColourButton.configure(command=lambda :self.open_colour_filter())

        self.ColourFilterCheck = tk.Checkbutton(self.ColourFilterFrame)
        self.ColourFilterCheck.place(relx=0.276, rely=0.345, relheight=0.172, relwidth = 0.421)
        self.ColourFilterCheck.configure(activebackground="#ececec")
        self.ColourFilterCheck.configure(activeforeground="#000000")
        self.ColourFilterCheck.configure(anchor='w')
        self.ColourFilterCheck.configure(background="#d9d9d9")
        self.ColourFilterCheck.configure(compound='left')
        self.ColourFilterCheck.configure(disabledforeground="#a3a3a3")
        self.ColourFilterCheck.configure(foreground="#000000")
        self.ColourFilterCheck.configure(highlightbackground="#d9d9d9")
        self.ColourFilterCheck.configure(highlightcolor="black")
        self.ColourFilterCheck.configure(justify='left')
        self.ColourFilterCheck.configure(selectcolor="#d9d9d9")
        self.ColourFilterCheck.configure(text='''Active''')
        self.ColourFilterCheck.configure(variable=self.colour_var)

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
        self.UserButton.configure(command=lambda :self.open_user_filter())

        self.UserFilterCheck = tk.Checkbutton(self.UserFilterFrame)
        self.UserFilterCheck.place(relx=0.276, rely=0.424, relheight=0.152, relwidth = 0.421)
        self.UserFilterCheck.configure(activebackground="#ececec")
        self.UserFilterCheck.configure(activeforeground="#000000")
        self.UserFilterCheck.configure(anchor='w')
        self.UserFilterCheck.configure(background="#d9d9d9")
        self.UserFilterCheck.configure(compound='left')
        self.UserFilterCheck.configure(disabledforeground="#a3a3a3")
        self.UserFilterCheck.configure(foreground="#000000")
        self.UserFilterCheck.configure(highlightbackground="#d9d9d9")
        self.UserFilterCheck.configure(highlightcolor="black")
        self.UserFilterCheck.configure(justify='left')
        self.UserFilterCheck.configure(selectcolor="#d9d9d9")
        self.UserFilterCheck.configure(text='''Active''')
        self.UserFilterCheck.configure(variable=self.user_var)

        self.ActivateAllFilter = tk.Checkbutton(self.FilterFrame)
        self.ActivateAllFilter.place(relx=0.207, rely=0.119, relheight=0.05, relwidth = 0.559)
        self.ActivateAllFilter.configure(activebackground="#ececec")
        self.ActivateAllFilter.configure(activeforeground="#000000")
        self.ActivateAllFilter.configure(anchor='w')
        self.ActivateAllFilter.configure(background="#d9d9d9")
        self.ActivateAllFilter.configure(compound='left')
        self.ActivateAllFilter.configure(disabledforeground="#a3a3a3")
        self.ActivateAllFilter.configure(foreground="#000000")
        self.ActivateAllFilter.configure(highlightbackground="#d9d9d9")
        self.ActivateAllFilter.configure(highlightcolor="black")
        self.ActivateAllFilter.configure(justify='left')
        self.ActivateAllFilter.configure(selectcolor="#d9d9d9")
        self.ActivateAllFilter.configure(text='''Active All''')
        self.ActivateAllFilter.configure(variable=self.all_filter_var)

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
            self.name = self.net.username
            self.top.after(100, lambda: self.client_update())
        else:
            self.name = self.net.client_name
            self.top.protocol("WM_DELETE_WINDOW", lambda : self.exit_protocol())
            """if self.net.bg_file_destination != '':
                self.set_as_bg(self.net.bg_file_destination)"""
            self.top.after(100, lambda: self.lobby_update())

    def exit_protocol(self):
        self.net.exit_protocol()
        self.top.destroy()

    def change_filters(self, time, colour, user):
        # updates self.blacklist
        for drawing in self.Drawings:
            if drawing[0] not in self.blacklist:
                if time == 1:
                    drawing_time = drawing[4]
                    if len(self.FromEntry.get()) > 0:
                        print("From time: "+str(self.FromEntry.get()))
                        if drawing_time < float(self.FromEntry.get()):
                            print(str(drawing) + "Added to blacklist")
                            self.blacklist += drawing
                    if len(self.ToEntry.get()) > 0:
                        if drawing_time > float(self.ToEntry.get()):
                            print(str(drawing) + "Added to blacklist")
                            self.blacklist += drawing
                if colour == 1:
                    drawing_outline = drawing[1]
                    if drawing_outline in self.colour_filter_list:
                        print(str(drawing) + "Added to blacklist")
                        self.blacklist += drawing
                if user == 1:
                    drawing_user = drawing[5]
                    if drawing_user in self.user_filter_list:
                        print(str(drawing) + "Added to blacklist")
                        self.blacklist += drawing

        self.drawn_drawings = []
        self.Canvas.delete('all')

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
                Drawing = [[self.brush, self.colour, self.fill, self.width,
                            time.time()-self.start, self.name, self.mouseCoords]]
                Drawing_string = json.dumps(Drawing)
                if self.status == "c":  # We're a client
                    self.net.my_socket.send(("D"+Drawing_string).encode())
                else:
                    self.net.update_clients(Drawing_string)
                self.Drawings += Drawing
                self.mouseCoords = []
        if mouse_click == 2:
            if self.brush == "poly" or self.brush == "lineC":
                Drawing = [[self.brush, self.colour, self.fill, self.width,
                            time.time()-self.start, self.name, self.mouseCoords]]
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
        print("Blacklist: "+str(self.blacklist))
        print("Drawn Drawings: "+str(self.drawn_drawings))
        if self.all_filter_var.get() == 1:
            self.user_var.set(1)
            self.colour_var.set(1)
            self.time_var.set(1)
            self.all_filter_var.set(0)
        if self.user_var.get() == 1 or self.colour_var.get() == 1 or self.time_var.get() == 1:
            print("Changing Filters")
            self.change_filters(user=self.user_var.get(), colour=self.colour_var.get(), time=self.time_var.get())
        self.Drawings = [self.Drawings[x] for x in range(len(self.Drawings)) if not(self.Drawings[x] in self.Drawings[:x])]
        print("Drawing...")
        print(self.Drawings)
        for drawing in self.Drawings:
            if drawing[0] not in self.drawn_drawings and drawing[0] not in self.blacklist:
                # New drawing, draw it
                print(str(drawing) + "Drawn")
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
                self.drawn_drawings += drawing
        self.blacklist = []
        self.top.after(100, lambda: self.update())

    def client_update(self):
        self.rlist, wlist, xlist = select.select([self.net.my_socket], [], [], 0.01)
        for current_socket in self.rlist:
            command = current_socket.recv(1).decode()
            if command == "B":  # recieve full svg file, set as background
                length_of_lengths = current_socket.recv(4).decode()
                message_length = int(current_socket.recv(int(length_of_lengths)).decode())
                f = open('saved.svg', 'wb')
                f.write(''.encode())
                f.close()
                f = open('saved.svg', 'ab')
                while not message_length == 0:
                    if message_length <= 9999:
                        data = current_socket.recv(message_length)
                        f.write(data)
                        break
                    data = current_socket.recv(9999)
                    f.write(data)
                    print("handling...")
                    message_length -= 9999
                f.close()
            elif command != "L":
                # In this case, command is not a command, but part of the drawing,
                # and as such it should be appended at the start of new_drawing_string
                new_drawing_string = command + current_socket.recv(4096).decode()
                print("New Drawing: "+new_drawing_string)
                new_drawing = json.loads(new_drawing_string)
                self.Drawings += new_drawing
            else:
                names = current_socket.recv(4096).decode()
                self.net.parse_connected_clients(names)
        self.top.after(1000, lambda: self.client_update())

    """def set_as_bg(self, file_dest):
        img = SvgImage(master=self.top, file=file_dest, scale=1)
        self.Canvas.create_image(0,0,anchor='nw',image=img)
        #self.Canvas.create_image(int(self.Canvas.winfo_width() / 2), int(self.Canvas.winfo_height() / 2), image=pimg)
    """

    def lobby_update(self):
        self.Drawings = self.net.get_data()
        self.top.after(100, lambda: self.lobby_update())

    def changeBrush(self, new_brush):
        self.brush = new_brush

    def open_colour_filter(self):
        to = tk.Toplevel(self.top)
        colour_filter = ColourFilterGUI.Toplevel1(top=to, current_colours=self.colour_filter_list)
        self.top.after(100, lambda: self.await_colour_filter_list(colour_filter))

    def await_colour_filter_list(self, colour_gui):
        self.colour_filter_list = colour_gui.colour_list
        self.top.after(100, lambda: self.await_colour_filter_list(colour_gui))

    def open_user_filter(self):
        if self.status == "c":
            self.net.get_connected_Clients()
            self.top.after(100, lambda :self.wait_for_clients_user_list())
        else:
            client_list = ast.literal_eval(self.net.send_names())
            print(client_list)
            to = tk.Toplevel(self.top)
            user_filter = UserFilterGUI.Toplevel1(top=to, all_users=client_list, current_users=self.user_filter_list)
            self.top.after(100, lambda :self.await_user_filter_list(user_filter))

    def wait_for_clients_user_list(self):
        if self.net.changed == 1:
            self.net.changed = 0
            client_list = self.net.client_name_list
            print(client_list)
            to = tk.Toplevel(self.top)
            user_filter = UserFilterGUI.Toplevel1(top=to, all_users=client_list, current_users=self.user_filter_list)
            self.top.after(100, lambda: self.await_user_filter_list(user_filter))
        else:
            self.top.after(100, lambda :self.wait_for_clients_user_list())

    def await_user_filter_list(self, user_gui):
        self.user_filter_list = user_gui.user_list
        self.top.after(100, lambda: self.await_user_filter_list(user_gui))

    def open_brush_params(self):
        to = tk.Toplevel(self.top)
        brush_select = BrushSelectGUI.Toplevel1(top=to, outline_colour=self.colour, fill_colour=self.fill, width=self.width)
        self.top.after(100, lambda :self.await_brush_change(brush_select))

    def await_brush_change(self, t):
        if t.Changed == 1:
            self.width = t.Width
            self.fill = t.FillC
            self.colour = t.LineC
            t.Changed = 0
        self.top.after(100, lambda :self.await_brush_change(t))

"""class SvgImage(tk.PhotoImage):
    Widget which can display images in PGM, PPM, GIF, PNG format.
    _tksvg_loaded = False
    _svg_options = ['scale', 'scaletowidth', 'scaletoheight']

    def __init__(self, name=None, cnf={}, master=None, **kw):
        # load tksvg
        if not SvgImage._tksvg_loaded:
            if master is None:
                master = tk._default_root
                if not master:
                    raise RuntimeError('Too early to create image')
            # master.tk.eval('package require tksvg')
            SvgImage._tksvg_loaded = True
        # remove specific svg options from keywords
        svgkw = {opt: kw.pop(opt, None) for opt in self._svg_options}
        tk.PhotoImage.__init__(self, name, cnf, master, **kw)
        # pass svg options
        self.configure(**svgkw)

    def configure(self, **kw):
        svgkw = {opt: kw.pop(opt) for opt in self._svg_options if opt in kw}
        # non svg options
        if kw:
            tk.PhotoImage.configure(self, **kw)
        # svg options
        options = ()
        for k, v in svgkw.items():
            if v is not None:
                options = options + ('-'+k, str(v))
        self.tk.eval('%s configure -format {svg %s}' % (self.name, ' '.join(options)))











This was part of a cut Feature: Adding svg files as background
unfortunately, reading the svg file using svg2rlg caused an obscure error when on mainGUI
(As there were no errors when the same method was used in test.py), 
and the obscure error had only 4 results come up when searched, none of which were relevent

The above class also did not work, as it did not detect the package tksvg even after said package was downloaded.

As such, I saw no way to Implement svg backgrounds. The button is still there on the lobbymanagerGUI,
but it will not effect the drawing in any way
"""

# def start_up():
#     mainGUI_support.main()

if __name__ == '__main__':
    root = tkinter.Tk()
    t = Toplevel1(root)
    root.mainloop()
