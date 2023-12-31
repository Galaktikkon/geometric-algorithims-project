from tkinter import *
from graph import Graph
from interface import Interface


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('tree search')
        self.geometry('750x550')
        self.resizable(False, False)
        self.__createWidgets()

    def __createWidgets(self):
        self.graph = Graph(self)
        self.graph.grid(row=0, column=1)
        self.menu = Interface(self, self.graph.ax)
        self.menu.grid(row=0, column=0)
