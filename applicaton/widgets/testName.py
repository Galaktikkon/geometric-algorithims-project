from tkinter import *
from tkinter import ttk


class testName(LabelFrame):

    def __init__(self, container, controller):
        super().__init__(container, text="testcase name")

        self.nameEntry = Entry(self, textvariable=controller.testCaseName)
        self.nameEntry.pack()
