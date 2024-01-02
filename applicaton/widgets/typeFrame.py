from tkinter import *
from controller.controller import Controller


class typeFrame(LabelFrame):
    def __init__(self, container, controller: Controller):
        super().__init__(container, text="select tree type")

        self.kdButton = Radiobutton(
            self,
            text="k-dimension",
            variable=controller.treeType,
            value="kd",
            command=lambda: controller.visualisationParameters.setTreeType(
                controller.treeType.get())
        )

        self.quadButton = Radiobutton(
            self,
            text=" quad",
            variable=controller.treeType,
            value="quad",
            command=lambda: controller.visualisationParameters.setTreeType(
                controller.treeType.get())
        )

        self.kdButton.grid(column=0, row=0)

        self.quadButton.grid(column=0, row=1)
