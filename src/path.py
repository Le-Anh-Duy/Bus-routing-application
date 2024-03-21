class path:
    def __init__(self, data):
        lat, lng, RouteId, RouteVarId = data
        self._lat = lat
        self._lng = lng
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    @property
    def RouteId(self):
        return self._RouteId

    @property
    def RouteVarId(self):
        return self._RouteVarId

    def get_keys(self):
        return [
            "_lat",
            "_lng",
            "_RouteId",
            "_RouteVarId"
        ]

    def to_dict(self):
        return {
            "lat": self._lat,
            "lng": self._lng,
            "RouteId": self._RouteId,
            "RouteVarId": self._RouteVarId
        }
