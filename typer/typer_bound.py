import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import pytesseract

screenshot = ImageGrab.grab()
gray_screenshot = screenshot.convert('L')


numpy_array = np.array(gray_screenshot)
thresholded_array = (numpy_array > 200).astype(np.uint8) * 255

contours, _ = cv2.findContours(thresholded_array, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if (x*y*w*h > 10):
        break
left, top, right, bottom = x, y, w, h
monitor = {"top": top, "left": left, "width": right-left, "height": bottom-top}
sct_img = sct.grab(monitor)
pyautogui.moveTo(x, y)
