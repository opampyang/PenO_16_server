__author__ = 'mario'

class Parcel:
    def __init__(self, index, origin, destination):
        self.index = index
        self.origin = origin
        self.destination = destination


    @staticmethod
    def simple_builder():
        parcels = []
        parcels.append(Parcel(142, 1, 2))
        parcels.append(Parcel(145, 2, 3))
        return parcels



class ParcelsHandler:
    def __init__(self, parcels):
        self.available_parcels = parcels
        self.on_the_road_parcels = []
        self.delivered_parcels = []


