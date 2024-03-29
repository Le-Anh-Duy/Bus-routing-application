import rtree
idx = rtree.Index()
# Define some sample data (replace with your actual objects)
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
