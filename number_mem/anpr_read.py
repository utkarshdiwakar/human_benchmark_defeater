import pytesseract
from PIL import Image, ImageOps


import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('screenshot.png')
# print(result)
for detection in result:
    print(detection[1])


# input_path = "Screenshot 2023-10-11 at 11.53.48 PM.png"
# img = Image.open(input_path)
# # img.show()
# text = pytesseract.image_to_string(img)
# print(text)

"""

1. Image of NumberPlate must be extracted (YOLO must create bounding box and coordinates - extracted) 
2. ESRGAN - Upscaling software
3. OCR - Pytesseract - if low accuracy, then finetuning.
4. Software to find details [done]

"""