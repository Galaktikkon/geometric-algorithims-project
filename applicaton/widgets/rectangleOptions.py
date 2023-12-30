from tkinter import *
from tkinter import ttk
# import do wizualizatora


class rectangleOptions(LabelFrame):

    def __init__(self, container):
        super().__init__(container, text="rectangle options")
        self.__addContent()

    def __addContent(self):
        # to sie chyba da skrocic do onelinerow ale trzeba
        # sprawdzic czy pozniej to nie bedzie robilo klopotow

        # połączenie do wizualizatora
        self.enterButton = ttk.Button(self, text='ENTER')
        self.enterButton.grid(row=0, column=0, columnspan=2)
        # połączenie do wizualizatora
        self.stopButton = ttk.Button(self, text='STOP')
        self.stopButton.grid(row=1, column=0, columnspan=2)
        # połączenie do wizualizatora
        self.generateRandom = ttk.Button(self, text="random")
        self.generateRandom.grid(row=0, column=2, columnspan=2)

        self.pointA = StringVar()
        self.pointB = StringVar()

        self.labelA = LabelFrame(self, text="A")
        self.labelA.grid(row=1, column=2)

        self.labelB = LabelFrame(self, text="B")
        self.labelB.grid(row=1, column=3)

        Entry(self.labelA, textvariable=self.pointA, width=3).pack()
        Entry(self.labelB, textvariable=self.pointB, width=3).pack()
