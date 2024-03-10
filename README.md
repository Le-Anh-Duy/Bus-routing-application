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

#### 1.2. Build the `RouteVar` class.
**The code for the first requirement**
A simple class with every properties of a route variations.

Each variation need to have its `RouteId` to denote it is a variations of a route.

To avoid user can accidentally modify any of the properties, every properties will be protected. So they will only be access through a getter functions.
Here i will specify the data that user can access and data that only admin can access.
<!-- To avoid user -->
**Users:**
- `RouteNo`
- `RouteVarName`
- `RouteVarShortName`
- `StartStop`
- `EndStop`
- `RunningTime`
- `OutBound`

**Admin:**
- `RouteID`
- `RouteVarId`

```python

class RouteVar:
	def __init__(self, RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, OutBound, RunningTime):
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

	def __str__(self):
		return f"Route Variation ID: {self.routeVarId}, Route: {self.routeNo}, Start Stop: {self.startStop}, End Stop: {self.endStop}, Distance: {self.distance}, Outbound: {self.outbound}, Running Time: {self.runningTime}"


```

#### 1.3. Build the `RouteVarQuery` class.

The requirement is to build the search functions. These functions will let user search the route variations by their attributes, such that the attribute satisfies some constrains.

So I will build a search funtions for each of the properties.
**They are:**
- `searchByRouteID`
-
##### 1.3.1 Search by `RouteID`
##### 1.3.2 Build the `OutputAsCSV` method

```python
def outputAsCSV(sefl, _datas, dest, fields):
	print(fields)
	with open(dest, "w", newline="", encoding='utf8') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fields)
		writer.writeheader()
		for row in _datas:
			writer.writerow(row.__dict__)

	csvfile.close()
```

In the `RouteVarQuery` class, I built this method to output the csv format. Using the 'csv' library