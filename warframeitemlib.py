
import json
import requests
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




def pullDataTxt():
    allList = []
    fileArcanes = io.open(r"warframe-helper/arcanesLib.txt",mode="r",encoding="utf-8")
    arcanes.append(json.load(fileArcanes))

    fileArchgun = io.open(r"warframe-helper/archgunLib.txt",mode="r",encoding="utf-8")
    archgun.append(json.load(fileArchgun))

    fileArchmelee = io.open(r"warframe-helper/archmeleeLib.txt",mode="r",encoding="utf-8")
    archmelee.append(json.load(fileArchmelee))

    fileArchwing = io.open(r"warframe-helper/archwingLib.txt",mode="r",encoding="utf-8")
    archwing.append(json.load(fileArchwing))

    fileFish = io.open(r"warframe-helper/fishLib.txt",mode="r",encoding="utf-8")
    fish.append(json.load(fileFish))

    fileGear = io.open(r"warframe-helper/gearLib.txt",mode="r",encoding="utf-8")
    gear.append(json.load(fileGear))

    fileGlyphs = io.open(r"warframe-helper/glpyhsLib.txt",mode="r",encoding="utf-8")
    glyphs.append(json.load(fileGlyphs))

    fileMelee = io.open(r"warframe-helper/meleeLib.txt",mode="r",encoding="utf-8")
    melee.append(json.load(fileMelee))

    fileMods = io.open(r"warframe-helper/modsLib.txt",mode="r",encoding="utf-8")
    mods.append(json.load(fileMods))

    filePets = io.open(r"warframe-helper/petsLib.txt",mode="r",encoding="utf-8")
    pets.append(json.load(filePets))

    filePrimary = io.open(r"warframe-helper/primaryLib.txt",mode="r",encoding="utf-8")
    primary.append(json.load(filePrimary))

    fileRelics = io.open(r"warframe-helper/relicsLib.txt",mode="r",encoding="utf-8")
    relics.append(json.load(fileRelics))

    fileResources = io.open(r"warframe-helper/resourcesLib.txt",mode="r",encoding="utf-8")
    resources.append(json.load(fileResources))

    fileSecondary = io.open(r"warframe-helper/secondaryLib.txt",mode="r",encoding="utf-8")
    secondary.append(json.load(fileSecondary))

    fileSentinels = io.open(r"warframe-helper/sentinelsLib.txt",mode="r",encoding="utf-8")
    sentinels.append(json.load(fileSentinels))

    fileSentinelWeapons = io.open(r"warframe-helper/sentinelWeaponsLib.txt",mode="r",encoding="utf-8")
    sentinelweapons.append(json.load(fileSentinelWeapons))

    fileSigils = io.open(r"warframe-helper/sigilsLib.txt",mode="r",encoding="utf-8")
    sigils.append(json.load(fileSigils))

    fileSkins = io.open(r"warframe-helper/skinsLib.txt",mode="r",encoding="utf-8")
    skins.append(json.load(fileSkins))

    fileWarframes = io.open(r"warframe-helper/warframesLib.txt",mode="r",encoding="utf-8")
    warframes.append(json.load(fileWarframes))

