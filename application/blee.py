import numpy as np
from kdTree.kdTree import kdTree
from quadTree.quadTree import quadTree
from time import perf_counter
from geometry.Rectangle import Rectangle
from geometry.Point import Point
from geometry.Point import createPointList
import matplotlib.pyplot as plt
from visualiser.visualiser import Visualiser


def findPointsIn(points: list[Point], rect: Rectangle):
    start = perf_counter()
    res = []
    for point in points:
        if rect.containsPoint(point):
            res.append(point)
    end = perf_counter()
    return end-start, len(res)


def checkTimeBuild(algo, points, cap, kd=True):
    start = perf_counter()
    if kd:
        tree = algo(points)
    else:
        tree = algo(points, cap)
    end = perf_counter()
    return end-start, tree


def checkTimeSearch(tree, rect):
    start = perf_counter()
    res = tree.search(rect)
    end = perf_counter()
    return end-start, len(res)


def generate_uniform_points(left=-100, right=100, n=100):
    s = set()
    while len(s) < n:
        x, y = np.random.uniform(left, right), np.random.uniform(left, right)
        s.add((x, y))
    return list(s)


def generate_normal_distr_points(middle=0, dev=100, n=100):
    s = set()
    points = np.random.normal(middle, dev, size=(2, n))
    for i in range(n):
        s.add((points[0][i], points[1][i]))
    return list(s)


def generate_grid_points(jump=2, a=10):
    points = []
    for i in range(a):
        for j in range(a):
            points.append((jump*i, jump*j))
    return points


def generate_cross_points(middle=0, width=100, height=100, n=100,  **kwargs):
    a = n//2
    s = set()
    while len(s) < a:
        x, y = np.random.uniform(middle-width, middle+width), middle
        s.add((x, y))
    while len(s) < n:
        x, y = middle, np.random.uniform(middle-width, middle+width)
        s.add((x, y))
    return list(s)


# A = [10**3, 5*10**3, 10**4, 5*10**4, 10**5, 5*10**5, 10**6]
# B = [30, 75, 100, 200, 500, 800, 1000]


# points_uniform = [generate_uniform_points(-1000, 1000, size) for size in A]
# points_normal = [generate_normal_distr_points(0, 200, size) for size in A]
# points_grid = [generate_grid_points(1, size) for size in B]
# points_cross = [generate_cross_points(0, 1000, size) for size in A]
# pointsList = [createPointList(bbb) for bbb in points_uniform]


rect = Rectangle(Point((-10, -10)), Point((90, 90)))

# points = createPointList(generate_cross_points())
# print(points)
# points = createPointList([(0, 30.422849566273783), (48.134635363912, 0), (60.642834014856845, 0), (49.77651939600119, 0), (0, 66.83484493208857), (1.8310988218477604, 0), (-12.006691225371483, 0), (75.55186776613411, 0), (0, -18.693658385781646), (94.48588488297707, 0), (78.91299463564027, 0), (0, 38.76326252970219), (0, 14.215189394990887), (9.204155645419519, 0), (0, 59.81761551490143), (-49.343940595310464, 0), (0, -15.972508763707012), (-60.16939220572086, 0), (0, 24.68424669502822), (-60.30427556677764, 0), (83.13361858959806, 0), (-32.47310489436393, 0), (64.53499493298983, 0), (0, 52.151178766281134), (30.77612090685156, 0), (0, -6.77034005810313), (-85.23310282321188, 0), (-13.955030333925961, 0), (-38.33186350045978, 0), (-62.95266788202327, 0), (-98.57920758537715, 0), (-63.41219739304713, 0), (0, 65.64783329524596), (0, -58.99681490076956), (0, 25.620470656913014), (0, 65.6512785808003), (34.924349172535926, 0), (0, 10.439390608683837), (-96.17877784409117, 0), (0, 11.676311081371324), (70.89075241752724, 0), (85.55222343830081, 0), (-68.51967698158924, 0), (0, -35.23683281253966), (0, -40.01550400621841), (-34.84659527933556, 0), (-85.71929626795918, 0), (0, -66.57598447350024), (70.9489416293558, 0), (52.9399121650585, 0), (0, -83.78564249470645), (45.806475795334336, 0), (0, 96.07623558256867),
#                           (51.93196373007211, 0), (38.122758436284215, 0), (-75.212582350643, 0), (0, 49.4305011233736), (0, 46.81522484392639), (-46.70126299172637, 0), (61.78794431331559, 0), (0, -14.489904816208309), (0, 95.94927106899453), (0, -35.376946061201295), (0, 59.621719417001), (0, 38.099303998455696), (0, -4.365512300745394), (-81.2641379889512, 0), (0, -1.383932130245924), (-9.18763464184454, 0), (0, 68.88921981548575), (-94.91793233483416, 0), (-39.028638504736925, 0), (-60.98104175158019, 0), (0, -60.02450760409146), (0, 48.75252002341901), (7.568615985560669, 0), (0, 24.553558276751545), (0, -87.965192075364), (37.65203344711642, 0), (0, 22.943740776348548), (0, 96.95322773810639), (-49.324723449890385, 0), (0, -11.239905463511107), (0, -5.334843901681467), (-64.9693051610102, 0), (0, 21.79315508308828), (0, -46.993689878325725), (0, -96.75118880260325), (0, 33.03636104754423), (0, -37.10620055451162), (-50.242478812781385, 0), (69.3190419401061, 0), (0, 57.48676882033939), (0, -12.176116027172654), (0, 56.55274224988921), (78.8696724755253, 0), (0, 82.63558132452457), (0, -57.48365606104422), (0, 71.80902809674842), (97.98726745823117, 0)])


