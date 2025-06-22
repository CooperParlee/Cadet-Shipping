import os
from PIL import Image
import pillow_heif
import time

pillow_heif.register_heif_opener()

ts = time.time()
count = 0

def convert_heic_to_png(root_dir, count):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".heic"):
                heic_path = os.path.join(root, file)
                png_path = os.path.join(root, os.path.splitext(file)[0] + ".png")
                
                try:
                    image = Image.open(heic_path)
                    
                    # ✅ Resize image if width > 500 pixels
                    max_width = 1024
                    if image.width > max_width:
                        ratio = max_width / image.width
                        new_height = int(image.height * ratio)
                        image = image.resize((max_width, new_height), Image.LANCZOS)

                    image.save(png_path, format="PNG")
                    print(f"Converted: {heic_path} → {png_path}")
                    count+=1
                except Exception as e:
                    print(f"Failed to convert {heic_path}: {e}")

    return count;

count = convert_heic_to_png("./Pictures", count)
count = convert_heic_to_png("./Main Report/Pictures", count)

print(f"Converted {count} images in: {time.time() - ts} seconds")
