class Stop:
    def __init__(self, StopId, Code, Name, StopType, Zone, Ward, AddressNo, Street, SupportDisability, Status, Lng, Lat, Search, Routes):
        self._stopId = StopId
        self._code = Code
        self._name = Name
        self._stopType = StopType
        self._zone = Zone
        self._ward = Ward
        self._addressNo = AddressNo
        self._street = Street
        self._supportDisability = SupportDisability
        self._status = Status
        self._lng = Lng
        self._lat = Lat
        self._search = Search
        self._routes = Routes

    @property
    def stopId(self):
        return self._stopId

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def stopType(self):
        return self._stopType

    @property
    def zone(self):
        return self._zone

    @property
    def ward(self):
        return self._ward

    @property
    def addressNo(self):
        return self._addressNo

    @property
    def street(self):
        return self._street

    @property
    def supportDisability(self):
        return self._supportDisability

    @property
    def status(self):
        return self._status

    @property
    def lng(self):
        return self._lng

    @property
    def lat(self):
        return self._lat

    @property
    def search(self):
        return self._search

    @property
    def routes(self):
        return self._routes

    # Add setter methods for properties that need to be modified

    # Example setter for demonstration
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Add other setter methods for properties as needed

# # Example usage:
# stop = Stop(1, "ABC", "Main Street", "Bus Stop", 1, "Central", 123, "Main St.", True, "Active", -73.987, 40.748, "Main St. Bus Stop", ["Route1", "Route2"])
# print(stop.name)  # Output: Main Street

# # Example setter usage
# stop.name = "New Main Street"
# print(stop.name)  # Output: New Main Street
