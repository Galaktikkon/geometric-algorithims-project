from geometry.Point import Point
import json


class visualisationParameters:

    def __init__(self):
        self.name: str = None
        self.treeType: str = None
        self.points: list[Point] = None

    def setName(self, name: str, names: str) -> str:
        assert name not in names, "names are to be unique"
        self.name = name

    def setTreeType(self, treeType: str) -> str:
        self.treeType = treeType

    def setPoints(self, points: list[Point]) -> list[Point]:
        assert len(points), "number of points is to be greater than 0"
        self.points = points

    def parametersToJson(self):
        return json.dumps({
            "name": self.Name,
            "treeType": self.TreeType,
            "points": self.Points
        })

    def parametersFromJson(self, jsonFile):
        parameters = json.loads(jsonFile)
        self.setName = parameters["name"]
        self.treeType = parameters["treeType"]
        self.points = parameters["points"]
