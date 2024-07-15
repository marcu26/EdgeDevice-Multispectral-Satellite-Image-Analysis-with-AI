import numpy as np
import rasterio
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import base64
from io import BytesIO
import os
from GetCoordinates import get_geographic_coordinates
from ApiClient import send_to_api

def process_and_send_image_from_folder(folder_path, api_url):
    image_file = None
    npy_file = None

    # Identify image and npy files
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.tiff') or file_name.endswith('.tif'):
            image_file = os.path.join(folder_path, file_name)
        elif file_name.endswith('.npy'):
            npy_file = os.path.join(folder_path, file_name)

    if not image_file or not npy_file:
        print(f"Lipsesc fișierele necesare din directorul {folder_path}.")
        return

    # Load and preprocess the image
    with rasterio.open(image_file) as src:
        img = src.read()
        img = img / 10000

    # Load argmax_channels
    argmax_channels = np.load(npy_file)

    # Define colors and classes for visualization
    colors = ['turquoise', 'yellow', 'green', 'red']
    classes = ['clear', 'thick cloud', 'thin cloud', 'cloud shadow']
    cmap = ListedColormap(colors)

    # Read RGB bands for visualization
    rgb_bands = [4, 3, 2]
    with rasterio.open(image_file) as src:
        img2 = src.read(rgb_bands)
        img2 = np.moveaxis(img2, 0, -1)
        img2 = img2 / 10000

    # Convert RGB image to base64
    buffer = BytesIO()
    plt.imshow(img2)
    plt.axis('off')
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    buffer.seek(0)
    base64_image_rgb = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Create overlay image
    buffer = BytesIO()
    plt.imshow(img2)
    plt.imshow(argmax_channels, cmap=cmap, interpolation='none', alpha=0.3)
    plt.axis('off')
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    buffer.seek(0)
    base64_overlay_rgb = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Convert mask to base64
    buffer = BytesIO()
    plt.imsave(buffer, argmax_channels, cmap=cmap)
    buffer.seek(0)
    base64_mask = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Calculate cloud percentage
    total_pixels = argmax_channels.size
    cloud_pixels = np.count_nonzero((argmax_channels == 1) | (argmax_channels == 3))
    cloud_percentage = (cloud_pixels / total_pixels) * 100

    # Extract coordinates using the function from the coordinates_extraction.py script
    coordinates = get_geographic_coordinates(image_file)
    latitude = coordinates['centroid']['lat']
    longitude = coordinates['centroid']['lon']

    # Read the Sentinel-2 image and encode it in base64
    with open(image_file, 'rb') as f:
        img_bytes = f.read()
        base64_image_sentinel2 = base64.b64encode(img_bytes).decode('utf-8')

    # Prepare payload
    payload = {
        "base64ImageRGB": base64_image_rgb,
        "base64OverlayRGB": base64_overlay_rgb,
        "base64ImageSentinel2": base64_image_sentinel2,
        "base64Mask": base64_mask,
        "unusablePercentage": cloud_percentage,
        "longitude": longitude,
        "latitude": latitude
    }

    # Send the payload to the API
    send_to_api(api_url, payload)
