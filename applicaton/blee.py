import numpy as np
from kdTree.kdTree import kdTree
from quadTree.quadTree import quadTree
from time import perf_counter
from geometry.Rectangle import Rectangle
from geometry.Point import Point
from geometry.Point import createPointList
import matplotlib.pyplot as plt


def checkTimeBuild(algo, points, kd=True):
    start = perf_counter()
    if kd:
        tree = algo(points)
    else:
        tree = algo(points, 1)
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


# points_uniform = [generate_uniform_points(-1000, 1000, 10**3), generate_uniform_points(-1000, 1000, 10**4),
#                   generate_uniform_points(-1000, 1000, 10**5), generate_uniform_points(-1000, 1000, 10**6)]
# points_normal = [generate_normal_distr_points(0, 200, 10*3), generate_normal_distr_points(
#     0, 200, 10**4), generate_normal_distr_points(0, 200, 10**5), generate_normal_distr_points(0, 200, 10**6)]

# pointsList = [[createPointList(aaa) for aaa in points_uniform], [
#     createPointList(bbb) for bbb in points_normal]]

rect = Rectangle(Point((-10, -10)), Point((90, 90)))

points = createPointList(generate_uniform_points(-100, 100, 200))
points = createPointList([(65.38716669798333, 64.4079373352395), (-40.11259285795259, -44.311424082839366), (-64.03864930553439, 20.839656637771256), (89.31599199496534, 69.32782369894633), (-16.78168393104073, -79.62082994710231), (-77.30232274494008, -58.93596121299183), (-75.34376727868369, 12.198491353995848), (66.65022930486711, 48.903962210742804), (60.702878615451, -79.24091767936712), (65.18100906813007, -97.23882499475714), (-62.056287432142824, -76.19624557225693), (69.03316459682989, -36.93023264779054), (59.080435160724335, 16.866764132476007), (-35.349838342756115, -35.56780637737218), (68.96637347438363, 33.77583652690572), (6.181264273989058, 83.39598585522216), (34.52571137103351, -78.94443938399971), (-47.1970992594227, 86.42944658077602), (6.522892580658365, 25.837267676162725), (-3.2373261351974065, 78.54427912641108), (90.57266492412592, -91.47689742635865), (-27.517637757513924, -60.0798173384705), (-22.801934852935332, 57.89522823355176), (-84.92330868655506, 40.93603835121644), (18.12393907062362, 27.32108291437811), (-16.00375502774611, -71.19889769635364), (-22.828870555017772, -12.328717433017971), (-46.56307072204899, -47.506276835669034), (-58.41388650091795, 37.095831572307276), (-42.14914367648828, -15.732206393984157), (-72.48299334457298, 26.535084671468482), (71.57774976680679, -74.14054784030404), (-43.59511320580203, 70.3461696462503), (43.74194087564885, -16.10943593827902), (9.919305535754418, 83.04811432728064), (86.60536688995242, 76.21311929261182), (72.9103422030359, 52.14338756380141), (-73.59374172355047, 26.573644492883645), (34.71083702266276, -48.52683700779865), (65.87332721707648, 47.590691337523424), (-8.298235413921006, 23.87379175061386), (81.94967159816463, -17.775243061505194), (-33.85041489200853, 37.621401468947454), (-38.43806572267996, 47.42111205772471), (39.12805263869069, 49.14369894700883), (39.800056200064375, 74.69446989580345), (-9.43241300924413, 15.106994976429107), (19.250672542677492, -1.3671774061517965), (26.30493029889638, -82.37923711741509), (65.2753351553097, 98.69114775043218), (-22.725481137384037, -24.36916793574582), (39.4871293800675, 19.629012618965618), (1.1257479295004629, 84.90223828249489), (-23.453822007811056, -68.00148528913124), (41.41926368100388, -37.843073038274255), (40.04777593112249, 46.017458228726696), (-0.54891633551361, 77.52915990047217), (-63.211735564680296, 94.80849171990442), (-76.94757423446916, -73.4879339796371), (12.840479022900354, 17.962220666401095), (-11.712040254974681, 14.109801474923714), (-85.04038402792455, 12.936178778006322), (-44.739317673487975, 24.123763660778124), (51.35554456031298, -40.0083239272095), (79.63580695434572, -13.18519782523515), (-64.82931171271768, 64.12959637619576), (-9.04069984844105, -68.89245282764283), (94.72152815965916, 90.54782138158382), (-2.433519881822079, -38.78051119133718), (-6.864181802804012, 78.54853197136856), (-59.2344502867785, 30.110502908670213), (-49.1470926916743, 9.288221991516352), (-86.14734071060828, 46.39847004297931), (5.320774464808451, 65.65504159161742), (-93.84672562113285, -62.5941138763294), (7.110040480353604, -38.54283637193101), (77.09718275781785, -34.391626967653096), (-5.874117215329846, 61.56275443770306), (-57.86408617729259, 51.07427293629755), (64.83316348783544, 1.574911055823705), (73.551309650664, -42.6783497738606), (57.67955134461124, 22.558295873875593), (-10.781824162212231, -8.882896335145901), (89.74765774699273, -79.62960464259304), (-64.24592065769093, -7.82200509787134), (34.0778277043687, -42.99946878936065), (-78.31522984706996, -12.298688973520129), (-76.52112070846265, 2.827630065477166), (65.9821181997614, -36.4865337083041), (51.17326429884474, -35.933506191702975), (-58.17776154027015, 99.24642563839018), (-76.341430473158, 21.21750551365882), (45.28808555788103, -64.02340727217566), (23.075767879517855, -78.45592936850998), (-36.98905481083037, -92.31206901804929), (71.65467596321747, -36.32696190735221), (-23.446736356478226, -54.0555301502996), (2.005723854902584, 15.819816326382437), (-16.373490296297774, 10.50656650385271), (48.182961762100945, 85.36975641757368),
                         (-7.02957951073779, 84.30999361745367), (3.518186276390537, -82.89179975637133), (-0.6006688021010973, 64.30928452455794), (76.72613890914758, 53.13187779496255), (-48.90096461759204, -85.89664256302163), (32.09518925429623, 95.8505525899267), (-51.76982307544178, -71.40721638061645), (72.27055511572257, -25.917610703688055), (-58.08987563729142, 21.19888133620975), (83.55512690448708, 99.08804239108869), (-36.59140843686095, -80.73116205933637), (88.1032038337847, 25.28191042499745), (32.98927299182154, 39.60093090123769), (76.14634792068165, 84.12690416950744), (-98.95629635666074, -22.736056554836566), (11.328948120168533, 88.00946222206338), (-38.668969095869656, 33.414547730277405), (-32.563217650898665, -82.01687529830812), (2.7622979080123855, 10.430352756703499), (29.142784974591194, 21.244953180736672), (14.508417946123544, -20.653611050597178), (41.657353707505735, -42.03318365402158), (-81.94736722755076, 52.18451725581886), (19.377046435394703, 75.82750365558084), (-32.262941729690596, -91.86474505846978), (35.55118562260469, 56.76105228316223), (79.54576059572733, 33.84586335731089), (-1.9253059644251067, -94.932657742661), (-60.91731774416358, -15.459814937484452), (-79.55031802461481, 66.5712421221804), (-64.745899361013, 84.18728739896767), (-52.68428838928947, 78.61814211138389), (80.95954848995044, 49.995042502532726), (97.084174587853, 6.5810093501046225), (65.19493068754906, -23.88987829417229), (57.25134964900812, 54.62138251208077), (57.44601298824486, -87.34847232103967), (-54.387372642260345, 57.89957775790239), (-98.56869030967377, -9.65620059410115), (-80.44262611484491, -79.65460411118337), (-17.645427531847545, -57.68703664031201), (64.05452040813378, 97.64284978731575), (-9.423007329557748, -39.052135695212286), (1.2906780077107385, 40.95842646670761), (99.18380386207625, -65.84514467994805), (0.4411308641453644, 83.27288355900154), (-59.09024356115098, 17.021897023623737), (-55.83586612284659, -16.99097645967369), (42.81749750182698, 86.47694752350986), (-30.276787344438944, -81.73084503610124), (-24.64725033261763, 46.4820602476255), (70.43753298286163, 6.741205218440598), (-47.47019984200431, -9.806715194136643), (34.45010692719512, -10.361051468927812), (78.10947853337714, 69.0062679161386), (-52.092531991616255, 31.82921220688911), (-92.06398317628167, -6.574028718203451), (-34.04495992345058, 82.08032997179697), (73.39810603614805, 78.07137472129097), (-39.76726708298857, -96.80214208437606), (8.402401333266198, 98.89429338840637), (-51.890386653624596, 85.12997767132188), (52.30105986157051, -71.3475004856128), (-2.46768587065489, -55.25186546679735), (5.663901803010134, -85.83118086131682), (-81.75018679690368, -79.99871842079303), (-85.01063920238232, 64.55121289345237), (41.66595845160609, 31.084741958053286), (-72.82610040096509, 13.7465226841436), (-40.82074878443878, -99.62882983744814), (-82.7156989222229, 23.849978628943163), (-93.61408470195538, 12.887275678721252), (79.2549355019845, 61.92768610361088), (-86.19904617081606, 96.99512702345683), (39.81466155338623, 56.446210231006205), (67.6679875403328, 21.411685465842623), (-82.5436139764971, 43.36179876452391), (-77.69082009885575, 93.9062624248611), (-47.94548953967048, 57.801817722935766), (-66.90349010426416, 25.55335217199557), (15.128748755707505, -10.141865445034725), (59.815696724803985, 59.74169200055607), (43.59934412560747, -92.34603807269532), (78.78408471307557, -94.25966598621743), (-77.81419375957947, -85.97147550107893), (68.04354679726322, 11.24387744783391), (74.25107613488498, -45.700717062638276), (-31.25820516586444, 20.5162159816265), (-20.525366805152714, -83.86027052049563), (68.17798582519654, 26.249748976086963), (-30.931210639131024, 47.99941987698918), (23.591971391075163, 62.29118873530152), (5.17255771373253, -97.41906469597113), (-94.49891967622108, -63.70266428284965), (12.29816597760383, 94.3168074968176), (-82.2936327618806, -10.504600393532073), (-50.12902283075134, -38.76394517291717), (-11.261625074990334, 50.0255707715624), (-57.55660556149573, 99.94346939752941), (36.857244070610875, 61.817774102959135)])
# print(points)
tree = quadTree(points, 1)
tree = kdTree(points)
res = tree.search(rect)
print(len(res))

ax = plt.subplot()
tree.draw(ax)
rect.draw(ax, c='red', lw=3)
ax.scatter([p.x() for p in points], [p.y()
           for p in points], s=10)
ax.scatter([p.x() for p in res], [p.y() for p in res], c='green', s=15)

plt.show()


# for i in range(2):
#     for j in range(4):
#         c = chr(j+97)
#         print("Zbiór ", i+1, c, ": ", sep="", end="\n")
#         kdBuildTime, tree1 = checkTimeBuild(kdTree, pointsList[i][j], True)
#         quadBuildTime, tree2 = checkTimeBuild(
#             quadTree, pointsList[i][j], False)
#         duration1, resLen1 = checkTimeSearch(tree1, rect)
#         duration2, resLen2 = checkTimeSearch(tree2, rect)
#         print("budowaine: ", round(kdBuildTime, 3), round(quadBuildTime, 3))
#         print("szukanie: ", resLen1, resLen2, round(
#             duration1, 3), round(duration2, 3))
