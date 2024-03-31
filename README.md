
<font face='Cambria'>

---

<center>
<br>
<br>
<br>
<h1 style="font-size:80px">Technical report</h1>
<h6 style="font-size:20px">Programming Technique - Lab section</h6>
<br>
<br>
<br>
<center><img src="./report_pictures/logo.png" height="200">
</center>

<div class='parent'>
  <div class='child'>
    <h5>Title:  </h5>
    <h5>Author:  </h5>
    <h5>Student ID:   </h5>
    <h5>Class:  </h5>
  </div>
  <div class='child2'>

  </div>
  <div class='child'>
    <h5>Report for Solo Project</h5>
    <h5>Lê Anh Duy</h5>
    <h5>23127011</h5>
    <h5>23CLC03</h5>
  </div>
</div>

<style>
.parent {
  margin: 20px;
  /* padding: 2rem 2rem; */
  text-align: center;
}

.child {
  display: inline-block;
  vertical-align: middle;
  text-align: left
}


.child2 {
  display: inline-block;
  vertical-align: middle;
  text-align: left;
  padding: 20px
}

</style>

</center>



<style>
#mydiv {
  margin: auto;
  width: 50%;
  padding: 10px;
}
</style>

---


<div style="page-break-after: always"></div>

---

## <center><h3>Table of contents</h3></center>

