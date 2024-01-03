from tkinter import *
from widgets.graph import Graph
from widgets.interface import Interface
from controller.controller import Controller


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('tree search')
        self.geometry('1150x850')
        self.resizable(False, False)
        graph: Graph = Graph(self)
        graph.grid(row=0, column=1)
        self.controller = Controller(graph.ax)
        Interface(self, self.controller, graph).grid(row=0, column=0)
