"""
This is the example of the request module which downloads the image
"""

import requests
from PIL import Image
from io import BytesIO

response_object = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Moon_and_Aurora.jpg/320px-Moon_and_Aurora.jpg')
print(response_object.status_code)
print(type(response_object.content))
image = Image.open(BytesIO(response_object.content))
print(type(image))
image.save('aurora.png')
Image.open('aurora.png')