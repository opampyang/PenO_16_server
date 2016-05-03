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

    def is_valid_position(self, v1, v2):
        for e in self.edges:
            if e.origin_id == v1 or e.destination_id == v1:
                if v1 == v2:
                    return True
                else:
                    if e.destination_id == v2:
                        return True
        return False

        #
        #
        #
        # if v1 == v2:
        #     i = 0
        #     for v in self.vertices:
        #         if v1 == v[0] or v2 == v[0]:
        #             i = i + 1
        #
        #     if i == 2:
        #         return True
        #     else:
        #         return False
        # else:
        #     ret = False
        #     for v in self.vertices:
        #         if v1 == v[0]:
        #             for e in self.edges:
        #                 if e.origin_id == v1 and e.destination_id == v2:
        #                     ret = True
        #     if ret is True:
        #         return True
        #     else:
        #         return False

    def toJSON(self):
        return MyEncoder().encode(self)

    @staticmethod
    def simple_builder():
        robots_map = PenMap()
        robots_map.addVertice(1,    5, None,   10,    2)
        robots_map.addVertice(2,    6, 	 12,    1,    3)
        robots_map.addVertice(3,    7, None,    2,    4)
        robots_map.addVertice(4,    7,   14,    3,   11)
        robots_map.addVertice(5,    8,    1, None,    6)
        robots_map.addVertice(6,    9,    2,    5,    7)
        robots_map.addVertice(7,    9,    3,    6,    4)
        robots_map.addVertice(8,   10,    5, None,    9)
        robots_map.addVertice(9,   11,    6,    8,    7)
        robots_map.addVertice(10,   8, None,   11,    1)
        robots_map.addVertice(11,   9, None,    4,   10)
        robots_map.addVertice(12,   2,   15, None,   13)
        robots_map.addVertice(13,  15, None,   14,   12)
        robots_map.addVertice(14,   4,   15,   13, None)
        robots_map.addVertice(15,  13, None,   12,   14)

        robots_map.addEdge(1,    2,    70.0)
        robots_map.addEdge(1,    5,    70.0)
        robots_map.addEdge(1,   10,   200.0)
        robots_map.addEdge(2,    3,    70.0)
        robots_map.addEdge(2,    6,    70.0)
        robots_map.addEdge(2,   12,   197.0)
        robots_map.addEdge(3,    2,    70.0)
        robots_map.addEdge(3,    7,    70.0)
        robots_map.addEdge(4,    3,    70.0)
        robots_map.addEdge(4,    7,   115.0)
        robots_map.addEdge(4,   11,   500.0)
        robots_map.addEdge(4,   14,   197.0)
        robots_map.addEdge(5,    1,    70.0)
        robots_map.addEdge(5,    6,    70.0)
        robots_map.addEdge(5,    8,    70.0)
        robots_map.addEdge(6,    2,    70.0)
        robots_map.addEdge(6,    5,    70.0)
        robots_map.addEdge(6,    7,    70.0)
        robots_map.addEdge(7,    3,    70.0)
        robots_map.addEdge(7,    4,   115.0)
        robots_map.addEdge(7,    6,    70.0)
        robots_map.addEdge(7,    9,   115.0)
        robots_map.addEdge(8,    5,    70.0)
        robots_map.addEdge(8,    9,    70.0)
        robots_map.addEdge(9,    6,    70.0)
        robots_map.addEdge(9,    7,   115.0)
        robots_map.addEdge(9,    8,    70.0)
        robots_map.addEdge(10,   1,   200.0)
        robots_map.addEdge(10,   8,    70.0)
        robots_map.addEdge(10,  11,    70.0)
        robots_map.addEdge(11,   4,   500.0)
        robots_map.addEdge(11,   9,    70.0)
        robots_map.addEdge(11,  10,    70.0)
        robots_map.addEdge(12,   2,   197.0)
        robots_map.addEdge(12,  13,    70.0)
        robots_map.addEdge(12,  15,   140.0)
        robots_map.addEdge(13,  12,    70.0)
        robots_map.addEdge(13,  14,    70.0)
        robots_map.addEdge(14,   4,   197.0)
        robots_map.addEdge(14,  13,    70.0)
        robots_map.addEdge(14,  15,   115.0)
        robots_map.addEdge(15,  12,   140.0)
        robots_map.addEdge(15,  13,    70.0)
        robots_map.addEdge(15,  14,   115.0)

        return robots_map

class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Edge):
            return [o.origin_id, o.destination_id, o.distance]
        else:
            return o.__dict__
