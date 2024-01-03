from tkinter import *
from tkinter import ttk
from widgets.pointOptions import pointOptions
from widgets.rectangleOptions import rectangleOptions
from widgets.testName import testName
from controller.controller import Controller
import os


class testOptions(LabelFrame):
    def __init__(self, container, controller: Controller):
        super().__init__(container, text="custom testcase")

        self.pointOptions: LabelFrame = pointOptions(self, controller)
        self.pointOptions.grid(row=1, column=0, columnspan=2)

        self.rectangleOptions: LabelFrame = rectangleOptions(self, controller)
        self.rectangleOptions.grid(row=2, column=0, columnspan=2)

        self.nameOptions: LabelFrame = testName(self, controller)
        self.nameOptions.grid(row=3, column=0, columnspan=2)

        self.clearButton: Button = ttk.Button(
            self, text="CLEAR", command=controller.clear)
        self.clearButton.grid(row=4, column=0)

        self.saveButton: Button = ttk.Button(
            self, text="SAVE", command=lambda: controller.saveData(os.path.join(controller.directory, 'tests.json')))
        self.saveButton.grid(row=4, column=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
