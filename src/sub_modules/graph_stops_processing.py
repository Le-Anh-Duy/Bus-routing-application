from cord_convert import converter

class node:
    def __init__(self, stopId, lat, lng):
        self.stopId = stopId # -1: not a stop, x >= 0: stopId
        self.lat = lat
        self.lng = lng
        self.x, self.y = converter().convert(lat, lng)

class graph_stops:
    def __init__(self, stops, nodes, adj):
        self.stops = []
        self.nodes = []
        self.adj = []