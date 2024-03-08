# solo-project

This will be my document of this solo-project.

---
## Week 05
### 1. Working with `vars.json` files

#### 1.1. Analize the given file.

The file contain some lists, each in one row, and may contain, zero or more the info of some bus routes, and its variations.

**Importain properties:**
- `RouteId`: the id of the bus route
- `RouteVarId`: the id of route variations

These properties give us a clear understand how the data is organized in `vars.json` file.

**The code for the first requirement**
<!-- A simple class -->
```python
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

```