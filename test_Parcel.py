__author__ = 'mario'
from Parcel import Parcel, ParcelsHandler

class TestParcel:

    def test_Parcel_Builder(self):
        parcels = Parcel.simple_builder()
        assert len(parcels) == 2

    def test_Parcel_JSON(self):
        handler = ParcelsHandler(Parcel.simple_builder())
        json = handler.toJSON()
        assert '{"on_the_road_parcels": [], "delivered_parcels": [], "available_parcels": [[142, 1, 2], [145, 2, 3]]}' == json

    def test_claim_parcel(self):
        handler = ParcelsHandler(Parcel.simple_builder())
        assert handler.claim_parcel("a-team", 142) is True
        assert handler.claim_parcel("a-team", 142) is False
        assert handler.claim_parcel("b-team", 142) is False


    def test_deliver_parcel(self):
        handler = ParcelsHandler(Parcel.simple_builder())
        assert handler.claim_parcel("a-team", 142) is True
        assert len(handler.on_the_road_parcels) == 1

        assert handler.delivered("a-team", 142) is True
        assert len(handler.on_the_road_parcels) == 0
        assert len(handler.delivered_parcels) == 1



if __name__ == "__main__":
    t = TestParcel()
    t.test_Parcel_JSON()

