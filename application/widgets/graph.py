from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from geometry.Point import Point
from geometry.Rectangle import Rectangle
from visualiser.visualiser import Visualiser


class Graph(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.fig, self.ax = plt.subplots(figsize=(10, 8))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.toolbar = NavigationToolbar2Tk(
            self.canvas, self, pack_toolbar=False)

        self.toolbar.update()
        self.toolbar.pack(anchor="center", fill=X)
