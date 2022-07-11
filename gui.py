# https://realpython.com/python-gui-tkinter/
import tkinter as tk
from feeds import Feeds

class Gui:
    window = None
    feed = None

    def __init__(self):
        self.window = tk.Tk()
        self.feed = Feeds()