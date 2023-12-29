from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from visualisationParameters import visualisationParameters
import os
import json

workingDirectory = os.path.abspath(os.getcwd())
dataDirectory = os.path.join(workingDirectory, 'data')
if not os.path.isdir(dataDirectory):
    os.mkdir(dataDirectory)


jsonFile = os.path.join(dataDirectory, 'tests.json')
if not os.path.isfile(jsonFile):
    with open(jsonFile, "w") as f:
        json.dump({}, f, indent=4)
        tests = {}
    f.close()
else:
    with open(jsonFile, "r") as f:
        tests: dict = json.load(f)

root = Tk()

root.geometry('750x550')
root.title('tree search')

parameters = visualisationParameters()

treeTypeVar = StringVar()

mainLabel = Label(root, text="GEOMETRIC SEARCH")
typeFrame = LabelFrame(root, text="tree type")
testFrame = LabelFrame(root, text="select test")

typeFrame.grid(row=1, column=0)
mainLabel.grid(row=0, column=0)

kdButton = Radiobutton(
    typeFrame,
    text="k-dimension",
    variable=treeTypeVar,
    value="kd"
)
quadButton = Radiobutton(
    typeFrame,
    text="quad",
    variable=treeTypeVar,
    value="quad"
)


kdButton.grid(column=0, row=0)
quadButton.grid(column=0, row=1)

testFrame.grid(row=2, column=0)

testName = StringVar()

testMenu = ttk.OptionMenu(
    testFrame,
    testName,
    tests.keys()[0] if tests.keys() else "",
    list(tests.keys()) if len(tests.keys()) else ""
)

testMenu.pack()

graphOptionsFrame = LabelFrame(root, text='specify test case')

graphPointsFrame = LabelFrame(graphOptionsFrame, text='points')

enterPointsButton = ttk.Button(graphPointsFrame, text='ENTER')
enterPointsButton.grid(row=0, column=0)

stopPointsButton = ttk.Button(graphPointsFrame, text='STOP')
stopPointsButton.grid(row=1, column=0)

randomPoints = BooleanVar(value=True)

randomPointsCheckButton = ttk.Checkbutton(
    graphPointsFrame, text="random?", variable=randomPoints)
randomPointsCheckButton.grid(row=0, column=1)

randomPointsCount = IntVar()
randomPointsCountSpinBox = ttk.Spinbox(
    graphPointsFrame, from_=1, to=10 ** 6, textvariable=randomPointsCount, wrap=True, width=4)

randomPointsCountSpinBox.grid(row=1, column=1)

# minX= StringVar()
# randomMinX = Entry(graphPointsFrame, textvariable=)


graphRectangleFrame = ttk.Labelframe(
    graphOptionsFrame, text='rectangle')

enterRectangleButton = ttk.Button(graphRectangleFrame, text='ENTER')
enterRectangleButton.grid(row=0, column=0)

stopRectangleButton = ttk.Button(graphRectangleFrame, text='STOP')
stopRectangleButton.grid(row=1, column=0)

randomRectangle = BooleanVar(value=True)
randomRectangleCheckButton = ttk.Checkbutton(
    graphRectangleFrame, text="random?", variable=randomRectangle)
randomRectangleCheckButton.grid(row=0, column=1, rowspan=2)

graphPointsFrame.grid(row=0, column=0)
graphRectangleFrame.grid(row=1, column=0)

clearGraphButton = ttk.Button(graphOptionsFrame, text='CLEAR')
clearGraphButton.grid(row=2, column=0, pady=2, sticky=W)

saveGraphButton = ttk.Button(graphOptionsFrame, text='SAVE')
saveGraphButton.grid(row=2, column=0, pady=2, sticky=E)

graphOptionsFrame.grid(row=3, column=0)
startButton = ttk.Button(root, text='START')
startButton.grid(row=4, column=0)

graphFrame = Frame(root)
fig, ax = plt.subplots(figsize=(6, 5))
canvas = FigureCanvasTkAgg(fig, master=graphFrame)
canvas.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas, graphFrame, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="center", fill=X)
graphFrame.grid(row=0, column=4, rowspan=20, columnspan=4)


root.mainloop()
