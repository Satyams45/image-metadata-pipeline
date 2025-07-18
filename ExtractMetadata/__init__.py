import logging
import io
from PIL import Image

def main(input: dict) -> dict:
    image_data = input['data']
    image_name = input['name']
    
    with Image.open(io.BytesIO(image_data)) as img:
        width, height = img.size
        format = img.format

    size_kb = round(len(image_data) / 1024, 2)

    return {
        "name": image_name,
        "size_kb": size_kb,
        "width": width,
        "height": height,
        "format": format
    }