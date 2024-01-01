from geometry.Point import Point
from geometry.Rectangle import Rectangle
from tkinter.messagebox import showerror


class visualisationParameters:

    def __init__(self):
        self.name: str = None
        self.treeType: str = None
        self.rectangle: Rectangle = None
        self.points: list[Point] = None

    def setName(self, name: str) -> None:
        self.name = name

    def setRectangle(self, rectangle: Rectangle) -> None:
        if not rectangle:
            showerror("rectangle error",
                      "rectangle cannot be ommited as a simulation parameter")
        else:
            self.rectangle = rectangle

    def setTreeType(self, treeType: str) -> None:
        if not treeType:
            showerror("tree type error",
                      "tree type cannot be ommited as a simulation parameter")
        else:
            self.treeType = treeType

    def setPoints(self, points: list[Point]) -> None:
        if not points:
            showerror("points error",
                      "set of points cannot be ommited as a simulation parameter")
        else:
            self.points = points
