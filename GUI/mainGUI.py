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

        self.drawings = []  # This will be updated as people draw
        self.drawn_drawings = []  # Used to remember which drawings have already been rendered, to not redraw everything
        self.brush = "lineS"  # The current brush
        self.colour = '#000000'  # The current color
        self.fill = '#ffffff'  # The current fill
        self.width = 5
        self.mouse_coords = []  # Used for multi-stroke drawing
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

        self.canvas = tk.Canvas(self.top)
        self.canvas.place(relx=0.102, rely=0.019, relheight=0.947
                          , relwidth=0.715)
        self.canvas.configure(background="#d9d9d9")
        self.canvas.configure(borderwidth="2")
        self.canvas.configure(highlightbackground="#d9d9d9")
        self.canvas.configure(highlightcolor="black")
        self.canvas.configure(insertbackground="black")
        self.canvas.configure(relief="ridge")
        self.canvas.configure(selectbackground="blue")
        self.canvas.configure(selectforeground="white")
        self.canvas.bind('<Button-1>', lambda x: self.draw(1))
        self.canvas.bind('<Button-3>', lambda x: self.draw(2))

        self.filter_frame = tk.Frame(self.top)
        self.filter_frame.place(relx=0.825, rely=0.019, relheight=0.951
                                , relwidth=0.164)
        self.filter_frame.configure(relief='groove')
        self.filter_frame.configure(borderwidth="2")
        self.filter_frame.configure(relief="groove")
        self.filter_frame.configure(background="#d9d9d9")
        self.filter_frame.configure(highlightbackground="#d9d9d9")
        self.filter_frame.configure(highlightcolor="black")

        self.filter_label = tk.Label(self.filter_frame)
        self.filter_label.place(relx=0.069, rely=0.02, height=81, width=124)
        self.filter_label.configure(activebackground="#f9f9f9")
        self.filter_label.configure(activeforeground="black")
        self.filter_label.configure(background="#d9d9d9")
        self.filter_label.configure(disabledforeground="#a3a3a3")
        self.filter_label.configure(font="-family {David} -size 20")
        self.filter_label.configure(foreground="#000000")
        self.filter_label.configure(highlightbackground="#d9d9d9")
        self.filter_label.configure(highlightcolor="black")
        self.filter_label.configure(text='''Filters''')

        self.time_filter_frame = tk.Frame(self.filter_frame)
        self.time_filter_frame.place(relx=0.0, rely=0.178, relheight=0.228
                                     , relwidth=1.0)
        self.time_filter_frame.configure(relief='groove')
        self.time_filter_frame.configure(borderwidth="2")
        self.time_filter_frame.configure(relief="groove")
        self.time_filter_frame.configure(background="#d9d9d9")
        self.time_filter_frame.configure(highlightbackground="#d9d9d9")
        self.time_filter_frame.configure(highlightcolor="black")

        self.from_label = tk.Label(self.time_filter_frame)
        self.from_label.place(relx=0.069, rely=0.087, height=31, width=54)
        self.from_label.configure(activebackground="#f9f9f9")
        self.from_label.configure(activeforeground="black")
        self.from_label.configure(anchor='w')
        self.from_label.configure(background="#d9d9d9")
        self.from_label.configure(compound='left')
        self.from_label.configure(disabledforeground="#a3a3a3")
        self.from_label.configure(font="-family {David} -size 12")
        self.from_label.configure(foreground="#000000")
        self.from_label.configure(highlightbackground="#d9d9d9")
        self.from_label.configure(highlightcolor="black")
        self.from_label.configure(text='''From:''')

        self.from_entry = tk.Entry(self.time_filter_frame)
        self.from_entry.place(relx=0.483, rely=0.087, height=30, relwidth=0.441)
        self.from_entry.configure(background="white")
        self.from_entry.configure(disabledforeground="#a3a3a3")
        self.from_entry.configure(font="TkFixedFont")
        self.from_entry.configure(foreground="#000000")
        self.from_entry.configure(highlightbackground="#d9d9d9")
        self.from_entry.configure(highlightcolor="black")
        self.from_entry.configure(insertbackground="black")
        self.from_entry.configure(selectbackground="blue")
        self.from_entry.configure(selectforeground="white")

        self.to_label = tk.Label(self.time_filter_frame)
        self.to_label.place(relx=0.069, rely=0.348, height=31, width=44)
        self.to_label.configure(activebackground="#f9f9f9")
        self.to_label.configure(activeforeground="black")
        self.to_label.configure(anchor='w')
        self.to_label.configure(background="#d9d9d9")
        self.to_label.configure(compound='left')
        self.to_label.configure(disabledforeground="#a3a3a3")
        self.to_label.configure(font="-family {David} -size 12")
        self.to_label.configure(foreground="#000000")
        self.to_label.configure(highlightbackground="#d9d9d9")
        self.to_label.configure(highlightcolor="black")
        self.to_label.configure(text='''To:''')

        self.to_entry = tk.Entry(self.time_filter_frame)
        self.to_entry.place(relx=0.483, rely=0.348, height=30, relwidth=0.441)
        self.to_entry.configure(background="white")
        self.to_entry.configure(disabledforeground="#a3a3a3")
        self.to_entry.configure(font="TkFixedFont")
        self.to_entry.configure(foreground="#000000")
        self.to_entry.configure(highlightbackground="#d9d9d9")
        self.to_entry.configure(highlightcolor="black")
        self.to_entry.configure(insertbackground="black")
        self.to_entry.configure(selectbackground="blue")
        self.to_entry.configure(selectforeground="white")

        self.explanation_label = tk.Label(self.time_filter_frame)
        self.explanation_label.place(relx=0.069, rely=0.696, height=31, width=124)

        self.explanation_label.configure(activebackground="#f9f9f9")
        self.explanation_label.configure(activeforeground="black")
        self.explanation_label.configure(anchor='w')
        self.explanation_label.configure(background="#d9d9d9")
        self.explanation_label.configure(compound='left')
        self.explanation_label.configure(disabledforeground="#a3a3a3")
        self.explanation_label.configure(font="-family {David} -size 9")
        self.explanation_label.configure(foreground="#000000")
        self.explanation_label.configure(highlightbackground="#d9d9d9")
        self.explanation_label.configure(highlightcolor="black")
        self.explanation_label.configure(text='''Leave Empty for Present''')

        self.time_filter_check = tk.Checkbutton(self.time_filter_frame)
        self.time_filter_check.place(relx=0.069, rely=0.522, relheight=0.217, relwidth=0.421)
        self.time_filter_check.configure(activebackground="#ececec")
        self.time_filter_check.configure(activeforeground="#000000")
        self.time_filter_check.configure(anchor='w')
        self.time_filter_check.configure(background="#d9d9d9")
        self.time_filter_check.configure(compound='left')
        self.time_filter_check.configure(disabledforeground="#a3a3a3")
        self.time_filter_check.configure(foreground="#000000")
        self.time_filter_check.configure(highlightbackground="#d9d9d9")
        self.time_filter_check.configure(highlightcolor="black")
        self.time_filter_check.configure(justify='left')
        self.time_filter_check.configure(selectcolor="#d9d9d9")
        self.time_filter_check.configure(text='''Active''')
        self.time_filter_check.configure(variable=self.time_var)

        self.colour_filter_frame = tk.Frame(self.filter_frame)
        self.colour_filter_frame.place(relx=0.0, rely=0.396, relheight=0.287
                                       , relwidth=1.0)
        self.colour_filter_frame.configure(relief='groove')
        self.colour_filter_frame.configure(borderwidth="2")
        self.colour_filter_frame.configure(relief="groove")
        self.colour_filter_frame.configure(background="#d9d9d9")
        self.colour_filter_frame.configure(highlightbackground="#d9d9d9")
        self.colour_filter_frame.configure(highlightcolor="black")

        self.colour_label = tk.Label(self.colour_filter_frame)
        self.colour_label.place(relx=0.207, rely=0.069, height=51, width=84)
        self.colour_label.configure(activebackground="#f9f9f9")
        self.colour_label.configure(activeforeground="black")
        self.colour_label.configure(background="#d9d9d9")
        self.colour_label.configure(compound='left')
        self.colour_label.configure(disabledforeground="#a3a3a3")
        self.colour_label.configure(font="-family {David} -size 20")
        self.colour_label.configure(foreground="#000000")
        self.colour_label.configure(highlightbackground="#d9d9d9")
        self.colour_label.configure(highlightcolor="black")
        self.colour_label.configure(text='''Colour''')

        self.colour_button = tk.Button(self.colour_filter_frame)
        self.colour_button.place(relx=0.138, rely=0.552, height=54, width=107)
        self.colour_button.configure(activebackground="#ececec")
        self.colour_button.configure(activeforeground="#000000")
        self.colour_button.configure(background="#d9d9d9")
        self.colour_button.configure(compound='left')
        self.colour_button.configure(disabledforeground="#a3a3a3")
        self.colour_button.configure(font="-family {David} -size 20")
        self.colour_button.configure(foreground="#000000")
        self.colour_button.configure(highlightbackground="#d9d9d9")
        self.colour_button.configure(highlightcolor="black")
        self.colour_button.configure(pady="0")
        self.colour_button.configure(text='''Choose''')
        self.colour_button.configure(command=lambda: self.open_colour_filter())

        self.colour_filter_check = tk.Checkbutton(self.colour_filter_frame)
        self.colour_filter_check.place(relx=0.276, rely=0.345, relheight=0.172, relwidth=0.421)
        self.colour_filter_check.configure(activebackground="#ececec")
        self.colour_filter_check.configure(activeforeground="#000000")
        self.colour_filter_check.configure(anchor='w')
        self.colour_filter_check.configure(background="#d9d9d9")
        self.colour_filter_check.configure(compound='left')
        self.colour_filter_check.configure(disabledforeground="#a3a3a3")
        self.colour_filter_check.configure(foreground="#000000")
        self.colour_filter_check.configure(highlightbackground="#d9d9d9")
        self.colour_filter_check.configure(highlightcolor="black")
        self.colour_filter_check.configure(justify='left')
        self.colour_filter_check.configure(selectcolor="#d9d9d9")
        self.colour_filter_check.configure(text='''Active''')
        self.colour_filter_check.configure(variable=self.colour_var)

        self.user_filter_frame = tk.Frame(self.filter_frame)
        self.user_filter_frame.place(relx=0.0, rely=0.673, relheight=0.327
                                     , relwidth=1.0)
        self.user_filter_frame.configure(relief='groove')
        self.user_filter_frame.configure(borderwidth="2")
        self.user_filter_frame.configure(relief="groove")
        self.user_filter_frame.configure(background="#d9d9d9")
        self.user_filter_frame.configure(highlightbackground="#d9d9d9")
        self.user_filter_frame.configure(highlightcolor="black")

        self.user_label = tk.Label(self.user_filter_frame)
        self.user_label.place(relx=0.069, rely=0.061, height=61, width=124)
        self.user_label.configure(activebackground="#f9f9f9")
        self.user_label.configure(activeforeground="black")
        self.user_label.configure(background="#d9d9d9")
        self.user_label.configure(compound='left')
        self.user_label.configure(disabledforeground="#a3a3a3")
        self.user_label.configure(font="-family {David} -size 20")
        self.user_label.configure(foreground="#000000")
        self.user_label.configure(highlightbackground="#d9d9d9")
        self.user_label.configure(highlightcolor="black")
        self.user_label.configure(text='''Users''')

        self.user_button = tk.Button(self.user_filter_frame)
        self.user_button.place(relx=0.138, rely=0.606, height=54, width=107)
        self.user_button.configure(activebackground="#ececec")
        self.user_button.configure(activeforeground="#000000")
        self.user_button.configure(background="#d9d9d9")
        self.user_button.configure(compound='left')
        self.user_button.configure(disabledforeground="#a3a3a3")
        self.user_button.configure(font="-family {David} -size 20")
        self.user_button.configure(foreground="#000000")
        self.user_button.configure(highlightbackground="#d9d9d9")
        self.user_button.configure(highlightcolor="black")
        self.user_button.configure(pady="0")
        self.user_button.configure(text='''Choose''')
        self.user_button.configure(command=lambda: self.open_user_filter())

        self.user_filter_check = tk.Checkbutton(self.user_filter_frame)
        self.user_filter_check.place(relx=0.276, rely=0.424, relheight=0.152, relwidth=0.421)
        self.user_filter_check.configure(activebackground="#ececec")
        self.user_filter_check.configure(activeforeground="#000000")
        self.user_filter_check.configure(anchor='w')
        self.user_filter_check.configure(background="#d9d9d9")
        self.user_filter_check.configure(compound='left')
        self.user_filter_check.configure(disabledforeground="#a3a3a3")
        self.user_filter_check.configure(foreground="#000000")
        self.user_filter_check.configure(highlightbackground="#d9d9d9")
        self.user_filter_check.configure(highlightcolor="black")
        self.user_filter_check.configure(justify='left')
        self.user_filter_check.configure(selectcolor="#d9d9d9")
        self.user_filter_check.configure(text='''Active''')
        self.user_filter_check.configure(variable=self.user_var)

        self.activate_all_filter = tk.Checkbutton(self.filter_frame)
        self.activate_all_filter.place(relx=0.207, rely=0.119, relheight=0.05, relwidth=0.559)
        self.activate_all_filter.configure(activebackground="#ececec")
        self.activate_all_filter.configure(activeforeground="#000000")
        self.activate_all_filter.configure(anchor='w')
        self.activate_all_filter.configure(background="#d9d9d9")
        self.activate_all_filter.configure(compound='left')
        self.activate_all_filter.configure(disabledforeground="#a3a3a3")
        self.activate_all_filter.configure(foreground="#000000")
        self.activate_all_filter.configure(highlightbackground="#d9d9d9")
        self.activate_all_filter.configure(highlightcolor="black")
        self.activate_all_filter.configure(justify='left')
        self.activate_all_filter.configure(selectcolor="#d9d9d9")
        self.activate_all_filter.configure(text='''Active All''')
        self.activate_all_filter.configure(variable=self.all_filter_var)

        self.brush_frame = tk.Frame(self.top)
        self.brush_frame.place(relx=0.0, rely=0.038, relheight=0.838, relwidth=0.096)
        self.brush_frame.configure(relief='groove')
        self.brush_frame.configure(borderwidth="2")
        self.brush_frame.configure(relief="groove")
        self.brush_frame.configure(background="#d9d9d9")
        self.brush_frame.configure(highlightbackground="#d9d9d9")
        self.brush_frame.configure(highlightcolor="black")

        self.straight_button = tk.Button(self.brush_frame)
        self.straight_button.place(relx=0.0, rely=0.0, height=94, width=87)
        self.straight_button.configure(activebackground="#ececec")
        self.straight_button.configure(activeforeground="#000000")
        self.straight_button.configure(background="#d9d9d9")
        self.straight_button.configure(compound='left')
        self.straight_button.configure(disabledforeground="#a3a3a3")
        self.straight_button.configure(foreground="#000000")
        self.straight_button.configure(highlightbackground="#d9d9d9")
        self.straight_button.configure(highlightcolor="black")
        self.straight_button.configure(command=lambda: self.changeBrush("lineS"))
        photo_location = "./straightLine.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.straight_button.configure(image=_img0)
        self.straight_button.configure(pady="0")

        self.curved_button = tk.Button(self.brush_frame)
        self.curved_button.place(relx=0.0, rely=0.202, height=94, width=87)
        self.curved_button.configure(activebackground="#ececec")
        self.curved_button.configure(activeforeground="#000000")
        self.curved_button.configure(background="#d9d9d9")
        self.curved_button.configure(compound='left')
        self.curved_button.configure(disabledforeground="#a3a3a3")
        self.curved_button.configure(foreground="#000000")
        self.curved_button.configure(highlightbackground="#d9d9d9")
        self.curved_button.configure(highlightcolor="black")
        self.curved_button.configure(command=lambda: self.changeBrush("lineC"))
        photo_location = "./curvedLine.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.curved_button.configure(image=_img1)
        self.curved_button.configure(pady="0")

        self.rect_button = tk.Button(self.brush_frame)
        self.rect_button.place(relx=0.0, rely=0.404, height=94, width=87)
        self.rect_button.configure(activebackground="#ececec")
        self.rect_button.configure(activeforeground="#000000")
        self.rect_button.configure(background="#d9d9d9")
        self.rect_button.configure(compound='left')
        self.rect_button.configure(disabledforeground="#a3a3a3")
        self.rect_button.configure(foreground="#000000")
        self.rect_button.configure(highlightbackground="#d9d9d9")
        self.rect_button.configure(highlightcolor="black")
        self.rect_button.configure(command=lambda: self.changeBrush("rect"))
        photo_location = "./rectangle.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.rect_button.configure(image=_img2)
        self.rect_button.configure(pady="0")

        self.poly_button = tk.Button(self.brush_frame)
        self.poly_button.place(relx=0.0, rely=0.607, height=94, width=87)
        self.poly_button.configure(activebackground="#ececec")
        self.poly_button.configure(activeforeground="#000000")
        self.poly_button.configure(background="#d9d9d9")
        self.poly_button.configure(compound='left')
        self.poly_button.configure(disabledforeground="#a3a3a3")
        self.poly_button.configure(foreground="#000000")
        self.poly_button.configure(highlightbackground="#d9d9d9")
        self.poly_button.configure(highlightcolor="black")
        self.poly_button.configure(command=lambda: self.changeBrush("poly"))
        photo_location = "./polyhedron.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.poly_button.configure(image=_img3)
        self.poly_button.configure(pady="0")

        self.circle_button = tk.Button(self.brush_frame)
        self.circle_button.place(relx=0.0, rely=0.809, height=94, width=87)
        self.circle_button.configure(activebackground="#ececec")
        self.circle_button.configure(activeforeground="#000000")
        self.circle_button.configure(background="#d9d9d9")
        self.circle_button.configure(compound='left')
        self.circle_button.configure(disabledforeground="#a3a3a3")
        self.circle_button.configure(foreground="#000000")
        self.circle_button.configure(highlightbackground="#d9d9d9")
        self.circle_button.configure(highlightcolor="black")
        self.circle_button.configure(command=lambda: self.changeBrush("oval"))
        photo_location = "./circle.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.circle_button.configure(image=_img4)
        self.circle_button.configure(pady="0")

        self.param_button = tk.Button(self.top)
        self.param_button.place(relx=0.723, rely=0.791, height=84, width=79)
        self.param_button.configure(activebackground="#ececec")
        self.param_button.configure(activeforeground="#000000")
        self.param_button.configure(background="#d9d9d9")
        self.param_button.configure(compound='left')
        self.param_button.configure(disabledforeground="#a3a3a3")
        self.param_button.configure(foreground="#000000")
        self.param_button.configure(highlightbackground="#d9d9d9")
        self.param_button.configure(highlightcolor="black")
        photo_location = "./painter.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.param_button.configure(image=_img5)
        self.param_button.configure(pady="0")
        self.param_button.configure(command=lambda: self.open_brush_params())
        self.update()
        if self.status == "c":
            self.name = self.net.username
            self.top.after(100, lambda: self.client_update())
        else:
            self.name = self.net.client_name
            self.top.protocol("WM_DELETE_WINDOW", lambda: self.exit_protocol())
            """if self.net.bg_file_destination != '':
                self.set_as_bg(self.net.bg_file_destination)"""
            self.top.after(100, lambda: self.lobby_update())

    def exit_protocol(self):
        self.net.exit_protocol()
        self.top.destroy()

    def change_filters(self, time, colour, user):
        # updates self.blacklist
        for drawing in self.drawings:
            if not str(drawing)[1:-1] in str(self.blacklist):
                if time == 1:
                    drawing_time = drawing[4]
                    if len(self.from_entry.get()) > 0:
                        print("From time: " + str(self.from_entry.get()))
                        if drawing_time < float(self.from_entry.get()):
                            print(str(drawing) + "Added to blacklist")
                            self.blacklist += drawing
                    if len(self.to_entry.get()) > 0:
                        if drawing_time > float(self.to_entry.get()):
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
        self.canvas.delete('all')

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
            self.mouse_coords += [list((self.top.winfo_pointerx() - self.top.winfo_rootx() - self.canvas.winfo_x(),
                                        self.top.winfo_pointery() - self.top.winfo_rooty() - self.canvas.winfo_y()))]
            if len(self.mouse_coords) == 2 and self.brush != "poly" and self.brush != "lineC":
                Drawing = [[self.brush, self.colour, self.fill, self.width,
                            time.time() - self.start, self.name, self.mouse_coords]]
                Drawing_string = json.dumps(Drawing)
                if self.status == "c":  # We're a client
                    self.net.my_socket.send(("D" + Drawing_string).encode())
                else:
                    self.net.update_clients(Drawing_string)
                self.drawings += Drawing
                self.mouse_coords = []
        if mouse_click == 2:
            if self.brush == "poly" or self.brush == "lineC":
                Drawing = [[self.brush, self.colour, self.fill, self.width,
                            time.time() - self.start, self.name, self.mouse_coords]]
                Drawing_string = json.dumps(Drawing)
                if self.status == "c":  # We're a client
                    self.net.my_socket.send(("D" + Drawing_string).encode())
                else:
                    self.net.update_clients(Drawing_string)
                self.drawings += Drawing
                self.mouse_coords = []

    def update(self):
        """
        This function renders all drawings in the self.drawings list that arent already drawn
        """
        print("Blacklist: " + str(self.blacklist))
        print("Drawn Drawings: " + str(self.drawn_drawings))
        if self.all_filter_var.get() == 1:
            self.user_var.set(1)
            self.colour_var.set(1)
            self.time_var.set(1)
            self.all_filter_var.set(0)
        if self.user_var.get() == 1 or self.colour_var.get() == 1 or self.time_var.get() == 1:
            print("Changing Filters")
            self.change_filters(user=self.user_var.get(), colour=self.colour_var.get(), time=self.time_var.get())
        self.drawings = [self.drawings[x] for x in range(len(self.drawings)) if
                         not (self.drawings[x] in self.drawings[:x])]
        print("Drawing...")
        print(self.drawings)
        for drawing in self.drawings:
            if not str(drawing)[1:-1] in str(self.drawn_drawings) and not str(drawing)[1:-1] in str(self.blacklist):
                # New drawing, draw it
                print(str(drawing) + "Drawn")
                b = drawing[0]  # brush
                if b == "oval":
                    self.canvas.create_oval(drawing[-1:][0], fill=drawing[2], outline=drawing[1], width=drawing[3])
                if b == "rect":
                    self.canvas.create_rectangle(drawing[-1:][0], fill=drawing[2], outline=drawing[1], width=drawing[3])
                if b == "lineS":
                    self.canvas.create_line(drawing[-1:][0], fill=drawing[1], width=drawing[3])
                if b == "poly":
                    self.canvas.create_polygon(drawing[-1:][0], fill=drawing[2], width=drawing[3], outline=drawing[1])
                if b == "lineC":
                    self.canvas.create_line(drawing[-1:][0], fill=drawing[1], width=drawing[3], smooth=True)
                self.drawn_drawings += drawing
            else:
                print(f"{drawing} not drawn")
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
                print("New Drawing: " + new_drawing_string)
                new_drawing = json.loads(new_drawing_string)
                self.drawings += new_drawing
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
        self.drawings = self.net.get_data()
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
            self.top.after(100, lambda: self.wait_for_clients_user_list())
        else:
            client_list = ast.literal_eval(self.net.send_names())
            print(client_list)
            to = tk.Toplevel(self.top)
            user_filter = UserFilterGUI.Toplevel1(top=to, all_users=client_list, current_users=self.user_filter_list)
            self.top.after(100, lambda: self.await_user_filter_list(user_filter))

    def wait_for_clients_user_list(self):
        if self.net.changed == 1:
            self.net.changed = 0
            client_list = self.net.client_name_list
            print(client_list)
            to = tk.Toplevel(self.top)
            user_filter = UserFilterGUI.Toplevel1(top=to, all_users=client_list, current_users=self.user_filter_list)
            self.top.after(100, lambda: self.await_user_filter_list(user_filter))
        else:
            self.top.after(100, lambda: self.wait_for_clients_user_list())

    def await_user_filter_list(self, user_gui):
        self.user_filter_list = user_gui.user_list
        self.top.after(100, lambda: self.await_user_filter_list(user_gui))

    def open_brush_params(self):
        to = tk.Toplevel(self.top)
        brush_select = BrushSelectGUI.Toplevel1(top=to, outline_colour=self.colour, fill_colour=self.fill,
                                                width=self.width)
        self.top.after(100, lambda: self.await_brush_change(brush_select))

    def await_brush_change(self, t):
        if t.Changed == 1:
            self.width = t.width
            self.fill = t.fill_c
            self.colour = t.line_c
            t.Changed = 0
        self.top.after(100, lambda: self.await_brush_change(t))


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
