from tkinter import *
from tkinter import ttk
# import do wizualzatora


class pointOptions(LabelFrame):
    def __init__(self, container):
        super().__init__(container, text="points options")
        self.__addContent()

    def __addContent(self):
        # połączenie do wizualizatora
        self.enterButton = ttk.Button(self, text='ENTER')
        self.enterButton.grid(row=0, column=0, columnspan=2)
        # połączenie do wizualizatora
        self.stopButton = ttk.Button(self, text='STOP')
        self.stopButton.grid(row=1, column=0, columnspan=2)
        # połączenie do wizualizatora
        self.generateRandom = ttk.Button(self, text="random")
        self.generateRandom.grid(row=0, column=2, columnspan=2)

        # dodać opis jak bedzie miejsce?
        self.pointCount = IntVar()
        self.SpinBox = ttk.Spinbox(
            self, from_=1, to=10 ** 6, textvariable=self.pointCount, wrap=True, width=4)
        self.SpinBox.grid(row=1, column=2, columnspan=2)

        Label(self, text="min_x").grid(row=2, column=0)
        Label(self, text="min_y").grid(row=3, column=0)
        Label(self, text="max_x").grid(row=2, column=2)
        Label(self, text="max_y").grid(row=3, column=2)

        self.minX = IntVar()
        self.minY = IntVar()
        self.maxX = IntVar()
        self.maxY = IntVar()

        Entry(master=self, textvariable=self.minX,
              width=5).grid(row=2, column=1)
        Entry(master=self, textvariable=self.minY,
              width=5).grid(row=3, column=1)
        Entry(master=self, textvariable=self.maxX,
              width=5).grid(row=2, column=3)
        Entry(master=self, textvariable=self.maxY,
              width=5).grid(row=3, column=3)
