'''
This script converts JPG images to PNG format.
Usage: python jpg_to_png_converter.py <input_directory> <output_directory>
'''

import sys
import os
from PIL import Image

try:
    source = sys.argv[1]
    output = sys.argv[2]
except IndexError:
    print("Usage: python jpg_to_png_converter.py <input_directory> <output_directory>")
    sys.exit(1)

if not os.path.exists(source):
    print("Input directory does not exist.")
    sys.exit(1)

os.makedirs(output, exist_ok=True)

files = os.listdir(source)
jpg_files = filter(lambda file: os.path.splitext(file)[1].lower() == '.jpg', files)

for file in jpg_files:
    f, e = os.path.splitext(file)
    outfile = f + ".png"
    print(f'Converting {file} to PNG format...')
    try:
        with Image.open(os.path.join(source, file)) as im:
            im.save(os.path.join(output, outfile), 'PNG')
    except OSError as err:
        print(f"Cannot convert {err}")

print("Conversion completed.")
