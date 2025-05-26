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
if not os.path.exists(output):
    os.makedirs(output)

files = os.listdir(source)

jpg_files = filter(lambda file: os.path.splitext(file)[1] == '.jpg', files)

for file in jpg_files:
    print(f'Converting {file} to PNG format...')

# loop through Pokedex,
# convert images to png
# save to the new
