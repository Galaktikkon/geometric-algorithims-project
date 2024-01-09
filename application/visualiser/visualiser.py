import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from geometry.Point import Point
from geometry.Rectangle import Rectangle
from math import inf


class Visualiser():
    def __init__(self, ax):
        self.ax = ax
        self.currentXLimits = [0, 10]
        self.currentYLimits = [0, 10]
        self.interval = DoubleVar(value=0.5)
        self.ax.set_xlim([self.currentXLimits[0], self.currentXLimits[1]])
        self.ax.set_ylim([self.currentYLimits[0], self.currentYLimits[1]])
        self.ins = None

    def setLimits(self, points):

        pointsList = [points] if isinstance(points, Point) else points

        for point in pointsList:
            self.currentXLimits[0] = min(point.x(), self.currentXLimits[0])
            self.currentXLimits[1] = max(point.x(), self.currentXLimits[1])
            self.currentYLimits[0] = min(point.y(), self.currentYLimits[0])
            self.currentYLimits[1] = max(point.y(), self.currentYLimits[1])

        xborder = int(abs(self.currentXLimits[0]-self.currentXLimits[1])*0.1)
        yborder = int(abs(self.currentXLimits[0]-self.currentXLimits[1])*0.1)

        self.ax.set_xlim(
            [self.currentXLimits[0]-xborder, self.currentXLimits[1]+yborder])
        self.ax.set_ylim(
            [self.currentYLimits[0]-xborder, self.currentYLimits[1]+yborder])

    def drawPoints(self, points, color="darkBlue", markersize=7, **kwargs):
        if isinstance(points, Point):
            self.setLimits(points)
            point = self.ax.plot(points.x(), points.y(),
                                 color=color, marker=".", markersize=markersize)[0]
            plt.draw()
            return point
        else:
            self.setLimits(points)
            for point in points:
                self.ax.plot(point.x(), point.y(),
                             color=color, marker=".", markersize=markersize)

            plt.draw()

    def drawPointsList(self, points: list[Point], color='darkBlue', markersize=7, **kwargs):
        res = []
        self.setLimits(points)
        for point in points:
            res.append(self.drawPoints(point, color, markersize))
        return res

    def removePointsList(self, points):
        for point in points:
            point.remove()

    def drawRectangle(self, rectangle: Rectangle, c='k', lw=1, **kwargs):
        x1, y1 = rectangle.lowerLeft.x(), rectangle.lowerLeft.y()
        x2, y2 = rectangle.upperRight.x(), rectangle.upperRight.y()
        self.setLimits([rectangle.lowerLeft, rectangle.upperRight])
        rect = self.ax.plot([x1, x2, x2, x1, x1],
                            [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)[0]
        plt.draw()
        return rect

    def drawLineInRect2D(self, rectangle, line, dim, lw=3.0, c='k', **kwargs):
        if dim == 0:
            y1, y2 = rectangle.lowerLeft.y(), rectangle.upperRight.y()
            self.ax.plot([line, line], [y1, y2], c, linewidth=lw)
        if dim == 1:
            x1, x2 = rectangle.lowerLeft.x(), rectangle.upperRight.x()
            self.ax.plot([x1, x2], [line, line], c, linewidth=lw)

    def clear(self):
        self.ax.cla()
        self.currentXLimits = [0, 10]
        self.currentYLimits = [0, 10]
        self.ax.set_xlim([self.currentXLimits[0], self.currentXLimits[1]])
        self.ax.set_ylim([self.currentYLimits[0], self.currentYLimits[1]])
        plt.draw()
