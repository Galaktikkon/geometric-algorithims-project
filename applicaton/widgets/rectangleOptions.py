from tkinter import *
from tkinter import ttk
from controller.controller import Controller


class rectangleOptions(LabelFrame):

    def __init__(self, container, ax):
        super().__init__(container, text="rectangle options")

        self.controller = Controller(ax)

        self.enterButton = ttk.Button(
            self, text='ENTER', command=self.controller.startInputRectangle)
        self.enterButton.grid(row=0, column=0, columnspan=2)

        self.stopButton = ttk.Button(
            self, text='STOP', command=self.controller.stopInput)
        self.stopButton.grid(row=1, column=0, columnspan=2)

        # połączenie do wizualizatora
        self.pointA = StringVar()
        self.pointB = StringVar()

        self.labelA = LabelFrame(self, text="A")
        self.labelA.grid(row=1, column=2)

        self.labelB = LabelFrame(self, text="B")
        self.labelB.grid(row=1, column=3)

        Entry(self.labelA, textvariable=self.pointA, width=3).pack()
        Entry(self.labelB, textvariable=self.pointB, width=3).pack()

        self.generateRandom = ttk.Button(self, text="random")
        self.generateRandom.grid(row=0, column=2, columnspan=2)
