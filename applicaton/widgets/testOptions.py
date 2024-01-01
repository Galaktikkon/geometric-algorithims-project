from tkinter import *
from tkinter import ttk
from widgets.pointOptions import pointOptions
from widgets.rectangleOptions import rectangleOptions
from widgets.testName import testName
from controller.controller import Controller


class testOptions(LabelFrame):
    def __init__(self, container, controller):
        super().__init__(container, text="custom testcase")

        self.pointOptions: LabelFrame = pointOptions(self, controller)
        self.pointOptions.grid(row=1, column=0, columnspan=2)

        self.rectangleOptions: LabelFrame = rectangleOptions(self, controller)
        self.rectangleOptions.grid(row=2, column=0, columnspan=2)

        self.nameOptions: LabelFrame = testName(self)
        self.nameOptions.grid(row=3, column=0, columnspan=2)

        self.clearButton: Button = ttk.Button(
            self, text="CLEAR", command=controller.clear)
        self.clearButton.grid(row=4, column=0)

        self.saveButton: Button = ttk.Button(self, text="SAVE")
        self.saveButton.grid(row=4, column=1)