capList = [1, 3, 5]

for i in range(6):
    capList.append(capList[-1]*10)

points = createPointList(generate_uniform_points(-10000, 10000, 10**5))
# ax = plt.subplot()
# vis = Visualiser(ax)

# tree = quadTree(points, 1)
# tree = kdTree(points)

# res = tree.search(rect)
# print(len(res))
# print(len(findPointsIn(points, rect)))
# tree.draw(vis)
# vis.drawRectangle(rect, c='red')
# vis.drawPoints(points, markersize=6, color='darkblue')
# ax.scatter([p.x() for p in points], [p.y()
#            for p in points], s=10)
# vis.drawPoints(res, color='green', markersize=8)
# ax.scatter([p.x() for p in res], [p.y() for p in res], c='green', s=15)

# plt.show()


# for i in range(6, 7):
#     c = chr(i+97)
#     # rect = Rectangle(Point((0, 0)), Point((A[i]//2, A[i]//2)))
#     print("Zbiór ", c, ": ", sep="", end="\n")
#     kdBuildTime, tree1 = checkTimeBuild(kdTree, pointsList[i], True)
#     quadBuildTime, tree2 = checkTimeBuild(
#         quadTree, pointsList[i], False)
#     duration1, resLen1 = checkTimeSearch(tree1, rect)
#     duration2, resLen2 = checkTimeSearch(tree2, rect)
#     print("budowaine: ", round(kdBuildTime, 3), round(quadBuildTime, 3))
#     print("szukanie: ", resLen1, resLen2, round(
#         duration1, 3), round(duration2, 3))


def generateRandomRectangle(left=-1000, right=1000):
    x1, y1 = np.random.uniform(left, right), np.random.uniform(left, right)
    x2, y2 = np.random.uniform(left, right), np.random.uniform(left, right)
    return Rectangle(Point((x1, y1)), Point((x2, y2)))


def compareCap(points, capList):
    bTimes = []
    sTimes = []
    count = []

    for cap in capList:
        print(f'Capacity: {cap}')
        buildTime, tree = checkTimeBuild(quadTree, points, cap, False)
        searchTime, resLen = checkTimeSearch(tree, rect)
        print(f'budowanie: {round(buildTime,3)}')
        print(f'szukanie: {round(searchTime,3)}')
        print(f'ile: {resLen}')
        print('\n')
        bTimes.append(buildTime)
        sTimes.append(searchTime)
        count.append(resLen)

    ax = plt.subplot()
    ax.plot([arg for arg in capList], [val for val in bTimes],
            label='czas budowania', color='darkblue')

    ax.plot([arg for arg in capList], [
        val for val in sTimes], label='czas przeszukiwania', color='purple')
    plt.xlabel("Capacity")
    plt.ylabel("Czas [s]")
    plt.legend()
    plt.show()


def compare(pointsList):
    for points in pointsList:
        print("Liczebność:", len(points))
        kdBuildTime, tree1 = checkTimeBuild(kdTree, points, True)
        quadBuildTime, tree2 = checkTimeBuild(
            quadTree, points, False)
        duration1, resLen1 = checkTimeSearch(tree1, rect)
        duration2, resLen2 = checkTimeSearch(tree2, rect)
        print("budowaine: ", round(kdBuildTime, 3), round(quadBuildTime, 3))
        print("szukanie: ", resLen1, resLen2, round(
            duration1, 3), round(duration2, 3))


def compareWithTrivial(n=10**5, maxTries=100):
    xs = []
    ysKD = []
    ysQuad = []
    ysTrivial = []
    points = createPointList(generate_uniform_points(-1000, 1000, n))
    totalTimeKD, treeKD = checkTimeBuild(kdTree, points)
    totalTimeQuad, treeQuad = checkTimeBuild(quadTree, points, False)
    totalTimeTrivial = 0
    for x in range(0, maxTries):
        rect = generateRandomRectangle()
        # print("Test", x+1)
        xs.append(x+1)
        timeKD, resKD = checkTimeSearch(treeKD, rect)
        timeQuad, resQuad = checkTimeSearch(treeQuad, rect)
        timeTrivial, resTrivial = findPointsIn(points, rect)
        assert (resKD == resQuad == resTrivial), 'cos sie zjebalo'
        totalTimeKD += timeKD
        totalTimeQuad += timeQuad
        totalTimeTrivial += timeTrivial
        ysKD.append(totalTimeKD)
        ysQuad.append(totalTimeQuad)
        ysTrivial.append(totalTimeTrivial)
        # print("KD-Tree:", totalTimeKD)
        # print("Quad-Tree:", totalTimeQuad)
        # print("Trivial:", totalTimeTrivial)
        # print("-----------------")
    ax = plt.subplot()
    ax.plot([arg for arg in xs], [val for val in ysKD],
            label='KD-Tree', color='blue')

    ax.plot([arg for arg in xs], [
        val for val in ysQuad], label='Quad-Tree', color='green')
    ax.plot([arg for arg in xs], [
        val for val in ysTrivial], label='Trivial', color='orange')
    plt.xlabel("Liczba przeszukiwań")
    plt.ylabel("Całkowity czas od rozpoczęcia symulacji [s]")
    plt.legend()
    plt.show()


compareCap(points, capList)
