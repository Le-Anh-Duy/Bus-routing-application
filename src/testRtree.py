from rtree import Index
import rtree
import shapely.geometry as sg


# Define some Shapely geometries
point = sg.Point(10, 20)
line = sg.LineString([(5, 5), (15, 15)])
polygon = sg.Polygon([(0, 0), (20, 0), (10, 10), (0, 10)])

idx = Index()

# Add the geometries to the index
idx.insert(1, point.bounds, obj=point)
nearest_geometry = idx.nearest((10, 10, 20, 20), 1)
print(list(nearest_geometry))  # Find the nearest geometry to a points in a list of index
# Output: [1]
