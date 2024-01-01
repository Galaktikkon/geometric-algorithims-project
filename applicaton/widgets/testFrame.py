from tkinter import *
from tkinter import ttk
from controller.controller import Controller


class testFrame(LabelFrame):
    def __init__(self, container, controller: Controller):
        super().__init__(container, text="select test case")

        selectedTest = StringVar()

        names = list(controller.tests.keys()) if len(
            controller.tests.keys()) else "",

        testMenu = ttk.OptionMenu(
            self,
            selectedTest,
            list(controller.tests.keys())[
                0] if controller.tests.keys() else "",
            *names[0],
            command=controller.loadTest
        )

        controller.testMenu = testMenu

        testMenu.pack()
