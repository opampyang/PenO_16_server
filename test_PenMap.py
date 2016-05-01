__author__ = 'mario'

from PenMap import PenMap, MyEncoder
import jsonpickle

class TestMap:


    def test_Map(self):
        map = PenMap()

        assert map is not None

    def test_simple_map(self):
        map = PenMap()
        map.addVertice(1, 3, 2, 4, None)
        map.addVertice(2, 1, 3, 4, None)

        map.addEdge(1, 2, 0.3)
        map.addEdge(1, 3, 0.5)
        map.addEdge(3, 1, 0.5)



        # prin
        # t json.dumps({"vertices": map.vertices, "edges": map.edges})
        m = MyEncoder().encode(map)
        print m
        print "BBB"

    def test_valid_position(self):
        map = PenMap()
        map.addVertice(1, 3, 2, 4, None)
        map.addVertice(2, 1, 3, 4, None)
        map.addEdge(1, 2, 0.3)

        assert map.is_valid_position(3, 3) is False
        assert map.is_valid_position(1, 1) is True
        assert map.is_valid_position(1, 2) is True
        assert map.is_valid_position(2, 2) is True
        assert map.is_valid_position(2, 1) is False


t = TestMap()
t.test_simple_map()

