__author__ = 'mario'

from PenMap import PenMap, MyEncoder
import jsonpickle

class TestMap:


    def test_Map(self):
        map = PenMap()

        assert map is not None

    def test_simple_map(self):
        map = PenMap()
        map.addVertice(3, 2, 4, None)
        map.addVertice(1, 3, 4, None)

        # prin
        # t json.dumps({"vertices": map.vertices, "edges": map.edges})
        m = MyEncoder().encode(map)
        print m
        print "BBB"

t = TestMap()
t.test_simple_map()

