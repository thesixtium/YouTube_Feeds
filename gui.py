# https://realpython.com/python-gui-tkinter/
import tkinter as tk
from feeds import Feeds

class Gui:
    window = None
    feed = None

    def __init__(self):
        self.feed = Feeds()
        self.window = tk.Tk()
        self.setup()
        self.window.mainloop()

    def setup(self):
        greeting = tk.Label(text="Hello, Tkinter")
        greeting.pack()
