# This Class Holds basic functions to flip between GUI's
import tkinter
from typing import List


class GUI:
    def __init__(self):
        self.widgets: List[tkinter.Widget] = []

    def cleanGUI(self):
        for widget in self.widgets:
            widget.destroy()

    def replaceGUI(self, anotherGUI, top, params=None):
        self.cleanGUI()
        __import__(anotherGUI.__name__)
        if params is not None:
            anotherGUI.Toplevel1(top, params)
        else:
            anotherGUI.Toplevel1(top)
