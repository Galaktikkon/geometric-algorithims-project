from tkinter import *
from tkinter import ttk
from controller.visualisationParameters import visualisationParameters
from geometry.Rectangle import Rectangle
from geometry.Point import Point
from math import inf


class visualisationInfo(Frame):

    def __init__(self, container, visualisationParameters: visualisationParameters):
        super().__init__(container)

        name = visualisationParameters.name
        points = visualisationParameters.points
        treeType = visualisationParameters.treeType
        rectangle = visualisationParameters.rectangle

        Label(self, text="testcase info: ").grid(row=0, column=0)

        Label(self, text="testcase name: "+name).grid(row=1, column=0)

        Label(self, text="tree type: "+treeType).grid(row=2, column=0)

        Label(self, text="number of points: " +
              str(len(points))).grid(row=3, column=0)

        Label(self, text="points range: " +
              self.__getPointsRange(points)).grid(row=4, column=0)

        Label(self, text="rectangle range: " +
              self.__getRectangle(rectangle)).grid(row=5, column=0)

    def __getPointsRange(self, points: list[Point]):
        xMin, yMin = inf, inf
        xMax, yMax = -inf, -inf
        for point in points:
            xMin = min(point.x(), xMin)
            xMax = max(point.x(), xMax)
            yMin = min(point.y(), yMin)
            yMax = max(point.x(), yMax)

        return f'\n x:[{xMin},{xMax}], \n y:[{yMin},{yMax}]'

    def __getRectangle(self, rectangle: Rectangle):

        sw = rectangle.lowerLeft
        se = Point((rectangle.lowerLeft.x(), rectangle.upperRight.y()))
        ne = rectangle.upperRight
        nw = Point((rectangle.lowerLeft.y(), rectangle.upperRight.x()))

        return f'\n sw: {sw}, \n se: {se}, \n ne: {ne}, \n nw: {nw}'
