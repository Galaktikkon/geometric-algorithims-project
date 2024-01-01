from tkinter import *
from tkinter import ttk

# dodać połączenia z I/O


class testFrame(LabelFrame):
    def __init__(self, container, tests, controller):
        super().__init__(container, text="select test case")
        self.tests: dict = tests
        self.selectedTest: str = StringVar()

        testMenu = ttk.OptionMenu(
            self,
            self.selectedTest,
            self.tests.keys()[0] if self.tests.keys() else "",
            list(self.tests.keys()) if len(self.tests.keys()) else ""
        )
        testMenu.pack()
