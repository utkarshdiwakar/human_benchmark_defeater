import mss
from PIL import Image
import time
import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('num.png')
text = ''
for detection in result:
    text+=detection[1]

print(text)


