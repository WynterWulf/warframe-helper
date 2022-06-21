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
    factor = 2
    x = 917 * factor
    y = 50 * factor
    currentState.screenshot = currentState.screenshot.resize((x,y))
    currentState.screenshot= currentState.screenshot.filter(ImageFilter.FIND_EDGES)
    
    currentState.screenshot.save("relicScreenshotTemp.png")


    currentState.screenStr = pytesseract.image_to_string(currentState.screenshot)

    #Filter: help fix grammar, improve number of items recognised
   
    currentState.screenStr = re.sub("[^A-Za-z]"," ",currentState.screenStr)
    currentState.screenStr = currentState.screenStr.lower()

    
    isTrue = any(x in currentState.screenStr for x in fissureRewards_matches)
    if isTrue:
        currentState.screenState ="Rewards screen"
    else:
        currentState.screenState = "None"

def similar(a,b):
    #print(SequenceMatcher(None, a, b).ratio())
    return SequenceMatcher(None, a, b).ratio()




#create starting variables

fissureRewardsnoParts_list = []
fissureVaulted_list = []
def loadPrimes():
    for x in warframeitemlib.archgun[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace("prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.archmelee[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace("prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.archwing[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.melee[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.primary[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.secondary[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.sentinels[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.sentinelweapons[0]:
        test = x['name']
        if "Prime " in test:
            test = test.lower()
            test = test.replace(" prime ","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)
        elif "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)

    for x in warframeitemlib.warframes[0]:
        test = x['name']
        if "Prime" in test:
            test = test.lower()
            test = test.replace(" prime","")
            test = re.sub("[^A-Za-z]"," ",test)
            if 'vaulted' in x.keys():
                fissureVaulted_list.append(test)
            fissureRewardsnoParts_list.append(test)


loadPrimes()

parts = [
        "forma", "blueprint",
        "systems","neuroptics","chassis",
        "receiver","barrel","stock",
        "grip","lower","limb","string","upper",
        "blade","link","handle","head","cerebrum","carapace",
        "gauntlet","receiver","pouch","stars","disc","band","buckle",
        "boot","harness","wings","hilt","ornament","chain",
]


fissureRewards_list = (fissureRewardsnoParts_list + parts)

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
    
    imageWidth, imageHeight = self.screenshot.size
    print(rewardCount)
    if rewardCount % 2 == 0:
        wid = imageWidth / 2
        imgL = self.screenshot.crop((0,0,wid,imageHeight))
        imgR = self.screenshot.crop((wid,0,imageWidth,imageHeight))
        if rewardCount == 4:
            wid2 = wid / 2
            imgL1 = imgL.crop((0,0,wid2,imageHeight))
            imgL2 = imgL.crop((wid2,0,wid,imageHeight))
            imgR1 = imgR.crop((0,0,wid2,imageHeight))
            imgR2 = imgR.crop((wid2,0,wid,imageHeight))
            imgL1Str = pytesseract.image_to_string(imgL1)
            imgL2Str = pytesseract.image_to_string(imgL2)
            imgR1Str = pytesseract.image_to_string(imgR1)
            imgR2Str = pytesseract.image_to_string(imgR2)
            # imgL1.show()
            # imgL2.show()
            # imgR1.show()
            # imgR2.show()
            rewardListTemp[0].string = imgL1Str.lower()
            rewardListTemp[1].string = imgL2Str.lower()
            rewardListTemp[2].string = imgR1Str.lower()
            rewardListTemp[3].string = imgR2Str.lower()
        else:
            imgLStr = pytesseract.image_to_string(imgL)
            imgRStr = pytesseract.image_to_string(imgR)
            rewardListTemp[0].string = imgLStr.lower()
            rewardListTemp[1].string = imgRStr.lower()
    elif rewardCount == 3:
        wid4 = imageWidth / 4
        wid3 = 3 * wid4
        offset = (imageWidth - wid3) / 2
        img1 = currentState.screenshot.crop((offset,0,(offset+wid4),imageHeight))
        img2 = currentState.screenshot.crop(((offset + wid4),0,(offset + (2 * wid4)),imageHeight))
        img3 = currentState.screenshot.crop(((offset + (2 * wid4)),0,imageWidth,imageHeight))
        img1Str = pytesseract.image_to_string(img1)
        img2Str = pytesseract.image_to_string(img2)
        img3Str = pytesseract.image_to_string(img3)
        rewardListTemp[0].string = img1Str.lower()
        rewardListTemp[1].string = img2Str.lower()
        rewardListTemp[2].string = img3Str.lower()
    else:
        print("rewardCount error")

    #check lowered string against vaulted list

    replaceList = [] + parts
    replaceList.append("prime")
    replaceList.remove("forma")


    replaceListPart = [] + fissureRewardsnoParts_list
    for x in parts:
        isTrue = x in replaceListPart
        if isTrue:
            replaceListPart = replaceListPart.remove(x)
    replaceListPart.append("prime")
    
    

    for i in rewardListTemp:
        string = re.sub("[^A-Za-z]"," ",i.string)
        string = string.split()
        matchingWords = []
        lenString = len(list(string))
        lenRewards = len(fissureRewards_list)
        k = 0
        while k < lenString:
            j = 0
            while j < lenRewards:
                rewardArray = fissureRewards_list[j].split()
                lenReward = len(rewardArray)
                l = 0
                while l < lenReward:
                    result = similar(string[k],rewardArray[l])
                    if  result > 0.8:
                        string[k] = rewardArray[l]
                        matchingWords.append(string[k])
                    l = l + 1
                j = j + 1
            k = k + 1
        replaceListLen = len(replaceList)
        replaceListPartLen = len(replaceListPart)
        m = 0
        matchingWordsPart = [] + matchingWords
        while m < replaceListLen:
            if replaceList[m] in matchingWords:
                matchingWords.remove(replaceList[m])
            if replaceList[m] in matchingWords:
                matchingWords.remove(replaceList[m])
            m = m + 1
        n = 0

        while n < replaceListPartLen:
            if replaceListPart[n] in matchingWordsPart:
                matchingWordsPart.remove(replaceListPart[n])
            if replaceListPart[n] in matchingWordsPart:
                matchingWordsPart.remove(replaceListPart[n])
            n = n + 1
        
        i.name = ' '.join(matchingWords)
        if matchingWordsPart[0] == "forma":
            matchingWordsPart.remove("forma")
        i.part = ' '.join(matchingWordsPart)

        a = 0
        for a in fissureVaulted_list:
            if i.name == a:
                i.isVaulted = True

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
    self.string = ""
    self.isVaulted = False
        


screenshot = pyautogui.screenshot(region=(476,222,971,243))
rewardList = []
currentState = state("None", screenshot, "",[], rewardList)
fissureRewards_matches = ["prime","blueprint","systems","neuroptics","chassis","rewards"]
always = 1


while currentState.screenState == "None":
    screenCheck()
    
    print(currentState.screenState)
    time.sleep(0.1) #END

while currentState.screenState == "Rewards screen":
    screenCheck()
    #currentState.screenshot.show()
    
    currentState.screenWords=currentState.screenStr.split()
    #print(currentState.screenStr)
    #print(currentState.screenWords)
    currentState.spellCheck()

    currentState.createRewardList()
    
    
    

    print(currentState.screenState)
    for x in currentState.rewardList:
        print(x.name + " " + x.part,end=" ")
        if x.isVaulted:
            print("is Vaulted")
        else:
            print(" ")

    time.sleep(15) #END

    #test