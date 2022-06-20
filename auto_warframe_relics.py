from tkinter import Y
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
import warframeitemlib



def screenCheck():
    currentState.screenshot = pyautogui.screenshot(region=(478,411,971,50))
    currentStateRaw.screenshot = pyautogui.screenshot(region=(476,411,971,50))
    factor = 2
    x = 917 * factor
    y = 50 * factor
    currentState.screenshot = currentState.screenshot.resize((x,y))
    currentStateRaw.screenshot = currentStateRaw.screenshot.resize((x,y))
    
    currentState.screenshot= currentState.screenshot.filter(ImageFilter.FIND_EDGES)
    
    currentState.screenshot.save("relicScreenshotTemp.png")


    currentState.screenStr = pytesseract.image_to_string(currentState.screenshot)
    currentStateRaw.screenStr = pytesseract.image_to_string(currentStateRaw.screenshot)

    #Filter: help fix grammar, improve number of items recognised
   
    currentState.screenStr = re.sub("[^A-Za-z]"," ",currentState.screenStr)
    currentStateRaw.screenStr = re.sub("[^A-Za-z]"," ",currentStateRaw.screenStr)
    currentState.screenStr = currentState.screenStr.lower()
    currentStateRaw.screenStr = currentStateRaw.screenStr.lower()

    
    isTrue = any(x in currentState.screenStr for x in fissureRewards_matches) or any(x in currentStateRaw.screenStr for x in fissureRewards_matches)
    if isTrue:
    #if fissureRewards_matches in screenStr: DOESNT WORK
        #print("TRUE")
        currentState.screenState ="Rewards screen"
    else:
        currentState.screenState = "None"

def similar(a,b):
    print(SequenceMatcher(None, a, b).ratio())
    return SequenceMatcher(None, a, b).ratio()




#create starting variables

fissureRewards_list = []
def loadPrimes():
    for x in warframeitemlib.arch_gun:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)
    
    for x in warframeitemlib.arch_melee:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.archwing:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.melee:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.primary:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.secondary:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.sentinels:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.sentinelweapons:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)

    for x in warframeitemlib.warframes:
        test = x['name']
        if "Prime" in test:
            test = test.replace(" Prime","")
            test = test.lower()
            fissureRewards_list.append(test)


loadPrimes()

parts = [
        "blueprint", "forma"
        "systems","neuroptics","chassis",
        "receiver","barrel","stock",
        "grip","lower","limb","string","upper",
        "blade","link","handle","head","cerebrum","carapace",
        "gauntlet","receiver","pouch","stars","disc","band","buckle",
        "boot","harness","wings","hilt","ornament","chain",
]


fissureRewards_list.append(parts)

class state:
  def __init__(self, screenState, screenshot, screenStr, screenWords, rewardList):
    
    self.screenState = screenState
    self.screenshot = screenshot
    self.screenStr = screenStr
    self.screenWords = screenWords
    self.rewardList = rewardList
  def createRewardList(self):
    i = 0
    rewardCount = 0
    
    screenWords = self.screenWords
    length = len(screenWords)
    rewardListTemp = []
    
    while i < length:
        #print(i)
        
        if(screenWords[i] == "prime"):
            print(screenWords[i-1])
            print(screenWords[i])
            print(screenWords[i+1])
            rewardListTemp.append(reward(screenWords[i-1],screenWords[i+1],rewardCount))
            rewardCount = rewardCount + 1
        elif(screenWords[i] == "forma"):
            print(screenWords[i])
            print(screenWords[i+1])
            rewardListTemp.append(reward(screenWords[i],"blueprint",rewardCount))
            rewardCount = rewardCount + 1
        i = i + 1
    if self.rewardList == []:
        self.rewardList = rewardListTemp
    else:
        rewardCount = len(self.rewardList)
        rewardList = self.rewardList
        i = 0
        for i in rewardList:
            for y in fissureRewards_list:
                correct = 0
                correctTemp = 0
                if any(ext in i.name for ext in y):
                    correct = correct + 1
                if any(ext in i.name for ext in y):
                    correctTemp = correctTemp + 1
                if correctTemp > correct:
                    rewardList[i] = rewardListTemp[i]
                
            
    
  def spellCheck(self):

    screenWordsTemp = self.screenWords
    
    lengthScreenWords = len(screenWordsTemp)
    lengthWords = len(fissureRewards_list)
    i = 0
    
    while i < lengthScreenWords:
        j = 0
        while j < lengthWords:
            
            result = similar(screenWordsTemp[i],fissureRewards_list[j])
            #print("compared",words[j],"with",screenWordsTemp[i])
            if  result > 0.8:
                screenWordsTemp[i] = fissureRewards_list[j]
                print("replaced",fissureRewards_list[j],"with",screenWordsTemp[i])
            j = j + 1
        i = i + 1
    self.screenWords = screenWordsTemp
class reward:
  def __init__(self, name, part, number):
    self.name = name
    self.part = part
    self.number = number
        


screenshot = pyautogui.screenshot(region=(476,222,971,243))
rewardList = []
currentState = state("None", screenshot, "",[], rewardList)
currentStateRaw = state("None", screenshot, "",[], rewardList)
fissureRewards_matches = ["prime","blueprint","systems","neuroptics","chassis","rewards"]
always = 1


while currentState.screenState == "None":
    screenCheck()
    
    print(currentState.screenState)
    time.sleep(0.1) #END

while currentState.screenState == "Rewards screen":
    screenCheck()
    #currentState.screenshot.show()
    
    #print(pytesseract.image_to_string(Image.open('relicScreenshot1.png')))
    currentState.screenWords=currentState.screenStr.split()
    currentStateRaw.screenWords=currentStateRaw.screenStr.split()
    print(currentState.screenStr)
    print(currentState.screenWords)
    print(currentStateRaw.screenStr)
    print(currentStateRaw.screenWords)
    currentState.spellCheck()
    currentStateRaw.spellCheck()

    currentState.createRewardList()
    currentStateRaw.createRewardList()
    
    
    

    print(currentState.screenState)

    time.sleep(0.1) #END

    #test