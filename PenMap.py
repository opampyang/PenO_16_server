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

    def addVertice(self, vertice_index, origin, straight, left, right):
        self.vertices.append([vertice_index, Vertice(origin, straight, left, right)])

    def addEdge(self, origin_id, destination_id, distance):
        self.edges.append(Edge(origin_id, destination_id, distance))


    def toJSON(self):
        return MyEncoder().encode(self)

    @staticmethod
    def simple_builder():
        robots_map = PenMap()
        robots_map.addVertice(1, 3, 2, 4, None)
        robots_map.addVertice(2, 1, 3, 4, None)

        robots_map.addEdge(1, 2, 0.3)
        robots_map.addEdge(1, 3, 0.5)
        robots_map.addEdge(3, 1, 0.5)

        return robots_map

class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Edge):
            return [o.origin_id, o.destination_id, o.distance]
        else:
            return o.__dict__