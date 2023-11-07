import mss
import pyautogui
import numpy as np
import cv2
import time
import numpy as np
time.sleep(5)
pyautogui.click(719,460)
sct = mss.mss()
left, top, right, bottom = 280, 250, 1200, 700
monitor = {"top": top, "left": left, "width": right-left, "height": bottom-top}
sct_img = sct.grab(monitor)
image_data = np.array(sct_img)
gray_image = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
_, thresholded_image = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)
y, x = np.where(thresholded_image == 255)
lst = list(zip(x,y))
pyautogui.click(lst[1000][0], lst[1000][1])
print(lst[1000][0], lst[1000][1])