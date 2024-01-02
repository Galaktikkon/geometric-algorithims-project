from tkinter import *
from tkinter import ttk
from controller.controller import Controller
from controller.visualisationParameters import visualisationParameters
from widgets.graph import Graph
from widgets.exitButton import exitButton
import matplotlib.pyplot as plt


class visualisationWindow(Toplevel):
    def __init__(self, visualisationParameters: visualisationParameters):
        super().__init__()
        self.geometry("600x600")
        self.graph = Graph(self)
        self.graph.grid(row=0, column=0)
        self.controller = Controller(self.graph.ax)
        self.controller.visualisationParameters = visualisationParameters

        self.menuFrame = Frame(self)
        self.menuFrame.grid(row=1, column=0)

        self.gifButton = ttk.Button(self.menuFrame, text="GIF")
        self.gifButton.grid(row=0, column=1, sticky=W)

        self.exitButton = exitButton(self.menuFrame, self.graph, self).grid(
            row=0, column=0, sticky=E)
