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
        if isinstance(o, Vertice):
            v = {}
            v['origin'] = o.origin
            if o.straight is not None:
                v['straight'] = o.straight
            if o.left is not None:
                v['left'] = o.left
            if o.right is not None:
                v['right'] = o.right

            return v
        else:
            return o.__dict__