import re

from selenium import webdriver

def vaulted_scraper():
    


    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    driver = webdriver.Chrome(executable_path=r"C:\Users\Tom\Desktop\code\chromedriver_win32\chromedriver.exe",options=option)

    globalVaulted = []
    globalUnvaulted = []

    def extractData(element,equipmentTypeName):
        rawText = element.text
        rawText = re.sub("[^A-Za-z,\n]"," ",rawText)
        names = rawText.split("\n")
        namesLen = len(names)
        i = 0
        vaulted = []
        
        unvaulted = []
        
        while i < namesLen:
            name = names[i]
            j = 0
            nameWords = name.split()
            nameWordsLen = len(nameWords)
            nameTitleLen = 0
            nameTitle = ""
            isVaulted = False
            while j < nameWordsLen:
                
                if nameWords[j] == "Prime":
                    nameTitleLen = j
                elif nameWords[j] == "V":
                    isVaulted = True
                j = j + 1
            if nameTitleLen == 1:
                nameTitle = nameWords[0]
            elif nameTitleLen == 2:
                nameTitle = nameWords[0] + " " + nameWords[1]
            elif nameTitleLen == 3:
                nameTitle = nameWords[0] + " "  + nameWords[1] + " "  + nameWords[2]
            if isVaulted:

                vaulted.append(nameTitle)
            else:
                unvaulted.append(nameTitle)
            i = i + 1
        globals()[equipmentTypeName] = equipmentType(vaulted,unvaulted)
        for i in vaulted:
            globalVaulted.append(i)
        for i in unvaulted:
            globalUnvaulted.append(i)
        print("hi")

    class equipmentType:
      def __init__(self,vaulted,unvaulted):
        self.vaulted = vaulted
        self.unvaulted = unvaulted



    names = []
    driver.get(r"https://warframe.fandom.com/wiki/Prime_Vault")

    warframe_element = driver.find_element_by_id("gallery-0")
    primary_element = driver.find_element_by_id("gallery-1")
    secondary_element = driver.find_element_by_id("gallery-2")
    melee_element = driver.find_element_by_id("gallery-3")
    archgun_element = driver.find_element_by_id("gallery-4")
    companion_element = driver.find_element_by_id("gallery-5")
    sentinelweapon_element = driver.find_element_by_id("gallery-6")
    archwing_element = driver.find_element_by_id("gallery-7")
    extractor_element = driver.find_element_by_id("gallery-8")
    Cosmetic_element = driver.find_element_by_id("gallery-9")

    extractData(warframe_element,"warframe")
    extractData(primary_element,"primary")
    extractData(secondary_element,"secondary")
    extractData(melee_element,"melee")
    extractData(archgun_element,"archgun")
    extractData(archwing_element,"archwing")

    with open(r"vaulted.txt","w") as fp:
        fp.truncate(0)
        for i in globalVaulted:
            fp.write("%s\n" % i)

    print("end")