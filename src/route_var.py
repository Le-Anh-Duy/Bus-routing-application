# with var is variations


# **Users:**
# - `RouteNo`
# - `RouteVarName`
# - `RouteVarShortName`
# - `StartStop`
# - `EndStop`
# - `RunningTime`
# - `OutBound`

# **Admin:**
# - `RouteID`
# - `routeVarId`


#build a getter and setter functions

class RouteVar:
	def __init__(self, RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, OutBound, RunningTime):
		self._routeId = RouteId
		self._routeVarId = RouteVarId
		self.routeVarName = RouteVarName
		self.routeVarShortName = RouteVarShortName
		self.routeNo = RouteNo
		self.startStop = StartStop
		self.endStop = EndStop
		self.distance = Distance
		self.outBound = OutBound
		self.runningTime = RunningTime

	def get_start_end(self):
		return {"startStop": self.startStop, "endStop": self.endStop}

	def __str__(self):
		return f"Route Variation ID: {self.routeVarId}, Route: {self.routeNo}, Start Stop: {self.startStop}, End Stop: {self.endStop}, Distance: {self.distance}, Outbound: {self.outbound}, Running Time: {self.runningTime}"
