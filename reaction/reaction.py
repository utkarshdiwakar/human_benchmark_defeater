import mss
import pyautogui
from PIL import Image
import time

local_sleep = time.sleep
local_click = pyautogui.click

local_sleep(3)
target_color = bytearray(b'\xffU\x89c\xffU\x89c\xffU\x89c')
screen_size = pyautogui.size()
x = screen_size.width / 2
y = screen_size.height / 2
local_click(x, y)

ms = mss.mss()
monitor = ms.monitors[1]
center_x = monitor['width'] // 2
center_y = monitor['height'] // 2
bbox = (center_x, center_y, center_x + 1, center_y + 1)
count = 0

while True:
    if ms.grab(bbox).raw[:3:-1] == target_color:
        local_click()
        local_sleep(0.5)
        local_click()