def pullDataApi():
    allList = []

    def allListAppend(dataType):
        allList.append([dataType])
        


    arcanes = json.loads(requests.get('https://api.warframestat.us/items/search/arcanes?by=category').text)
    archgun = json.loads(requests.get('https://api.warframestat.us/items/search/arch-gun?by=category').text)
    archmelee = json.loads(requests.get('https://api.warframestat.us/items/search/arch-melee?by=category').text)
    archwing = json.loads(requests.get('https://api.warframestat.us/items/search/archwing?by=category').text)
    fish = json.loads(requests.get('https://api.warframestat.us/items/search/fish?by=category').text)
    gear = json.loads(requests.get('https://api.warframestat.us/items/search/gear?by=category').text)
    glyphs = json.loads(requests.get('https://api.warframestat.us/items/search/glyphs?by=category').text)
    melee = json.loads(requests.get('https://api.warframestat.us/items/search/melee?by=category').text)
    mods = json.loads(requests.get('https://api.warframestat.us/items/search/mods?by=category').text)
    pets = json.loads(requests.get('https://api.warframestat.us/items/search/pets?by=category').text)
    primary = json.loads(requests.get('https://api.warframestat.us/items/search/primary?by=category').text)
    relics = json.loads(requests.get('https://api.warframestat.us/items/search/relics?by=category').text)
    resources = json.loads(requests.get('https://api.warframestat.us/items/search/resources?by=category').text)
    secondary = json.loads(requests.get('https://api.warframestat.us/items/search/secondary?by=category').text)
    sentinels = json.loads(requests.get('https://api.warframestat.us/items/search/sentinels?by=category').text)
    sentinelweapons = json.loads(requests.get('https://api.warframestat.us/items/search/sentinelweapons?by=category').text)
    sigils = json.loads(requests.get('https://api.warframestat.us/items/search/sigils?by=category').text)
    skins = json.loads(requests.get('https://api.warframestat.us/items/search/skins?by=category').text)
    warframes = json.loads(requests.get('https://api.warframestat.us/items/search/warframes?by=category').text)

    allListAppend(arcanes)
    allListAppend(archgun)
    allListAppend(archmelee)
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

    fileArcanes = open("warframe-helper/arcanesLib.txt","w")
    json.dump(arcanes,fileArcanes)

    fileArchgun = open("warframe-helper/archgunLib.txt","w")
    json.dump(archgun,fileArchgun)

    fileArchmelee = open("warframe-helper/archmeleeLib.txt","w")
    json.dump(archmelee,fileArchmelee)

    fileArchwing = open("warframe-helper/archwingLib.txt","w")
    json.dump(archwing,fileArchwing)

    fileFish = open("warframe-helper/fishLib.txt","w")
    json.dump(fish,fileFish)

    fileGear = open("warframe-helper/gearLib.txt","w")
    json.dump(gear,fileGear)

    fileGlyphs = open("warframe-helper/glpyhsLib.txt","w")
    json.dump(glyphs,fileGlyphs)

    fileMelee = open("warframe-helper/meleeLib.txt","w")
    json.dump(melee,fileMelee)

    fileMods = open("warframe-helper/modsLib.txt","w")
    json.dump(mods,fileMods)

    filePets = open("warframe-helper/petsLib.txt","w")
    json.dump(pets,filePets)

    filePrimary = open("warframe-helper/primaryLib.txt","w")
    json.dump(primary,filePrimary)

    fileRelics = open("warframe-helper/relicsLib.txt","w")
    json.dump(relics,fileRelics)

    fileResources = open("warframe-helper/resourcesLib.txt","w")
    json.dump(resources,fileResources)

    fileSecondary = open("warframe-helper/secondaryLib.txt","w")
    json.dump(secondary,fileSecondary)

    fileSentinels = open("warframe-helper/sentinelsLib.txt","w")
    json.dump(sentinels,fileSentinels)

    fileSentinelWeapons = open("warframe-helper/sentinelWeaponsLib.txt","w")
    json.dump(sentinelweapons,fileSentinelWeapons)

    fileSigils = open("warframe-helper/sigilsLib.txt","w")
    json.dump(sigils,fileSigils)

    fileSkins = open("warframe-helper/skinsLib.txt","w")
    json.dump(skins,fileSkins)

    fileWarframes = open("warframe-helper/warframesLib.txt","w")
    json.dump(warframes,fileWarframes)
            


    print("test")

arcanes =[]
archgun =[]
archmelee =[]
archwing =[]
fish =[]
gear =[]
glyphs =[]
melee =[]
mods =[]
pets =[]
primary =[]
relics =[]
resources =[]
secondary =[]
sentinels =[]
sentinelweapons =[]
sigils =[]
skins =[]
warframes =[]

pullDataTxt()

print("test")