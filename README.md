# solo-project

This will be my document of this solo-project.

---
## Week 05

### 0. Prepare some external modules before implementing the files.
#### 0.1. Analize the given requirements

Lets look at the `RouteVarQuery` and `StopQuery` classes, they have some method that are pretimuch the same as each other.

So before implement the two classes, I will make a class names `query` which will contain all the similar method of the twos. So when i implement the `RouteVarQuery` and `StopQuery` classes, i just need to inherit from the `query` class and add in some functions that are specified for each kind of object.




#### 0.2. Inspecting the code.
The code should look like this. It will act like a data structure that manage the data being put in it.

```python
import json
import csv
from route_var import RouteVar
from stop import Stop

class query:

    #_data should be a list of objects
    def __init__(self):
        self._list = []


    def push(self, element):
        self._list.append(element)

    def load(self, elements):
        for ele in elements:
            self._list.append(ele)

    def searchBy(self, att, cond):
        # cond - conditions - callback functions
        retList = []

        for element in self._list:
            if cond(element[att]):
                retList.append(element)

        return retList

    # _datas should be a list dictionary
    # fields is your list of headers
    def outputAsCSV(self, _datas, dest, fields):

        # print(fields)
        with open(dest, "w", newline="", encoding='utf8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in _datas:
                writer.writerow(row.__dict__)

        csvfile.close()

    def outputAsJSON(self, _datas, dest):
        with open(dest, "w", encoding="utf-8") as jsonfile:
            for obj in _datas:
                json.dump([obj.__dict__], jsonfile, ensure_ascii=False)
                jsonfile.write('\n')

        jsonfile.close()
```

##### 0.2.1. `push` and `load` functions.
These functions will let users append new elements into our structure.

##### 0.2.1. `searchBy` functions.

We are required to search by prompting, so I think it is best to make the condition to be customizable.

Due to the data set is not so big. Linear search might be just enough. And the `cond` will be a function that could be vary when executing.

```python
def searchBy(self, att, cond):
	# cond - conditions - callback functions
	retList = []

	for element in self._list:
		if cond(element[att]):
			retList.append(element)

	return retList
```


### 1. Working with `vars.json` file.
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
### 2. Working with `stop.json` file.
This file contains data of stops, and stop properties to work with.

**Those are:**
- `StopId`
- `Code`

#### 2.1. Build the `stop.class`.
```python
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
```
