from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror


class RandomWindow(Toplevel):

    def __init__(self, maxX, minX, maxY, minY, controller, exitFunc):
        super().__init__()
        self.geometry("200x100")

        self.controller = controller
        self.exitFunc = exitFunc

        self.frame = LabelFrame(self, text='specify x and y', padx=10, pady=10)

        Label(self.frame, text="min_x").grid(row=0, column=0)
        Label(self.frame, text="min_y").grid(row=1, column=0)
        Label(self.frame, text="max_x").grid(row=0, column=2)
        Label(self.frame, text="max_y").grid(row=1, column=2)

        self.minXEntry = Entry(master=self.frame, textvariable=minX,
                               width=5)
        self.minXEntry.insert(0, "-1000")
        self.minXEntry.grid(row=0, column=1)

        self.minYEntry = Entry(master=self.frame, textvariable=minY,
                               width=5)
        self.minYEntry.insert(0, "-1000")
        self.minYEntry.grid(row=1, column=1)

        self.maxXEntry = Entry(master=self.frame, textvariable=maxX,
                               width=5)
        self.maxXEntry.insert(0, "1000")
        self.maxXEntry.grid(row=0, column=3)

        self.maxYEntry = Entry(master=self.frame, textvariable=maxY,
                               width=5)
        self.maxYEntry.insert(0, "1000")
        self.maxYEntry.grid(row=1, column=3)

        ttk.Button(
            self.frame, text='save & exit', command=lambda window=self, minX=minX, maxX=maxX, minY=minY, maxY=maxY: self.exit(window, minX, maxX, minY, maxY)).grid(row=2, column=0, columnspan=4)

        self.frame.pack()

    def exit(self, window, minX, maxX, minY, maxY):
        if float(minX.get()) >= float(maxX.get()):
            showerror("invalid input",
                      "max_x value should be greater than min_x value")
            return
        elif float(minY.get()) >= float(maxY.get()):
            showerror("invalid input",
                      "max_y value should be greater than min_y value")
            return
        else:
            self.exitFunc()
            window.destroy()
