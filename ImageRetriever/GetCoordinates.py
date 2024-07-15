import rasterio
from rasterio.warp import transform
import numpy as np

def get_geographic_coordinates(image_path):
    with rasterio.open(image_path) as src:
        img = src.read(1)
        
        transform_affine = src.transform
        
        src_crs = src.crs
        
        width = src.width
        height = src.height
        
        corners = [(0, 0), (0, height), (width, 0), (width, height)]
        
        def pixel_to_geo(transform, x, y):
            lon, lat = transform * (x, y)
            return lon, lat
        
        geographic_coords = [pixel_to_geo(transform_affine, corner[0], corner[1]) for corner in corners]
        
        utm_coords = np.array(geographic_coords)
        utm_x = utm_coords[:, 0]
        utm_y = utm_coords[:, 1]

        lat_lon_coords = transform(src_crs, 'EPSG:4326', utm_x, utm_y)
        
        latitudes = lat_lon_coords[1]
        longitudes = lat_lon_coords[0]
        
        coordinates = {
            "corners": [{"lat": lat, "lon": lon} for lat, lon in zip(latitudes, longitudes)],
            "centroid": {
                "lat": np.mean(latitudes),
                "lon": np.mean(longitudes)
            }
        }
        
        return coordinates

if __name__ == "__main__":
    import sys
    image_path = sys.argv[1]
    coordinates = get_geographic_coordinates(image_path)
    print(coordinates)
