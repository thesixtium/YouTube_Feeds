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
        self.window.geometry("400x400")
        options = self.feed.list_feeds()

        clicked = tk.StringVar()
        clicked.set("default")

        def show():
            label.config(text=clicked.get())

        dropdown = tk.OptionMenu(self.window, clicked, *options)
        dropdown.pack()

        button = tk.Button(self.window, text="click me", command=show).pack()

        greeting = tk.Label(text="YouTube Feeds")
        greeting.pack()

        label = tk.Label(self.window, text=" ")
        label.pack()

        feed_select_frame = tk.Frame(
            master=self.window,
            relief=tk.RAISED,
            borderwidth=1
        )