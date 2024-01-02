from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from widgets.graph import Graph


class exitButton(ttk.Button):
    def __init__(self, container, graph, window):
        super().__init__(master=container, text="EXIT", command=lambda window=window,
                         graph=graph: self.closeWindow(window, graph))

    def closeWindow(self, window, graph: Graph):
        plt.close(graph.fig)
        window.destroy()
