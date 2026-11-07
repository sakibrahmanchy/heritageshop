from rembg import remove
from PIL import Image
import os

input_dir = "/workspace/patina-video/assets"
output_dir = "/workspace/patina-video/assets_nobg"

os.makedirs(output_dir, exist_ok=True)

images_to_process = [
    "04580472-7538-4b64-8fb0-863859e9b14a.jpg",
    "f6eeac79-e2c9-4f9e-a923-112bb5960ab2.jpg", 
    "de427794-15cd-4721-8a10-e8896ffcf3a7.jpg",
    "16f82807-3343-441d-9e66-48e3c11dfdf1.jpg",
    "999d33ac-695d-4fe7-8904-96adc5778ad5.jpg",
    "556522ec-9893-482c-b2de-0d4d0b6a1575.jpg",
    "aca18ca6-7df1-4ed1-acd9-25573c4158d2.jpg",
]

for img_name in images_to_process:
    input_path = os.path.join(input_dir, img_name)
    output_name = img_name.replace('.jpg', '.png')
    output_path = os.path.join(output_dir, output_name)
    
    print(f"Processing: {img_name}")
    
    with open(input_path, 'rb') as inp:
        input_data = inp.read()
    
    output_data = remove(input_data)
    
    with open(output_path, 'wb') as out:
        out.write(output_data)
    
    print(f"  Saved: {output_name}")

print("\nDone! All backgrounds removed.")
