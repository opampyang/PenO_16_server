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
        parcels.append(Parcel(	1	,	3	, 	4	))
        parcels.append(Parcel(	2	,	13	, 	8	))
        parcels.append(Parcel(	3	,	11	, 	8	))
        parcels.append(Parcel(	4	,	10	, 	11	))
        parcels.append(Parcel(	5	,	5	, 	9	))
        parcels.append(Parcel(	6	,	15	, 	12	))
        parcels.append(Parcel(	7	,	10	, 	4	))
        parcels.append(Parcel(	8	,	5	, 	6	))
        parcels.append(Parcel(	9	,	14	, 	5	))
        parcels.append(Parcel(	10	,	4	, 	6	))
        parcels.append(Parcel(	11	,	10	, 	4	))
        parcels.append(Parcel(	12	,	3	, 	2	))
        parcels.append(Parcel(	13	,	8	, 	13	))
        parcels.append(Parcel(	14	,	9	, 	3	))
        parcels.append(Parcel(	15	,	14	, 	13	))
        parcels.append(Parcel(	16	,	3	, 	6	))
        parcels.append(Parcel(	17	,	13	, 	6	))
        parcels.append(Parcel(	18	,	1	, 	8	))
        parcels.append(Parcel(	19	,	3	, 	2	))
        parcels.append(Parcel(	20	,	13	, 	14	))
        parcels.append(Parcel(	21	,	15	, 	2	))
        parcels.append(Parcel(	22	,	6	, 	3	))
        parcels.append(Parcel(	23	,	12	, 	9	))
        parcels.append(Parcel(	24	,	14	, 	15	))
        parcels.append(Parcel(	25	,	5	, 	10	))
        parcels.append(Parcel(	26	,	5	, 	7	))
        parcels.append(Parcel(	27	,	5	, 	12	))
        parcels.append(Parcel(	28	,	2	, 	4	))
        parcels.append(Parcel(	29	,	14	, 	2	))
        parcels.append(Parcel(	30	,	6	, 	15	))
        parcels.append(Parcel(	31	,	11	, 	2	))
        parcels.append(Parcel(	32	,	14	, 	10	))
        parcels.append(Parcel(	33	,	12	, 	7	))
        parcels.append(Parcel(	34	,	11	, 	15	))
        parcels.append(Parcel(	35	,	11	, 	13	))
        parcels.append(Parcel(	36	,	1	, 	9	))
        parcels.append(Parcel(	37	,	8	, 	2	))
        parcels.append(Parcel(	38	,	3	, 	12	))
        parcels.append(Parcel(	39	,	4	, 	11	))
        parcels.append(Parcel(	40	,	1	, 	9	))
        parcels.append(Parcel(	41	,	6	, 	14	))
        parcels.append(Parcel(	42	,	2	, 	5	))
        parcels.append(Parcel(	43	,	10	, 	14	))
        parcels.append(Parcel(	44	,	3	, 	5	))
        parcels.append(Parcel(	45	,	10	, 	6	))
        parcels.append(Parcel(	46	,	7	, 	12	))
        parcels.append(Parcel(	47	,	4	, 	3	))
        parcels.append(Parcel(	48	,	2	, 	1	))
        parcels.append(Parcel(	49	,	6	, 	10	))
        parcels.append(Parcel(	50	,	13	, 	12	))
        parcels.append(Parcel(	51	,	2	, 	3	))
        parcels.append(Parcel(	52	,	6	, 	9	))
        parcels.append(Parcel(	53	,	2	, 	8	))
        parcels.append(Parcel(	54	,	4	, 	10	))
        parcels.append(Parcel(	55	,	12	, 	3	))
        parcels.append(Parcel(	56	,	14	, 	3	))
        parcels.append(Parcel(	57	,	13	, 	12	))
        parcels.append(Parcel(	58	,	11	, 	10	))
        parcels.append(Parcel(	59	,	5	, 	11	))
        parcels.append(Parcel(	60	,	13	, 	3	))
        parcels.append(Parcel(	61	,	12	, 	5	))
        parcels.append(Parcel(	62	,	14	, 	10	))
        parcels.append(Parcel(	63	,	6	, 	3	))
        parcels.append(Parcel(	64	,	2	, 	5	))
        parcels.append(Parcel(	65	,	4	, 	1	))
        parcels.append(Parcel(	66	,	10	, 	5	))
        parcels.append(Parcel(	67	,	12	, 	8	))
        parcels.append(Parcel(	68	,	6	, 	11	))
        parcels.append(Parcel(	69	,	6	, 	4	))
        parcels.append(Parcel(	70	,	4	, 	1	))
        parcels.append(Parcel(	71	,	2	, 	1	))
        parcels.append(Parcel(	72	,	14	, 	2	))
        parcels.append(Parcel(	73	,	4	, 	7	))
        parcels.append(Parcel(	74	,	1	, 	2	))
        parcels.append(Parcel(	75	,	2	, 	9	))
        parcels.append(Parcel(	76	,	3	, 	4	))
        parcels.append(Parcel(	77	,	13	, 	7	))
        parcels.append(Parcel(	78	,	7	, 	11	))
        parcels.append(Parcel(	79	,	8	, 	15	))
        parcels.append(Parcel(	80	,	8	, 	12	))
        parcels.append(Parcel(	81	,	12	, 	2	))
        parcels.append(Parcel(	82	,	9	, 	8	))
        parcels.append(Parcel(	83	,	11	, 	4	))
        parcels.append(Parcel(	84	,	12	, 	2	))
        parcels.append(Parcel(	85	,	6	, 	5	))
        parcels.append(Parcel(	86	,	4	, 	13	))
        parcels.append(Parcel(	87	,	13	, 	12	))
        parcels.append(Parcel(	88	,	7	, 	6	))
        parcels.append(Parcel(	89	,	15	, 	5	))
        parcels.append(Parcel(	90	,	3	, 	5	))
        parcels.append(Parcel(	91	,	6	, 	7	))
        parcels.append(Parcel(	92	,	5	, 	12	))
        parcels.append(Parcel(	93	,	7	, 	10	))
        parcels.append(Parcel(	94	,	1	, 	7	))
        parcels.append(Parcel(	95	,	5	, 	1	))
        parcels.append(Parcel(	96	,	3	, 	13	))
        parcels.append(Parcel(	97	,	6	, 	2	))
        parcels.append(Parcel(	98	,	5	, 	10	))
        parcels.append(Parcel(	99	,	13	, 	5	))
        parcels.append(Parcel(	100	,	15	, 	14	))
        parcels.append(Parcel(	101	,	2	, 	1	))
        parcels.append(Parcel(	102	,	8	, 	15	))
        parcels.append(Parcel(	103	,	9	, 	2	))
        parcels.append(Parcel(	104	,	2	, 	12	))
        parcels.append(Parcel(	105	,	2	, 	9	))
        parcels.append(Parcel(	106	,	8	, 	9	))
        parcels.append(Parcel(	107	,	8	, 	6	))
        parcels.append(Parcel(	108	,	4	, 	13	))
        parcels.append(Parcel(	109	,	6	, 	4	))
        parcels.append(Parcel(	110	,	11	, 	13	))
        parcels.append(Parcel(	111	,	2	, 	9	))
        parcels.append(Parcel(	112	,	6	, 	13	))
        parcels.append(Parcel(	113	,	15	, 	5	))
        parcels.append(Parcel(	114	,	14	, 	13	))
        parcels.append(Parcel(	115	,	14	, 	3	))
        parcels.append(Parcel(	116	,	7	, 	5	))
        parcels.append(Parcel(	117	,	13	, 	10	))
        parcels.append(Parcel(	118	,	11	, 	13	))
        parcels.append(Parcel(	119	,	3	, 	6	))
        parcels.append(Parcel(	120	,	11	, 	2	))
        parcels.append(Parcel(	121	,	12	, 	4	))
        parcels.append(Parcel(	122	,	13	, 	12	))
        parcels.append(Parcel(	123	,	13	, 	3	))
        parcels.append(Parcel(	124	,	9	, 	3	))
        parcels.append(Parcel(	125	,	12	, 	9	))
        parcels.append(Parcel(	126	,	4	, 	8	))
        parcels.append(Parcel(	127	,	13	, 	9	))
        parcels.append(Parcel(	128	,	2	, 	13	))
        parcels.append(Parcel(	129	,	14	, 	7	))
        parcels.append(Parcel(	130	,	2	, 	6	))
        parcels.append(Parcel(	131	,	5	, 	4	))
        parcels.append(Parcel(	132	,	6	, 	5	))
        parcels.append(Parcel(	133	,	12	, 	3	))
        parcels.append(Parcel(	134	,	2	, 	3	))
        parcels.append(Parcel(	135	,	11	, 	3	))
        parcels.append(Parcel(	136	,	1	, 	6	))
        parcels.append(Parcel(	137	,	9	, 	14	))
        parcels.append(Parcel(	138	,	10	, 	12	))
        parcels.append(Parcel(	139	,	10	, 	4	))
        parcels.append(Parcel(	140	,	4	, 	3	))
        parcels.append(Parcel(	141	,	3	, 	6	))
        parcels.append(Parcel(	142	,	2	, 	7	))
        parcels.append(Parcel(	143	,	3	, 	8	))
        parcels.append(Parcel(	144	,	8	, 	2	))
        parcels.append(Parcel(	145	,	8	, 	10	))
        parcels.append(Parcel(	146	,	6	, 	4	))
        parcels.append(Parcel(	147	,	12	, 	6	))
        parcels.append(Parcel(	148	,	2	, 	3	))
        parcels.append(Parcel(	149	,	7	, 	1	))
        parcels.append(Parcel(	150	,	2	, 	7	))
        parcels.append(Parcel(	151	,	3	, 	14	))
        parcels.append(Parcel(	152	,	11	, 	3	))
        parcels.append(Parcel(	153	,	10	, 	13	))
        parcels.append(Parcel(	154	,	1	, 	15	))
        parcels.append(Parcel(	155	,	4	, 	14	))
        parcels.append(Parcel(	156	,	11	, 	10	))
        parcels.append(Parcel(	157	,	11	, 	3	))
        parcels.append(Parcel(	158	,	8	, 	4	))
        parcels.append(Parcel(	159	,	13	, 	12	))
        parcels.append(Parcel(	160	,	9	, 	7	))
        parcels.append(Parcel(	161	,	9	, 	3	))
        parcels.append(Parcel(	162	,	5	, 	3	))
        parcels.append(Parcel(	163	,	13	, 	12	))
        parcels.append(Parcel(	164	,	4	, 	5	))
        parcels.append(Parcel(	165	,	11	, 	10	))
        parcels.append(Parcel(	166	,	6	, 	10	))
        parcels.append(Parcel(	167	,	4	, 	6	))
        parcels.append(Parcel(	168	,	12	, 	11	))
        parcels.append(Parcel(	169	,	3	, 	15	))
        parcels.append(Parcel(	170	,	3	, 	5	))
        parcels.append(Parcel(	171	,	10	, 	11	))
        parcels.append(Parcel(	172	,	7	, 	9	))
        parcels.append(Parcel(	173	,	10	, 	4	))
        parcels.append(Parcel(	174	,	3	, 	12	))
        parcels.append(Parcel(	175	,	3	, 	4	))
        parcels.append(Parcel(	176	,	9	, 	4	))
        parcels.append(Parcel(	177	,	2	, 	1	))
        parcels.append(Parcel(	178	,	4	, 	7	))
        parcels.append(Parcel(	179	,	7	, 	3	))
        parcels.append(Parcel(	180	,	3	, 	6	))
        parcels.append(Parcel(	181	,	5	, 	8	))
        parcels.append(Parcel(	182	,	11	, 	10	))
        parcels.append(Parcel(	183	,	11	, 	6	))
        parcels.append(Parcel(	184	,	8	, 	9	))
        parcels.append(Parcel(	185	,	14	, 	3	))
        parcels.append(Parcel(	186	,	12	, 	9	))
        parcels.append(Parcel(	187	,	10	, 	6	))
        parcels.append(Parcel(	188	,	12	, 	8	))
        parcels.append(Parcel(	189	,	8	, 	5	))
        parcels.append(Parcel(	190	,	10	, 	9	))
        parcels.append(Parcel(	191	,	1	, 	12	))
        parcels.append(Parcel(	192	,	6	, 	2	))
        parcels.append(Parcel(	193	,	3	, 	8	))
        parcels.append(Parcel(	194	,	11	, 	5	))
        parcels.append(Parcel(	195	,	6	, 	9	))
        parcels.append(Parcel(	196	,	14	, 	5	))
        parcels.append(Parcel(	197	,	10	, 	5	))
        parcels.append(Parcel(	198	,	5	, 	8	))
        parcels.append(Parcel(	199	,	14	, 	7	))
        parcels.append(Parcel(	200	,	11	, 	12	))
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
            return o.__dict__