- [Table of contents](#table-of-contents)
- [Abstract](#abstract)
- [Project structure](#project-structure)
  - [1. File management.](#1-file-management)
  - [2. Class diagram.](#2-class-diagram)
    - [2.1. Query classes.](#21-query-classes)
    - [2.2. Data classes.](#22-data-classes)
- [Week 05](#week-05)
  - [1. Prepare the parent class.](#1-prepare-the-parent-class)
    - [1.1. Analize the given requirements.](#11-analize-the-given-requirements)
    - [1.2. Inspecting the code `query.py`.](#12-inspecting-the-code-querypy)
      - [1.2.1. `push` and `load` functions.](#121-push-and-load-functions)
      - [1.2.2. `searchBy(seft, atts, messageCond, className)` functions.](#122-searchbyseft-atts-messagecond-classname-functions)
      - [1.2.3. `outputAsCSV` and `outputAsJSON`.](#123-outputascsv-and-outputasjson)
  - [2. Working with `vars.json` file.](#2-working-with-varsjson-file)
    - [2.1. Analize the given file.](#21-analize-the-given-file)
    - [2.2. Build the `RouteVar` class.](#22-build-the-routevar-class)
    - [2.3. Build the `RouteVarQuery` class.](#23-build-the-routevarquery-class)
  - [3. Working with `stops.json` file.](#3-working-with-stopsjson-file)
    - [3.1. Build the `stop` class.](#31-build-the-stop-class)
    - [3.2. Build the stop `stopQuerry` class.](#32-build-the-stop-stopquerry-class)
    - [3.3. Two additional classes.](#33-two-additional-classes)
- [Week 06](#week-06)
  - [1. Using `pyproj` to convert a (lat, lng) to (x, y).](#1-using-pyproj-to-convert-a-lat-lng-to-x-y)
  - [2. Research bout `geojson.io`.](#2-research-bout-geojsonio)
    - [2.1. `.geojson` format.](#21-geojson-format)
  - [3. `Path` and `PathQuery` classes.](#3-path-and-pathquery-classes)
    - [3.1. `Path` class.](#31-path-class)
    - [3.2. `PathQuery` class.](#32-pathquery-class)
  - [4.  Research about `shapely` library in python.](#4--research-about-shapely-library-in-python)
    - [4.1. Overview](#41-overview)
    - [4.2. Usefull functions](#42-usefull-functions)
  - [5. Research about `rtree` library in python.](#5-research-about-rtree-library-in-python)
    - [5.1. Overview.](#51-overview)
    - [5.2. Usefull functions.](#52-usefull-functions)
    - [5.3. Using Rtree with shapely.](#53-using-rtree-with-shapely)
  - [6. Using large language models.](#6-using-large-language-models)
    - [6.1. Overview.](#61-overview)
    - [6.2. Using the model to prompting.](#62-using-the-model-to-prompting)
    - [6.3. Apply to the app.](#63-apply-to-the-app)
- [References](#references)

<div style="page-break-after: always"></div>

---
## <center><h3>Abstract</h3></center>
This report details the development of a **bus management system**, the solo porject for *KTLT-lab* section, using **Python**. The system incorporates a unique feature: integration with a language model for enhanced bus stop and route search capabilities, reflecting the growing trend of AI utilization.

**Structure of the report:** The report is divided into weekly sections, outlining the tasks accomplished during each development phases. It's important to note that features may evolve between versions, so the report contents might slightly differ between versions.

**User manual:** The current application uses a user-friendly console interface for interaction, relying on keyboard input for navigation.

<center><img src="./report_pictures/image-2.png" height="200"></center>


While core functionalities are operational, the application is currently in development. This means some feature might be litmite So please type correctly when using options *[2], [3], [4]* and the options *[1]* can be used when the internet is connected only.


**Using options [1]:**

This option lets users experience the integrated language model to enhance the searching functionalyties.

<center><img src="./report_pictures/image-3.png" height="200"></center>


Users just need to type in the message, which may vary from personal conditions, to specific infomation of the stops. After receiving the requirements, the program makes some 'API' call to get the responds.

<!-- ![Respond img](./report_pictures/image-4.png) -->
<center><img src="./report_pictures/image-4.png" height="200"></center>

After it completed analizing the message, for the purpose of showcasing the search function works, we will see a console message that tell us what the program is searching for.

Finally, the user can name the output file and choose the desired format (typically saved within the "output" folder). This allows for customization and easy access to search results.

**Using option [2]:**

In case the first option isn't working, users can try manualy searching with this second options. Which will require using keyboard to input, and navigate throught each attributes that they want to search.

This option will first requires user to specify the searching objects.

<!-- ![alt text](./report_pictures/image-5.png) -->
<center><img src="./report_pictures/image-4.png" height="200"></center>

After chosing the object, the interface provides options for users to specify various search criteria (which are attributes in the class).

<!-- ![alt text](./report_pictures/image-6.png) -->
<center><img src="./report_pictures/image-6.png" height="200"></center>


When finished chosing the attribute, user will have a sections where they can tell the program to search base on the condition, the conditions should be presented in format that *Python* can understand.

<!-- ![alt text](./report_pictures/image-7.png) -->
<center><img src="./report_pictures/image-7.png"></center>


After filled out all the search paramenters, users can now name their files and chose the desired output format.

![alt text](./report_pictures/image-8.png)
<!-- <center><img src="./report_pictures/image-8.png" height="200"> -->

When the search is completed, the system displays relevant search results based on the chosen criteria.

**Using option [3]:**

This option is use as a testing tool of the program. When running it gives you the extracted data of 'stop', 'routeVar' or 'path'.

<!-- ![alt text](./report_pictures/image-9.png) -->
<center><img src="./report_pictures/image-9.png" heigh="200px"></center>

There is nothing to special, users just need type in and it will give them the file of extracted datas.

![alt text](./report_pictures/image-10.png)

**Using option [4]:**

This options will showcases the functionalites of tasks of week 06 sections. Which is required to visualize bus routes and and generating GeoJSON files.

It is a "one-click-run" option, where, when the '4' is selected, it will run.

![alt text](./report_pictures/image-11.png)

After it complete running, users will get the following files.

![alt text](./report_pictures/image-12.png)

The `map_with_lines.html` file can be opended in any browser, and display a full map with path, lineString(s), Point(s).

![alt text](./report_pictures/image-14.png)

The `map.geojson` should have data of 'GeoJSON' objects so users can use it to plot on [geojson.io](geojson.io).

<!-- ![alt text](./report_pictures/image-15.png) -->
<center><img src="./report_pictures/image-15.png" height="300"></center>


<div style="page-break-after: always"></div>

---
## <center><h3>Project structure</h3></center>

Move on the technical sections. This sections give us an overview how files and data are stored and managed.

### 1. File management.

<!-- ![alt text](./report_pictures/image-16.png) -->
<center><img src="./report_pictures/image-16.png" height="300"></center>

- The **data** folder is where the data is stored, like `path.json`, `vars.json`, `stops.json`.
- The **logs** folder is where all the logs, messages are writen.
- The **output** folder is where all the files that being created by the program are stored.
- The **src** folder is where all the source files are store. And there are three folders **\_\_pycache\_\_, conditions_modules, sub_modules**:
  -  **\_\_pycache\_\_**: Stores **bytecode files** (`.pyc` files) containing the compiled version of your Python modules.
  -  **conditions_modules:** As the message user might gets really complicated (like, "find me route that passes stops 1, 2, 3...") and requires external functions to evaluate (which would be further implement).
  - **sub_modules**: This is where most of the functionalities are implemented in separate Python files.

- The **main.py** and other .py files, are used to test the programe.
- The **.env** file is use to store secret datas.

### 2. Class diagram.
#### 2.1. Query classes.

With further explaination will come at later sections. Due to the query classes share some method that are identical, so they will all inherit from one parent class

<!-- ![alt text](./report_pictures/image-17.png) -->
<center><img src="./report_pictures/image-17.png" height="400"></center>

#### 2.2. Data classes.
**Route var class**
<!-- ![alt text](./report_pictures/image-18.png) -->
<center><img src="./report_pictures/image-18.png" height="400"></center>

**Path class**
<!-- ![alt text](./report_pictures/image-19.png) -->
<center><img src="./report_pictures/image-19.png" height="400"></center>

**Stop class**
Because the [`stops.json`](./data/stops.json) don't give us the stops directly. becuase the stops are inside a list of stop attached to the route variations. So to have a more organized structure and to reserse the intentions of the data, the `RouteOfStop` class is necessary.

<!-- ![alt text](./report_pictures/image-20.png) -->
<center><img src="./report_pictures/image-20.png" height="400"></center>

<div style="page-break-after: always"></div>

---
## <center><h3>Week 05</h3></center>


### 1. Prepare the parent class.
#### 1.1. Analize the given requirements.

We will examine the `RouteVarQuery` and `StopQuery` classes. They share some methods.

To avoid code redundancy, we will create a parent class named `query`. Then, both `RouteVarQuery` and `StopQuery` can inherit from `Query` and only implement functions specific to their objects.


#### 1.2. Inspecting the code [`query.py`](./src/sub_modules/query.py).
The code should look like this. It will act like a data structure that manage the data being put in it.

```python
import json
import csv
class query:
    # _list should be a list of objects
    def __init__(self, logger):
        self._list = []
        self.logger = logger # add logger to easier see the info

    def push(self, element): #insert sigle element
        #detail is in the code
        pass

    def load(self, elements): # insert a list to query
        #detail is in the code
        pass
```
```python
    def searchBy(self, atts, messageCond, className): #list att
        def cond(a, conditions):
            #detail of this functions is in the code
        #detail is in the code
        pass

    def outputAsCSV(self, _datas, dest, fields):
        #detail is in the code
        pass

    def outputAsJSON(self, _datas, dest):
        #detail is in the code
        pass
```

##### 1.2.1. `push` and `load` functions.
Because the class will be uses to manage a list of objects, so these functions will let users append new elements into our structure.

##### 1.2.2. `searchBy(seft, atts, messageCond, className)` functions.

We are required to search by prompting, so I think it is best to make the condition to be customizable.

Due to the data set is not so big, linear search might be just enough. And the `cond(a, conditions)` will be a function that can evaluate the a string conditions.

My plan is to use some LLM to process the prompting and extract the conditions and the attributes for me then I would process that result base on the desires of user want to find by locations, times, ect....

For example: By runing the following script will give us a list, and some log messages.
```python
searchBy(["_runningTime", "_distance"], "a[0] < 100 and a[1] < 50000", "routeVar")
```
*output:*
![alt text](./report_pictures/image-1.png)

##### 1.2.3. `outputAsCSV` and `outputAsJSON`.
These functions are uses to output the desired format for user.

### 2. Working with [`vars.json`](./data/vars.json) file.
#### 2.1. Analize the given file.

The `vars.json` is used to store route infomation. The data

**Importain properties:**
- `RouteId`: the id of the bus route
- `RouteVarId`: the id of route variations

These properties give us a clear understand how the data is organized in `vars.json` file. The data structure consists of lists, where each list represents a bus route and potentially contains multiple variations of that route.

#### 2.2. Build the `RouteVar` class.

A simple class with every properties of a route variation.

To avoid accidentally modify any of the properties, every properties will be protected. So they will only be accessed through/modified a getter/setter function (those functions will be implemented in the code, but for the readability of this report, I will not include).

*The code is in [`route_var.py`](./src/sub_modules/route_var.py):*
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
```

#### 2.3. Build the `RouteVarQuery` class.

As planed above, this class will inherit from the `query` class above for some of the functionalities. Due to the differences from the layout of each file, the `extract` function need to be implemented separately.

*The code is in [`route_var_query.py`](./src/sub_modules/route_var_query.py)*
```python
from query import query
from route_var import RouteVar
import json
import csv

class RouteVarQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        tmp = []
        with open(dest, "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)
                for d in data: # d is a dict
                    value_of_field = []
                    for v in d:
                        value_of_field.append(d[v])
                    print(value_of_field)

                tmp.append(RouteVar(value_of_field))
        self._list = tmp
```

### 3. Working with [`stops.json`](./data/stops.json) file.

This file contains a series of stops on each line, these stopd will represent the path that buses take, they belong to some route variations. So in each line, there are the `routeId` and `routeVarId` attached to the list of stops.

To extract the stops, we need to extract the stops from the stop list of each route variations. Therefore, some of the stop, which are belong to multiple routes, will be duplicated and I will handle that situation in the later part of this sections.

#### 3.1. Build the `stop` class.

First we need to build the `stop` class, which is used to manage the basic infomation of a bus stop.

*The code is in [`stop.py`](./src/sub_modules/stop.py)*
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

#### 3.2. Build the stop `stopQuerry` class.

This class will have the same functionalities with the above class, but with a custom extracter to extract data and `remove_duplicate` functions to remove duplicate.

*The code is in [`stop_query.py`](./src/sub_modules/stop_query.py)*
```python
class StopQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        # Detail implementation are in the file

    def remove_duplicate(self):
        # Detail implementation are in the file
```

#### 3.3. Two additional classes.

To get the most out of the `stops.json` file, we need to have way to manage the stops along the route variations. So I made two more classes.

The first one is to manage stops along the route, and the second one is to query each route.
```python
class RouteOfStop():
    def __init__(self, stops, RouteId, RouteVarId):
        self._stops = stops
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId
```

```python

class RouteOfStopQuery(query):
    def __init__(self):
        super().__init__()

    def extract(self, dest):
        # detail implementation is in the stop_query file.
```

<div style="page-break-after: always"></div>

----
## <center><h3>Week 06</h3></center>

### 1. Using `pyproj` to convert a (lat, lng) to (x, y).
When working on a Geograhic Coordinate Systems, especially working on a small area, and need the data that you calculate to be as precise and effectively as possible, you might need to convert (lat, lng) coordinate to (x, y) coordinate using some converting standard.

The given data was given in (lat, lng) standard and can be ploted onto `geojson.io`, which is currently in $\texttt{WGS84}$ standard (that represent the Earth as a sphere). Therefore, using (lat, lng) to perform distance or other calculation will take a lot of effort and invole many trigonometry functions, which will dramatically decrease the performance of our programe.

So, we need first convert $\texttt{WGS84}$ to $\texttt{EPSG: 3405}$, which is Vietnamese standard projection system, that projected (lat, lng) coordinate of a sphere to the coordinate of a plane (x, y).

```python
from pyproj import Transformer
# Input CRS (geographic coordinates)
input_crs = "EPSG:4326"
# Output CRS (projected coordinate system for Vietnam)
output_crs = "EPSG:3405"  # VN-2000 / UTM zone 48N

class converter:
    def __init__(self):
        self.transformer = Transformer.from_crs(input_crs, output_crs)
    def convert(self, latitude, longitude):
        x, y = self.transformer.transform(latitude, longitude)
        return x, y
```

For the simplycity and the reuseability of the code, the converter will be put in a class and serve as a module.

### 2. Research bout `geojson.io`.
[geojson.io](htpp://geojson.io/) is a quick, simple tool for creating, viewing, and sharing spatial data. This website uses `.geojson` format to plot the data onto it.

#### 2.1. `.geojson` format.
GeoJSON is a format for encoding a variety of geographic data structures. And this format is not so hard.
```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
```

GeoJSON supports the following geometry types: Point, LineString, Polygon, MultiPoint, MultiLineString, and MultiPolygon. Geometric objects with additional properties are Feature objects. Sets of features are contained by FeatureCollection objects.

- The additional properties could be any of the user define properties.
- The coordinate reference system for all GeoJSON coordinates is a geographic coordinate reference system, using the World Geodetic System 1984 (WGS 84) [WGS84] datum, with longitude and latitude units of decimal degrees.
- The coordinate object can be a pair of coordinates, or a list of coordinates to represent different type of shape in geojson.
    - `Point`, need a pair of coordinate
    - `LineString`, need a list of the pair of two coordinate to represent the starting point and ending point of a string
    - `Polygon`, for a polygon with `n` vertices to be ploted, we need a list of `n + 1` point that are arranged in clockwise/counter clockwise order, with the first and the last point are the same.

- Note: the coordinate should be lng/lat in geojson

### 3. `Path` and `PathQuery` classes.
#### 3.1. `Path` class.

A path will have a list of lat/lng coordinate (Most of them are not the `STOP`) which are use to indicate the the shape of path.

```python
class path:
    def __init__(self, data):
        lat, lng, RouteId, RouteVarId = data
        self._lat = lat
        self._lng = lng
        self._RouteId = RouteId
        self._RouteVarId = RouteVarId
    # detail implementation are in the code
```
#### 3.2. `PathQuery` class.

This query class is almost the same as the previouse twos, also inherits from  `query` parent class for its functions. Like the twos above, we also need to make a custom `extract` method for this class.

```python
from path import path
from query import query
import json

class path_query(query):
    def __init__(self):
        super().__init__()

    def extract(self):
        with open("../../data/paths.json", "r", encoding="utf8") as file:
            for line in file:
                data = json.loads(line)
                self.push(path([data["lat"], data["lng"], data["RouteId"], data["RouteVarId"]]))
# Path: src/query.py
            file.close()
```

### 4.  Research about `shapely` library in python.
#### 4.1. Overview

`shapely` is a python library for working with geometric objects in two-dimensional space. It is usally used to create, maniplulate, and analize geometric objects like points, lines, polygons.... Also, `shaply` provide us a user-friendly interface for geometric data. Therefore, it is ideal to choose `shapely` for tasks involving spatial data analysis, like:
- Finding areas and perimeters.
- Checking for geometric relationships, (intersection, containment,...).
- Performing spatial operation, (buffering, offset, ...).

#### 4.2. Usefull functions

- `object.area`: Returns the area (`float`) of the object.

- `object.bounds`: Returns a `(minx, miny, maxx, maxy)` tuple (float values) that bounds the object.

- `object.length`: Returns the length (`float`) of the object.

- `object.distance(other)`: Returns the minimum distance (`float`) to the other geometric object.
- `object.hausdorff_distance(other)`: Returns the Hausdorff distance (`float`) to the other geometric object. The Hausdorff distance between two geometries is the furthest distance that a point on either geometry can be from the nearest point to it on the other geometry.

- `object.intersection(other)`: Returns a collection of every type of intersected object.

- `object.interpolate(distance[, normalized=False])`: Return a point at the specified distance along a linear geometric object. The distance will be calculated from the starting point, *go along* with the line string (the linestring will act like a paht):
    - If the destinated point lies on the LineString, it is the length of the begining point to that point.
    - If the destinated point does not lie on the LineString, it is the length of the beginning point to a point on the linestring, such that, the point is the first closest point from the begining.
```python
from shapely import Point, LineString
ip = Point(0.5, 0.5)
line = LineString([(0, 0), (1, 0), (1, 1), (0, 1)])
dist = line.project(ip)  # dist is now 0.5 not 1.5 or 2.5
```
**Can be used to solve:** finding distance between stops.

- `object.intersection(other)` and `object.interpolate(distance[, normalized=False])` will be often use.

### 5. Research about `rtree` library in python.
#### 5.1. Overview.

`RTree` is a powerful spatial data management system, which provide us with efficently spatial queries (search for nearest point, etc...). Normally, `Rtree` will store data in form of *bounding box*, which is a box that are denoted by its upper-left and bottom-right corners.

Having `RTree` in this project, it will be used as a spatial database for `shapely` objects, and use it to find the nearest point from a set of points along the bus route to our current location/destination.

**Example:** storing and retrive data from rtree

```python
import rtree
idx = rtree.Index()
# Define some sample data
object1_bbox = (0, 0, 10, 10)
object2_bbox = (5, 5, 15, 15)

# Add objects to the index with unique IDs
idx.insert(1, object1_bbox)
idx.insert(22, object2_bbox)
# Define your query rectangle
query_bbox = (7, 7, 12, 12)

# Find objects intersecting the query rectangle
for item_id in idx.intersection(query_bbox):
    print(f"Found object {item_id}")
```

#### 5.2. Usefull functions.
- `Index()`: Creates an R-Tree index object to manage your spatial data.
- `insert(id, bbox)`: Inserts an object into the index with a unique identifier (id) and its bounding box (bbox) of the form as the bound of above shapely's `.bounds` function.
- `insert_many(iterable)`: Efficiently inserts multiple objects from an iterable (like a list) into the index.
- `intersection(bbox)`: Performs an intersection search, returning IDs of objects whose bounding boxes intersect with the specified query rectangle (bbox).
- `nearest(point, n=1)`: Finds the nearest n objects (default: 1) to a given query point. Returns a list of tuples containing (ID, distance).
- `delete(id, bbox=None)`: Removes an object from the index identified by its ID and optionally its bounding box (if available).
- `write(filename)` and `read(filename)`: Persist the R-Tree data to a file (filename) for later loading.

#### 5.3. Using Rtree with shapely.

Because rtree manages geometry objects as bounding boxes, so when we insert an `Shapyly` object to `rtree`, we need to insert its bounding.

```python
from rtree import Index
import rtree
import shapely.geometry as sg


# Define some Shapely geometries
point = sg.Point(10, 20)
line = sg.LineString([(5, 5), (15, 15)])
polygon = sg.Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])

# Create an R-Tree index
idx = Index()

# Add the geometries to the index
idx.insert(1, point.bounds, obj=point)
nearest_geometry = idx.nearest((10, 10, 20,     20), 1)
print(list(nearest_geometry))  # Find the nearest geometry to a points in a list of index
# Output: [1]
```

### 6. Using large language models.
#### 6.1. Overview.

To know which function is best suit to search for the user's messages, we will need a language model for understanding what users want to find.

After took a look at some common models's pricing, I choose the "Claude 3 - Haiku" model, here is the pricing.
<!-- ![alt text](./report_pictures/image.png) -->
<center><img src="./report_pictures/image.png" height="400"></center>

#### 6.2. Using the model to prompting.

To ensure privacy infomation won't be leaked out, sensitive information, like API key..., will be stored in a `.env` file and could only be access as a evironment variable.

```python
import anthropic
import dotenv
import os

dotenv.load_dotenv()
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(
    api_key=anthropic_api_key,
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only as short as possible.",
    messages=[
        {"role": "user", "content": "How are you today?"}
    ]
)

print(message.content)
```

**The respond:**
```json
[ContentBlock(text="I'm doing well.... How can I help you today?", type='text')]
```

#### 6.3. Apply to the app.

To simplify the management process, the promting functionality will be implemented as a class, see [`promting_bot.py`](./src/sub_modules/promting_bot.py) for detail.

The output tokens are way more expensive than the input tokens, the message we want to make should be as specific as possible so that the bot only outputs the necessary infomation.

```python
import anthropic
import dotenv
import os

class respondHandler():
    def __init__(self):
        self.stopData = "meta data" # real data is in the file
        self.routeVarData = "meta data" # real data is in the file
        self.pathData = "meta data" # real data is in the file

        dotenv.load_dotenv()
        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(
            api_key=anthropic_api_key,
        )

    def respond(self, messages):

        print(f"responding, please wait...")

        message = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.0,
            system = f"given the data [{self.pathData}, {self.routeVarData}, {self.stopData}], return the class, the list of attribute use in condition and condition string that python understand, each attribute in the condition should be 'a[i]', with 'i' is the index in the returned atrributes list, respond only in json format in one line.",
            messages=[
                {"role": "user", "content": messages},
            ]
        )

        print(f"responded!!")

        return message.content[0].text
```

The app will force the model to output in the below format, which is more convenient for using.
```json
{"class": "_className_", "attributes": ["at1", "at2", ...], "conditions": "_condition string_"}
```

<!-- ## Week 07

In this week's assignments I need to build graph, and doing a shortest path finding algorithm on this graph.

*Things to plan out:*
- Graph structure
- Graph logic, construction, considered point...

*To do:*
- Extract and build graph.
- plan to construct the graph, step by step -->

## References
* [Geographic 101 for dummies](https://8thlight.com/insights/geographic-coordinate-systems-101)
* [Using shapely](https://shapely.readthedocs.io/en/stable/manual.html#general-attributes-and-methods)
* [Anthropic Haiku Cookbook](https://docs.llamaindex.ai/en/latest/examples/cookbooks/anthropic_haiku/)
* [Learning Rtree](https://rtree.readthedocs.io/en/latest/)
* [Drawing Class Diargram](https://app.diagrams.net/)
</font>