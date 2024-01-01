from tkinter import *
from tkinter import ttk
from controller.controller import Controller


class rectangleOptions(LabelFrame):

    def __init__(self, container, controller: Controller):
        super().__init__(container, text="rectangle options")

        self.controller = controller

        self.enterButton = ttk.Button(
            self, text='ENTER', command=self.controller.startInputRectangle)
        self.enterButton.grid(row=0, column=0, columnspan=2)

        self.stopButton = ttk.Button(
            self, text='STOP', command=self.controller.stopInput)
        self.stopButton.grid(row=1, column=0, columnspan=2)

        self.generateRandom = ttk.Button(
            self, text="random", command=lambda: self.controller.randomRectangle())
        self.generateRandom.grid(row=0, column=2, columnspan=2, rowspan=2)
