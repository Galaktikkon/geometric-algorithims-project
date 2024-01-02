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


class visualisationWindow(Toplevel):
    def __init__(self, visualisationParameters: visualisationParameters):
        super().__init__()
        self.geometry("850x550")
        self.graph = Graph(self)
        self.graph.grid(row=0, column=3)
        self.controller = Controller(self.graph.ax)
        self.controller.visualisationParameters = visualisationParameters

        self.menuFrame = visualisationInfo(self, visualisationParameters)
        self.menuFrame.grid(row=0, column=0, rowspan=7, columnspan=2)

        self.gifButton = ttk.Button(self.menuFrame, text="GIF")
        self.gifButton.grid(row=8, column=0, pady=5)

        self.exitButton = exitButton(self.menuFrame, self.graph, self).grid(
            row=9, column=0, pady=5)

        self.tree = self.__createTree(
            self.controller.visualisationParameters.treeType,
            self.controller.visualisationParameters.points
        )

        self.controller.visualiser.drawVisualisation(
            self.tree, self.controller.visualisationParameters.points, self.controller.visualisationParameters.rectangle)

    def __createTree(self, treetype: str, points: list[Point]):
        if treetype == 'quad':
            tree = quadTree(points, 1)
        elif treetype == 'kd':
            tree = kdTree(points)

        return tree
