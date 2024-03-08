# with var is variations

class RouteVar:
	def __init__(self, RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, OutBound, RunningTime):
		self.routeId = RouteId
		self.routeVarId = RouteVarId
		self.routeVarName = RouteVarName
		self.routeVarShortName = RouteVarShortName
		self.routeNo = RouteNo
		self.startStop = StartStop
		self.endStop = EndStop
		self.distance = Distance
		self.outBound = OutBound
		self.runningTime = RunningTime

	def __str__(self):
		return f"Route Variation ID: {self.routeVarId}, Route: {self.routeNo}, Start Stop: {self.startStop}, End Stop: {self.endStop}, Distance: {self.distance}, Outbound: {self.outbound}, Running Time: {self.runningTime}"
