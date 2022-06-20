import pyautogui
from PIL import *
from PIL import ImageFilter
from PIL import ImageEnhance
import time
import keyboard
import cv2
import numpy as np
from PIL import Image
import pytesseract
import re
from difflib import SequenceMatcher
import pandas as pd
from os.path import exists
from vaulted_scraper import vaulted_scraper

# Global Vars
lines = []
currentTime = time.time()
daySeconds = 24 * 60 * 60

        
        


# Classes

class sceneContainer:
  def __init__(self,screenShot,state):
    self.screenShot = screenShot
    self.state = state

class profile:
  def __init__(self):
    self.firstOpened = 0
    self.lastOpened = 0
# -- Initialisation --

globalData = profile()

if exists('warframe_helper_temp.txt'):
    with open(r'warframe_helper_temp.txt') as file:
        lines = file.readlines()
        
        globalData.firstOpened = float(lines[0])
        globalData.lastOpened = float(lines[1])

        if currentTime > (daySeconds + globalData.lastOpened):
            vaulted_scraper()
    with open(r'warframe_helper_temp.txt','w') as file:
        file.truncate(0)
        file.write(str(globalData.firstOpened))
        file.write("\n")
        file.write(str(currentTime))
else:
    with open(r"warframe_helper_temp.txt","x") as file:
        file.write(str(currentTime))
        file.write("\n")
        file.write(str(currentTime))
        
        globalData.firstOpened = currentTime
        globalData.lastOpened = currentTime



warframeScreen = pyautogui.screenshot()

# -- General Loop --

interval = 0.1
on = 1
while on == 1:
    warframeScreen = pyautogui.screenshot()
    time.sleep(interval)