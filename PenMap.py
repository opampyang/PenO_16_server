__author__ = 'mario'

from json import JSONEncoder


class Vertice(object):
    def __init__(self, origin, straight, left, right):
        self.origin = origin
        self.straight = straight
        self.left = left
        self.right = right



class Edge:
    def __init__(self, origin_id, destination_id, distance):
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.distance = distance


class PenMap(object):

    def __init__(self):
        self.vertices = []
        self.edges = []

    def addVertice(self, origin, straight, left, right):
        self.vertices.append(Vertice(origin, straight, left, right))

    def addEdge(self, origin_id, destination_id, distance):
        self.edges.append(Edge(origin_id, destination_id, distance))


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__