from tkinter import *


class typeFrame(LabelFrame):
    def __init__(self, container):
        super().__init__(container, text="select tree type")
        self.treeType = StringVar()

        self.kdButton = Radiobutton(
            self,
            text="k-dimension",
            variable=self.treeType,
            value="kd"
        )

        self.quadButton = Radiobutton(
            self,
            text="quad",
            variable=self.treeType,
            value="quad"
        )

        self.kdButton.grid(column=0, row=0)

        self.quadButton.grid(column=0, row=1)
