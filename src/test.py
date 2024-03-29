import json
import folium

def create_geojson(latitudes, longitudes, filename='map.geojson'):
    features = []  # Connect the last point to the first point
    for i in range(len(latitudes) - 1):
        j = (i + 1)
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [longitudes[i], latitudes[i]],
                    [longitudes[j], latitudes[j]]
                ]
            },
            "properties": {}
        }
        features.append(feature)

    feature_collection = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(filename, 'w') as f:
        json.dump(feature_collection, f)

def plot_on_map(latitudes, longitudes):
    map_center = [sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes)]
    my_map = folium.Map(location=map_center, zoom_start=5)

    # Plot markers for each point
    for lat, lon in zip(latitudes, longitudes):
        folium.Marker([lat, lon]).add_to(my_map)

    # Draw lines connecting each pair of points
    for i in range(len(latitudes)-1):
        line = folium.PolyLine(locations=[[latitudes[i], longitudes[i]], [latitudes[i+1], longitudes[i+1]]], color='blue')
        my_map.add_child(line)

    my_map.save('map_with_lines.html')

with open("../data/paths.json", "r") as file:
    for line in file:
        s = json.loads(line)

        latitudes = s["lat"]  # Example latitudes
        longitudes = s["lng"]  # Example longitudes

        create_geojson(latitudes, longitudes, filename='map.geojson')
        plot_on_map(latitudes, longitudes)
        break