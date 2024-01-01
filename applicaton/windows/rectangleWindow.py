from tkinter import *
from windows.abstractRandomWIndow import abstractRandomWindow
from tkinter.messagebox import showerror


class rectangleWindow(abstractRandomWindow):

    def __init__(self, maxX, minX, maxY, minY, controller):
        super().__init__(maxX, minX, maxY, minY, controller)

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
            self.controller.generateRandomRectangle()
            window.destroy()
