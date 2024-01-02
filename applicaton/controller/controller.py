from tkinter import *
from tkinter.messagebox import showerror
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from geometry.Point import Point
from geometry.Rectangle import Rectangle
from visualiser.visualiser import Visualiser
from windows.pointsWindow import pointsWindow
from windows.rectangleWindow import rectangleWindow
from controller.visualisationParameters import visualisationParameters
import random
import os
import jsonpickle
import json
from threading import Thread


class Controller:

    def __init__(self, ax) -> None:

        self.ax = ax
        self.visualiser = Visualiser(ax)

        self.moveBinding = None
        self.clickBinding = None

        self.visualisationParameters = visualisationParameters()

        self.currentPoint = None
        self.points: list[Point] = []
        self.rectangle: Rectangle = None
        self.currentRectangle = None
        self.currentRectangleVerticle = None
        self.currentRectangleVerticleB = None
        self.rectangleVerticle: Point = None

        self.minX = StringVar()
        self.minY = StringVar()
        self.maxX = StringVar()
        self.maxY = StringVar()
        self.randomPointsCount = IntVar()

        self.testMenu = None
        self.treeType = StringVar()
        self.testCaseName = StringVar()
        self.tests: dict = None

        self.directory = self.__initializeData()
        self.__loadData(self.directory)

        self.thread: Thread = None
        self.tree = None

    def startInputPoint(self):
        self.moveBinding = plt.connect(
            'motion_notify_event', self.__onMove)
        self.clickBinding = plt.connect(
            'button_press_event', self.__onClickPoint)

    def startInputRectangle(self):
        self.moveBinding = plt.connect(
            'motion_notify_event', self.__onMoveRectangle)
        self.clickBinding = plt.connect(
            'button_press_event', self.__onClickRectangle)

    def __clearInput(self):
        if self.currentPoint is not None:
            self.currentPoint.remove()
            self.currentPoint = None

        if self.currentRectangleVerticle is not None:
            self.currentRectangleVerticle.remove()
            self.currentRectangleVerticle = None

        if self.currentRectangle is not None:
            self.currentRectangle.remove()
            self.currentRectangle = None

        if self.currentRectangleVerticleB is not None:
            self.currentRectangleVerticleB.remove()
            self.currentRectangleVerticleB = None

    def __onMove(self, event):

        if event.inaxes != self.ax:
            self.__clearInput()
        else:
            self.__clearInput()
            self.currentPoint = self.visualiser.drawPoints(
                Point((event.xdata, event.ydata)))

    def __onClickPoint(self, event):
        if event.inaxes != self.ax:
            return
        if event.button is MouseButton.LEFT:
            newPoint = Point((event.xdata, event.ydata))
            self.points.append(newPoint)
            self.visualiser.drawPoints(newPoint)

    def __onClickRectangle(self, event):
        if event.inaxes != self.ax:
            return
        if event.button is MouseButton.LEFT:
            if self.rectangleVerticle is not None:
                self.rectangle = Rectangle(
                    self.rectangleVerticle, Point((event.xdata, event.ydata)))
                self.visualiser.drawRectangle(self.rectangle, c='red')
                self.visualiser.drawPoints(
                    Point((event.xdata, event.ydata)), color='red')
                self.stopInput()
                self.rectangleVerticle = None

            else:
                self.rectangleVerticle = Point((event.xdata, event.ydata))
                self.visualiser.drawPoints(self.rectangleVerticle, color='red')

    def __onMoveRectangle(self, event):
        if event.inaxes != self.ax:
            self.__clearInput()
        else:
            self.__clearInput()
            if self.rectangleVerticle is not None:
                self.currentRectangle = self.visualiser.drawRectangle(
                    Rectangle(self.rectangleVerticle, Point((event.xdata, event.ydata))), c='red')
                self.currentRectangleVerticleB = self.visualiser.drawPoints(
                    Point((event.xdata, event.ydata)), color='red')
            else:
                self.currentRectangleVerticle = self.visualiser.drawPoints(
                    Point((event.xdata, event.ydata)), color='red')

    def __resetRanges(self):
        self.maxX.set("")
        self.maxY.set("")
        self.minX.set("")
        self.minY.set("")

    def randomPoints(self):
        self.__resetRanges()
        window = pointsWindow(self.maxX, self.minX, self.maxY, self.minY, self)

    def randomRectangle(self):
        self.__resetRanges()
        window = rectangleWindow(self.maxX, self.minX,
                                 self.maxY, self.minY, self)

    def generateRandomPoints(self):

        if self.randomPointsCount is None or self.randomPointsCount.get() <= 0:
            showerror("invalid point count",
                      "point count should be greater than 0")

        points = set()
        i = 0
        while i < self.randomPointsCount.get():
            x = random.uniform(float(self.minX.get()), float(self.maxX.get()))
            y = random.uniform(float(self.minY.get()), float(self.maxY.get()))

            newPoint = Point((x, y))

            if newPoint not in points:
                points.add(newPoint)
                i += 1

        self.points = list(points)
        self.visualiser.clear()
        self.visualiser.drawPoints(self.points)

        if self.rectangle is not None:
            self.currentRectangle = self.visualiser.drawRectangle(
                self.rectangle, c='red', lw=1.5)

    def generateRandomRectangle(self):

        x1 = random.uniform(float(self.minX.get()), float(self.maxX.get()))
        y1 = random.uniform(float(self.minY.get()), float(self.maxY.get()))
        a = Point((x1, y1))
        while True:
            x2 = random.uniform(float(self.minX.get()), float(self.maxX.get()))
            y2 = random.uniform(float(self.minY.get()), float(self.maxY.get()))
            if x2 != x1 and y2 != y1:
                b = Point((x2, y2))
                if self.currentRectangle is not None:
                    self.currentRectangle.remove()
                    self.currentRectangle = None

                self.rectangle = Rectangle(a, b)
                self.currentRectangle = self.visualiser.drawRectangle(
                    self.rectangle, c='red', lw=1.5)
                break

    def stopInput(self):
        self.__clearInput()
        plt.disconnect(self.clickBinding)
        plt.disconnect(self.moveBinding)

    def clear(self):
        self.visualiser.clear()
        self.__clearInput()
        self.points = []
        self.rectangle = None

    def __loadData(self, path):
        testFile = os.path.join(path, 'tests.json')
        if not os.path.isfile(testFile):
            with open(testFile, "w") as f:
                json.dump({}, f, indent=4)
                self.tests = {}
        else:
            with open(testFile, "r") as f:
                fileInput = f.read()
                if fileInput:
                    self.tests = jsonpickle.loads(jsonpickle.decode(fileInput))
                else:
                    self.tests = {}
        f.close()

    def __initializeData(self):
        workingDirectory = os.path.abspath(os.getcwd())
        dataDirectory = os.path.join(workingDirectory, 'data')
        if not os.path.isdir(dataDirectory):
            os.mkdir(dataDirectory)

        return dataDirectory

    def saveData(self, path):
        self.visualisationParameters.setName(self.testCaseName.get())
        self.visualisationParameters.setPoints(self.points)
        self.visualisationParameters.setRectangle(self.rectangle)

        self.tests[self.visualisationParameters.name] = {
            "points": self.visualisationParameters.points,
            "rectangle": self.visualisationParameters.rectangle,
        }

        with open(path, "w") as f:
            json.dump(jsonpickle.encode(self.tests), f, indent=4)
        f.close()

        self.testMenu.set_menu(list(self.tests.keys())[0],
                               *list(self.tests.keys()))

    def loadTest(self, testName):
        if testName not in self.tests:
            showerror("test error", "such test does not exist")
        name = testName
        points = self.tests[name]["points"]
        rectangle = self.tests[name]["rectangle"]

        self.visualisationParameters.setName(name)
        self.visualisationParameters.setPoints(points)
        self.visualisationParameters.setRectangle(rectangle)

        self.points = points
        self.testCaseName = name
        self.rectangle = rectangle

        self.visualiser.clear()
        self.visualiser.drawPoints(points)
        self.visualiser.drawRectangle(rectangle, c='red')

    def __createListFromPoints(self, points):
        output = []
        for point in points:
            output.append((point.x(), point.y()))

        return output

    def createPythonListFromPoints(self):
        with open(os.path.join(self.directory, self.testCaseName), "w") as f:
            output = self.__createListFromPoints(self.points)
            f.write(self.testCaseName+" = "+str(output))
        f.close()

    def reset(self, thread: Thread):
        if not thread:
            return
        thread.join()

    def showBuild(self):
        pass
