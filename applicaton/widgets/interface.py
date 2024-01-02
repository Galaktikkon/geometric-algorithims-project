from tkinter import *
from tkinter import ttk
from controller.visualisationParameters import visualisationParameters
from widgets.typeFrame import typeFrame
from widgets.testFrame import testFrame
from widgets.testOptions import testOptions
from widgets.graph import Graph
from widgets.exitButton import exitButton
from windows.visualisationWindow import visualisationWindow
import matplotlib.pyplot as plt


class Interface(Frame):

    def __init__(self, container, controller, graph):
        super().__init__(container)
        self.parameters = visualisationParameters()
        self.controller = controller
        self.container = container
        self.graph = graph
        self.__addContent()

    def __addContent(self):
        Label(self, text="Geometric Search").grid(row=0, column=0)
        # Tree type frame
        self.typeframe: LabelFrame = typeFrame(self, self.controller)
        self.typeframe.grid(row=1, column=0)

        # Test case frame
        self.testFrame: LabelFrame = testFrame(self, self.controller)
        self.testFrame.grid(row=2, column=0)

        # Option Menu
        self.testOptions: LabelFrame = testOptions(self, self.controller)
        self.testOptions.grid(row=3, column=0)

        # Start visalisation
        self.startButton: ttk.Button = ttk.Button(
            self, text="START", command=self.startVisualisation)
        self.startButton.grid(row=4, column=0)

        # Exit App
        self.exitButton: ttk.Button = exitButton(
            self, self.graph, self.container)
        self.exitButton.grid(row=5, pady=10)

    def startVisualisation(self):
        visualisationWindow(self.controller.visualisationParameters)
