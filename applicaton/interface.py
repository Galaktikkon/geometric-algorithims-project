from tkinter import *
from tkinter import ttk
from visualisationParameters import visualisationParameters
from widgets.typeFrame import typeFrame
from widgets.testFrame import testFrame
from widgets.testOptions import testOptions
from graph import Graph
import matplotlib.pyplot as plt


class Interface(Frame):

    def __init__(self, container):
        super().__init__(container)
        self.parameters = visualisationParameters()
        self.__addContent()

    def __addContent(self):
        Label(self, text="Geometric Search").grid(row=0, column=0)
        # Tree type frame
        self.typeframe: LabelFrame = typeFrame(self)
        self.typeframe.grid(row=1, column=0)

        # Test case frame
        self.testFrame: LabelFrame = testFrame(self, {})
        self.testFrame.grid(row=2, column=0)

        # Option Menu
        self.testOptions: LabelFrame = testOptions(self)
        self.testOptions.grid(row=3, column=0)

        # Start visalisation
        self.startButton: ttk.Button = ttk.Button(
            self, text="START", command=self.startVisualisation)
        self.startButton.grid(row=4, column=0)

    # dodać sprawdzanie poprawności jak bedzie czas i zamykanie rzeczy
    def startVisualisation(self):
        top = Toplevel()
        graph = Graph(top)
        graph.grid(row=0, column=0)
        ttk.Button(master=top, text="CLOSE",
                   command=lambda top=top, graph=graph: self.closeWindow(top, graph)).grid(row=1, column=0)

        # dodać guzik do gifa i cacy

    def closeWindow(self, window, graph: Graph):
        plt.close(graph.fig)
        window.destroy()
