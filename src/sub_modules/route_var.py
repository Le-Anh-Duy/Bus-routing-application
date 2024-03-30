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

import inspect

class RouteVar:

	def __init__(self, data):
		RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, OutBound, RunningTime = data
		self._routeId = RouteId
		self._routeVarId = RouteVarId
		self._routeVarName = RouteVarName
		self._routeVarShortName = RouteVarShortName
		self._routeNo = RouteNo
		self._startStop = StartStop
		self._endStop = EndStop
		self._distance = Distance
		self._outBound = OutBound
		self._runningTime = RunningTime

	@property
	def routeVarName(self):
		return self._routeVarName

	@property
	def routeVarShortName(self):
		return self._routeVarShortName

	@property
	def routeNo(self):
		return self._routeNo

	@property
	def startStop(self):
		return self._startStop

	@property
	def endStop(self):
		return self._endStop

	@property
	def distance(self):
		return self._distance

	@property
	def runningTime(self):
		return self._runningTime

	@property
	def outBound(self):
		return self._outBound

	@routeVarName.setter
	def routeVarName(self, new_routeVarName):
		self._routeVarName = new_routeVarName

	@routeVarShortName.setter
	def routeVarShortName(self, new_routeVarShortName):
		self._routeVarShortName = new_routeVarShortName

	@routeNo.setter
	def routeNo(self, new_routeNo):
		self._routeNo = new_routeNo

	@startStop.setter
	def startStop(self, new_startStop):
		self._startStop = new_startStop

	@endStop.setter
	def endStop(self, new_endStop):
		self._endStop = new_endStop

	@distance.setter
	def distance(self, new_distance):
		self._distance = new_distance

	@runningTime.setter
	def runningTime(self, new_runningTime):
		self._runningTime = new_runningTime

	@outBound.setter
	def outBound(self, new_outBound):
		self._outBound = new_outBound

	def get_keys(self):
		return [
			'_routeId',
			'_routeVarId',
			'_routeVarName',
			'_routeVarShortName',
			'_routeNo',
			'_startStop',
			'_endStop',
			'_distance',
			'_outBound',
			'_runningTime'
		]

	def to_dict(self):
		return {
			'routeId': self._routeId,
			'routeVarId': self._routeVarId,
			'routeVarName': self._routeVarName,
			'routeVarShortName': self._routeVarShortName,
			'routeNo': self._routeNo,
			'startStop': self._startStop,
			'endStop': self._endStop,
			'distance': self._distance,
			'outBound': self._outBound,
			'runningTime': self._runningTime
		}

	def __str__(self) -> dict:
		return str(self.__dict__)
