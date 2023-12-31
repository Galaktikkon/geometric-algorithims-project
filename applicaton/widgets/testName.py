from tkinter import *
from tkinter import ttk


class testName(LabelFrame):

    def __init__(self, container):
        super().__init__(container, text="testcase name")

        self.caseName = StringVar()
        self.nameEntry = Entry(self, textvariable=self.caseName)
        self.nameEntry.pack()
