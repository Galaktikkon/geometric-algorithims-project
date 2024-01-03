from tkinter import *
from tkinter import ttk
from controller.controller import Controller


class rectangleOptions(LabelFrame):

    def __init__(self, container, controller: Controller):
        super().__init__(container, text="rectangle options")

        self.enterButton = ttk.Button(
            self, text='ENTER', command=controller.startInputRectangle)
        self.enterButton.grid(row=0, column=0, columnspan=2)

        self.stopButton = ttk.Button(
            self, text='STOP', command=controller.stopInput)
        self.stopButton.grid(row=1, column=0, columnspan=2)

        self.generateRandom = ttk.Button(
            self, text="random", command=controller.randomRectangle)
        self.generateRandom.grid(row=0, column=2, columnspan=2, rowspan=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
