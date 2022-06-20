import pyautogui
from PIL import *
from PIL import ImageFilter
from PIL import ImageEnhance
import time
import keyboard
import cv2
import numpy as np
#create starting variables
scale = 300
warframe_speed = 1.4

time.sleep(5) #Added to give time to click into game

keyboard.press('w')

if scale == 100:
    screenshot1 = pyautogui.screenshot(region=(28,26,231,142))
elif scale == 300:
    screenshot1 = pyautogui.screenshot(region=(41,32,678-41,426-32))
    
screenshot1.save("sc1.png")

time.sleep(0.1)

keyboard.release('w')

if scale == 100:
    screenshot2 = pyautogui.screenshot(region=(28,26,231,142))
elif scale == 300:
    screenshot2 = pyautogui.screenshot(region=(41,32,678-41,426-32))
    
screenshot2.save("sc2.png")

#screenshot 1

screenshot_edges1 = screenshot1.filter(ImageFilter.FIND_EDGES)
screenshot_edges1.save("sc1e.png")

screenshot_clean1 = ImageEnhance.Brightness(screenshot_edges1).enhance(0.01)
screenshot_clean1 = ImageEnhance.Contrast(screenshot_clean1).enhance(100)
screenshot_clean1 = ImageEnhance.Sharpness(screenshot_clean1).enhance(10000)
screenshot_clean1.save("sc1c.png")

#screenshot 2

screenshot_edges2 = screenshot2.filter(ImageFilter.FIND_EDGES)
screenshot_edges2.save("sc2e.png")

screenshot_clean2 = ImageEnhance.Brightness(screenshot_edges2).enhance(0.01)
screenshot_clean2 = ImageEnhance.Contrast(screenshot_clean2).enhance(100)
screenshot_clean2 = ImageEnhance.Sharpness(screenshot_clean2).enhance(10000)
screenshot_clean2.save("sc2c.png")

black_pix = 100
black_arr = np.array([black_pix, black_pix, black_pix], dtype = "uint16")

sc1e_cv2 = cv2.imread("sc1e.png", flags=cv2.IMREAD_COLOR)

sc1e_cv2[np.where(sc1e_cv2<black_arr)] = [0]
cv2.imwrite("sc1test.png", sc1e_cv2)