from tkinter import Button, LabelFrame, Frame
from tkinter.constants import *
from tkinter.tix import Tk

from webmarker.frames import Toolbar, MainFrame


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.toolbar = Toolbar(self)
        self.toolbar.pack(side=TOP, fill=X)
        self.main_frame = MainFrame(self)
        self.main_frame.pack(side=BOTTOM, fill=BOTH, expand=True)


def create_application_root():
    root = Tk()
    root.tk.eval('package require Tix')
    root.minsize(500, 300)
    app = Application(root)
    app.pack(fill=BOTH, expand=True)
    return root, app
