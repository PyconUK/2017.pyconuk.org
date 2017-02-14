#!/usr/bin/python
"""Output some HTML to make my life easier."""
import os
from PIL import Image


directory = './sponsors'
content = """
<div style='width:%dpx;flex-grow:%d'>
    <i style='padding-bottom:%d%%'></i>
    <img src='%s' alt=''>
</div>"""

for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        im = Image.open(os.path.join(directory, filename))
        width, height = im.size
        a = width * 100 / height
        b = height / width * 100
        print(content % (a, a, b, 'static/sponsors/' + filename))
        continue
    else:
        continue
