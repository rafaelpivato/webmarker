from tkinter import Button, Label, Frame, Scrollbar
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
        self.images = SourceImages(self)
        self.images.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll = Scrollbar(self)
        self.scroll.pack(side=RIGHT, fill=Y)


class SourceImages(Frame):

    def __init__(self, master=None):
        super().__init__(master, pady=5)
        self.create_widgets()

    def create_widgets(self):
        self.spread1 = Spread(self)
        self.sep1 = Separator(self)
        self.spread2 = Spread(self)
        self.sep2 = Separator(self)
        self.spread3 = Spread(self)
        self.spread1.pack(side=TOP, fill=X)
        self.sep1.pack(side=TOP, fill=X)
        self.spread2.pack(side=TOP, fill=X)
        self.sep2.pack(side=TOP, fill=X)
        self.spread3.pack(side=TOP, fill=X)


class Spread(Frame):

    def __init__(self, master=None):
        super().__init__(master, padx=10, pady=5)
        self.create_widgets()

    def create_widgets(self):
        self.preview = ImageFrame(self, text='Original')
        self.cropped = ImageFrame(self, text='Cropped')
        self.marked = ImageFrame(self, text='Marked')
        self.preview.pack(side=LEFT)
        self.cropped.pack(side=LEFT)
        self.marked.pack(side=RIGHT)


class ImageFrame(Frame):

    def __init__(self, master=None, text='Image'):
        super().__init__(master, padx=10, pady=10)
        self.create_widgets(text=text)

    def create_widgets(self, text='Image'):
        self.label = Label(self, text=text, padx=10, pady=10)
        self.button = Button(self, bitmap='gray25', width=300, height=168)
        self.label.pack(side=TOP, fill=X)
        self.button.pack(side=BOTTOM)
