from tkinter import Button, Frame, Scrollbar
from tkinter.constants import *
from tkinter.ttk import Separator


class Toolbar(Frame):

    def __init__(self, master=None):
        super().__init__(master, padx=5, pady=5, bg='blue')
        self.create_widgets()

    def create_widgets(self):
        self.refresh_btn = Button(self, text='Refresh')
        self.sep1 = Separator(self)
        self.process_btn = Button(self, text='Process All')

        self.refresh_btn.pack(side=LEFT)
        self.sep1.pack(side=LEFT)
        self.process_btn.pack(side=LEFT)


class MainFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.images = ImagesFrame(self)
        self.images.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll = Scrollbar(self)
        self.scroll.pack(side=RIGHT, fill=Y)


class ImagesFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master, bg='yellow')
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, text='Main Images')
        self.button.pack(side=LEFT, fill=BOTH, expand=True)
