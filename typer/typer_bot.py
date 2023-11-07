import cv2
import mss
import pyautogui
import time
import pytesseract
from PIL import Image
time.sleep(4)
# with mss.mss() as sct:
#     left, top, right, bottom = 200, 420, 1250, 600
#     monitor = {"top": top, "left": left, "width": right-left, "height": bottom-top}
#     sct_img = sct.grab(monitor)

#     img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
img = pyautogui.screenshot(region=pyautogui.selectRegion())
print(img)
text = ''
text = pytesseract.image_to_string(img)
text = text.replace('\n', ' ')
text = text.replace('  ', ' ')
time.sleep(2)
print(text)
pyautogui.keyDown('shift')
pyautogui.press(text[0])
pyautogui.keyUp('shift')
pyautogui.write(text[1:])


"""
so they're finally here, performing for you. If you know the words, you can join in too. Put your hands together if you want to clap, as we take you through this monkey rap! 
"""