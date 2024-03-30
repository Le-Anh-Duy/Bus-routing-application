class Path:
    def __init__(self, data):
        lat, lng, RouteId, RouteVarId = data
        self._lat = lat
        self._lng = lng
        self._routeId = RouteId
        self._routeVarId = RouteVarId

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    @property
    def routeId(self):
        return self._routeId

    @property
    def routeVarId(self):
        return self._routeVarId

    @lat.setter
    def lat(self, new_lat):
        self._lat = new_lat

    @lng.setter
    def lng(self, new_lng):
        self._lng = new_lng

    @routeId.setter
    def routeId(self, new_RouteId):
        self._routeId = new_RouteId

    @routeVarId.setter
    def routeVarId(self, new_RouteVarId):
        self._routeVarId = new_RouteVarId

    def get_keys(self):
        return [
            "_lat",
            "_lng",
            "_routeId",
            "_routeVarId"
        ]

    def to_dict(self):
        return {
            "lat": self._lat,
            "lng": self._lng,
            "routeId": self._routeId,
            "routeVarId": self._routeVarId
        }
