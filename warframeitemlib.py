
import json
import io



# def screenCheck():
#     currentState.screenshot = pyautogui.screenshot(region=(478,411,971,50))
#     factor = 2
#     x = 917 * factor
#     y = 50 * factor
#     currentState.screenshot = currentState.screenshot.resize((x,y))
    
#     currentState.screenshot= currentState.screenshot.filter(ImageFilter.FIND_EDGES)
    
#     currentState.screenshot.save("relicScreenshotTemp.png")


#     currentState.screenStr = pytesseract.image_to_string(currentState.screenshot)

#     #Filter: help fix grammar, improve number of items recognised
   
#     currentState.screenStr = re.sub("[^A-Za-z]"," ",currentState.screenStr)
#     currentState.screenStr = currentState.screenStr.lower()

    
#     isTrue = any(x in currentState.screenStr for x in inventory_matches) or any(x in currentState.screenStr for x in inventory_matches)
#     if isTrue:
#     #if fissureRewards_matches in screenStr: DOESNT WORK
#         #print("TRUE")
#         currentState.screenState ="Inventory screen"
#     else:
#         currentState.screenState = "None"

# class state:
#   def __init__(self, screenState, screenshot, screenStr, screenWords, inventoryList):
    
#     self.screenState = screenState
#     self.screenshot = screenshot
#     self.screenStr = screenStr
#     self.screenWords = screenWords
#     self.inventoryList = inventoryList
#   def createInventoryList(self):
#     i = 0
#     rewardCount = 0
    
#     screenWords = self.screenWords
#     length = len(screenWords)
#     inventoryListTemp = []
    
#     while i < length:
#         #print(i)
        
#         # RECOGNISE PRIME PARTS AND FORMA

#         if(screenWords[i] == "prime"):
#             print(screenWords[i-1])
#             print(screenWords[i])
#             print(screenWords[i+1])
#             inventoryListTemp.append(item(screenWords[i-1],screenWords[i+1],inventoryCount))
#             inventoryCount = inventoryCount + 1
#         elif(screenWords[i] == "forma"):
#             print(screenWords[i])
#             print(screenWords[i+1])
#             inventoryListTemp.append(item(screenWords[i],"Blueprint",inventoryCount))
#             inventoryCount = inventoryCount + 1
#         i = i + 1
#     if self.inventoryList == []:
#         self.inventoryList = inventoryListTemp
#     else:
#         inventoryCount = len(self.inventoryList)
#         inventoryList = self.inventoryList
#         i = 0
#         while i < inventoryCount:
#             correct = 0
#             correctTemp = 0
#             if any(ext in inventoryList[i].name for ext in words):
#                 correct = correct + 1
#             if any(ext in inventoryList[i].part for ext in words):
#                 correct = correct + 1
#             if any(ext in inventoryListTemp[i].name for ext in words):
#                 correctTemp = correctTemp + 1
#             if any(ext in inventoryListTemp[i].part for ext in words):
#                 correctTemp = correctTemp + 1
#             if correctTemp > correct:
#                 inventoryList[i] = inventoryListTemp[i]
#             i = i + 1

# class item:
#   def __init__(self, name, part, ID):
#     self.name = name
#     self.part = part
#     self.ID = ID



allList = []

def allListAppend(dataType):
    allList.append([dataType])
    


arcanes = json.load(io.open(r"..\warframe\warframe-items\data\json\Arcanes.json",mode="r",encoding="utf-8"))
arch_gun = json.load(io.open(r"..\warframe\warframe-items\data\json\Arch-Gun.json",mode="r",encoding="utf-8"))
arch_melee = json.load(io.open(r"..\warframe\warframe-items\data\json\Arch-Melee.json",mode="r",encoding="utf-8"))
archwing = json.load(io.open(r"..\warframe\warframe-items\data\json\Archwing.json",mode="r",encoding="utf-8"))
fish = json.load(io.open(r"..\warframe\warframe-items\data\json\Fish.json",mode="r",encoding="utf-8"))
gear = json.load(io.open(r"..\warframe\warframe-items\data\json\Gear.json",mode="r",encoding="utf-8"))
glyphs = json.load(io.open(r"..\warframe\warframe-items\data\json\Glyphs.json",mode="r",encoding="utf-8"))
melee = json.load(io.open(r"..\warframe\warframe-items\data\json\Melee.json",mode="r",encoding="utf-8"))
mods = json.load(io.open(r"..\warframe\warframe-items\data\json\Mods.json",mode="r",encoding="utf-8"))
pets = json.load(io.open(r"..\warframe\warframe-items\data\json\Pets.json",mode="r",encoding="utf-8"))
primary = json.load(io.open(r"..\warframe\warframe-items\data\json\Primary.json",mode="r",encoding="utf-8"))
relics = json.load(io.open(r"..\warframe\warframe-items\data\json\Relics.json",mode="r",encoding="utf-8"))
resources = json.load(io.open(r"..\warframe\warframe-items\data\json\Resources.json",mode="r",encoding="utf-8"))
secondary = json.load(io.open(r"..\warframe\warframe-items\data\json\Secondary.json",mode="r",encoding="utf-8"))
sentinels = json.load(io.open(r"..\warframe\warframe-items\data\json\Sentinels.json",mode="r",encoding="utf-8"))
sentinelweapons = json.load(io.open(r"..\warframe\warframe-items\data\json\SentinelWeapons.json",mode="r",encoding="utf-8"))
sigils = json.load(io.open(r"..\warframe\warframe-items\data\json\Relics.json",mode="r",encoding="utf-8"))
skins = json.load(io.open(r"..\warframe\warframe-items\data\json\Relics.json",mode="r",encoding="utf-8"))
warframes = json.load(io.open(r"..\warframe\warframe-items\data\json\Relics.json",mode="r",encoding="utf-8"))

allListAppend(arcanes)
allListAppend(arch_gun)
allListAppend(arch_melee)
allListAppend(archwing)
allListAppend(fish)
allListAppend(gear)
allListAppend(glyphs)
allListAppend(melee)
allListAppend(mods)
allListAppend(pets)
allListAppend(primary)
allListAppend(relics)
allListAppend(resources)
allListAppend(secondary)
allListAppend(sentinels)
allListAppend(sentinelweapons)
allListAppend(sigils)
allListAppend(skins)
allListAppend(warframes)

print(len(allList))


print("test")