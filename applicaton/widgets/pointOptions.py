from tkinter import *
from tkinter import ttk
from controller.controller import Controller
# import do wizualzatora


class pointOptions(LabelFrame):

    def __init__(self, container, controller):

        super().__init__(container, text="points options")

        self.controller = controller

        self.enterButton = ttk.Button(
            self, text='ENTER', command=self.controller.startInputPoint)
        self.enterButton.grid(row=0, column=0, columnspan=2)

        self.stopButton = ttk.Button(
            self, text='STOP', command=self.controller.stopInput)
        self.stopButton.grid(row=1, column=0, columnspan=2)

        self.controller.randomPointsCount.set(25)

        self.SpinBox = ttk.Spinbox(
            self, from_=1, to=10 ** 6, textvariable=self.controller.randomPointsCount, wrap=True, width=4)
        self.SpinBox.grid(row=1, column=2, columnspan=2)

        self.generateRandom = ttk.Button(
            self, text="random", command=lambda: self.controller.randomPoints())
        self.generateRandom.grid(row=0, column=2, columnspan=2)
