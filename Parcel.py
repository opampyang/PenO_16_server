from json import JSONEncoder

__author__ = 'mario'

class Parcel:
    def __init__(self, parcel_id, origin, destination):
        self.parcel_id = parcel_id
        self.origin = origin
        self.destination = destination
        self.team_id = ""


    def has_team(self, team_id):
        if self.team_id is team_id:
            return True
        else:
            return False


    def add_team_id(self, team_id):
        self.team_id = team_id

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


    def claim_parcel(self, team_id, parcel_id):
        ret = False
        for parcel in self.available_parcels:
            if parcel.parcel_id == parcel_id and not parcel.has_team(team_id):
                parcel.add_team_id(team_id)
                self.available_parcels.remove(parcel)
                self.on_the_road_parcels.append(parcel)
                ret = True

        return ret

    def delivered(self, team_id, parcel_id):
        ret = False
        for parcel in self.on_the_road_parcels:
            if parcel.parcel_id == parcel_id and parcel.has_team(team_id):
                self.on_the_road_parcels.remove(parcel)
                self.delivered_parcels.append(parcel)
                ret = True

        return ret

    def toJSON(self):
        return MyEncoder().encode(self)


class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Parcel):
            if o.team_id is not "":
                return [o.parcel_id, o.origin, o.destination, o.team_id]
            else:
                return [o.parcel_id, o.origin, o.destination]
        else:
            # return o.__dict__
            return {'available-parcels': o.available_parcels,
                    'on-the-road-parcels': o.on_the_road_parcels,
                    'delivered-parcels': o.delivered_parcels}