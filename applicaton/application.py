from tkinter import *
from widgets.graph import Graph
from widgets.interface import Interface
from controller.controller import Controller


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
        self.controller = Controller(self.graph.ax)
        self.menu = Interface(self, self.controller, self.graph)
        self.menu.grid(row=0, column=0)
