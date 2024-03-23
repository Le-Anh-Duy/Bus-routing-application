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