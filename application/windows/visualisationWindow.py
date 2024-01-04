from tkinter import *
from tkinter import ttk
from controller.controller import Controller
from controller.visualisationParameters import visualisationParameters
from widgets.graph import Graph
from widgets.exitButton import exitButton
import matplotlib.pyplot as plt
from geometry.Point import Point
from kdTree.kdTree import kdTree
from quadTree.quadTree import quadTree
from widgets.visualisationInfo import visualisationInfo
from threading import Thread


class visualisationWindow(Toplevel):
    def __init__(self, visualisationParameters: visualisationParameters):
        super().__init__()
        self.geometry("1250x850")
        self.resizable(False, False)
        self.graph = Graph(self)
        self.graph.grid(row=0, column=3)
        self.controller = Controller(self.graph.ax)
        self.controller.visualisationParameters = visualisationParameters

        self.menuFrame = visualisationInfo(self, visualisationParameters)
        self.menuFrame.grid(row=0, column=0, rowspan=7, columnspan=2)

        self.searchButton = ttk.Button(
            self.menuFrame, text="SEARCH", command=self.controller.showSearch)
        self.searchButton.grid(row=8, column=0, pady=5)

        self.buildButton = ttk.Button(
            self.menuFrame, text="BUILD", command=self.controller.showBuild)
        self.buildButton.grid(row=9, column=0)

        self.stopButton = ttk.Button(
            self.menuFrame, text="CLEAR", command=self.controller.reset)
        self.stopButton.grid(row=10, column=0)

        self.exitButton = exitButton(self.menuFrame, self.graph, self).grid(
            row=11, column=0, pady=5)
