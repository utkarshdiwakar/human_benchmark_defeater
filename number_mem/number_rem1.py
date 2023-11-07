import pytesseract
import cv2
from PIL import Image, ImageOps

def shrink_image(input_path, factor):
    with Image.open(input_path) as img:
        width, height = img.size
        new_width = int(width / factor)
        new_height = int(height / factor)
        smaller_img = img.resize((new_width, new_height), Image.LANCZOS)
        grayscale_image = ImageOps.grayscale(smaller_img)
        # threshold_value = 4  # Adjust this value as needed
        # thresholded_image = ImageOps.autocontrast(grayscale_image, cutoff=threshold_value)
        threshold = 80
        image = grayscale_image.point( lambda p: 255 if p > threshold else 0 )
        image_file = image.convert('1')
        return image_file

input_path = 'download.jpeg'
shrink_factor = 1
# shrink_image(input_path, shrink_factor).show()
img = shrink_image(input_path, shrink_factor)
img.save("anpr_result2.jpeg")
# img = Image.open("anpr_result.jpeg")

text = pytesseract.image_to_string(img)
print(text)