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
        self.ax.set_xlim([self.currentXLimits[0], self.currentXLimits[1]])
        self.ax.set_ylim([self.currentYLimits[0], self.currentYLimits[1]])

    def setLimits(self, points_raw):

        points = [points_raw] if isinstance(points_raw, Point) else points_raw

        for point in points:
            self.currentXLimits[0] = min(point.x(), self.currentXLimits[0])
            self.currentXLimits[1] = max(point.x(), self.currentXLimits[1])
            self.currentYLimits[0] = min(point.y(), self.currentYLimits[0])
            self.currentYLimits[1] = max(point.y(), self.currentYLimits[1])
        self.ax.set_xlim(
            [self.currentXLimits[0]-1, self.currentXLimits[1]+1])
        self.ax.set_ylim(
            [self.currentYLimits[0]-1, self.currentYLimits[1]+1])

    def drawPoints(self, points, color="darkBlue"):

        if isinstance(points, Point):
            self.setLimits(points)
            point = self.ax.plot(points.x(), points.y(),
                                 color=color, marker=".")[0]
            plt.draw()
            return point
        else:
            self.setLimits(points)
            for point in points:
                self.ax.plot(point.x(), point.y(),
                             color=color, marker=".")

            plt.draw()

    def drawRectangle(self, rectangle: Rectangle, c='k', lw=1, **kwargs):
        x1, y1 = rectangle.lowerLeft.x(), rectangle.lowerLeft.y()
        x2, y2 = rectangle.upperRight.x(), rectangle.upperRight.y()
        self.setLimits([rectangle.lowerLeft, rectangle.upperRight])
        rect = self.ax.plot([x1, x2, x2, x1, x1],
                            [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)[0]
        plt.draw()
        return rect

    def clear(self):
        self.ax.cla()
        self.ax.set_xlim([0, 10])
        self.ax.set_ylim([0, 10])
        plt.draw()
