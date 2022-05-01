import os
import shutil
from os.path import basename
from pathlib import Path
from zipfile import ZipFile
import uuid



# This is Color's
green = "\033[0;32m"
reset = "\033[0;0m"
white = "\033[0;37m"
red = "\033[0;31m"
boldred = "\033[1;31m"
boldwhite = "\033[1;37m"
boldgreen = "\033[1;32m"



class Pack:
    def __init__(self, name, file, bodyType):
        self.name = name
        self.file = file
        self.bodyType = bodyType



def checkForDir(path):
    if not os.path.exists(path):
        os.mkdir(path)



def createSkins(skinFiles, packName):
    skins = []
    for i in skinFiles:
        print("\n\tCurrent Skin:", i)
        file = i
        filename = Path(i)
        name = "skin." + packName + "." + filename.stem.replace("_","")
        bodyValue = int(input(green + "Please body type (0 for Steve and 1 for Alex/Slim): " + white))
        bodyType = convertBodyValue(bodyValue)
        skins.append(Pack(name, file, bodyType))
    return skins



def convertBodyValue(bodyValue):
    if (bodyValue == 1):
        bodyType = "geometry.humanoid.customSlim"
    else:
        bodyType = "geometry.humanoid.custom"
    return bodyType



def copySkins(skinsArr):
    for obj in skinsArr:
        shutil.copy("./temp/" + obj.file, "./Temp/" + obj.file, follow_symlinks=True)



def spaceAndTooLower(name):
    name = name.lower()
    return name



def generateManifest(packName, uuidA, version, uuidB):
    manifest_file = open("./Temp/manifest.json", 'w+')
    temp = "{\n\t\"format_version\": 1,\n\t\"header\": {\n\t\t\"name\": \"" + \
           packName + "\",\n\t\t\"uuid\": \"" + uuidA + \
           "\",\n\t\t\"version\": [\n\t\t\t" + \
           str(version[0]) + ",\n\t\t\t" + \
           str(version[1]) + ",\n\t\t\t" + \
           str(version[2]) + "\n\t\t]" + \
           "\n\t},\n\t\"modules\": [\n\t\t{\n\t\t\t\"type\": \"skin_pack\"," \
           "\n\t\t\t\"uuid\": \"" + uuidB + "\",\n\t\t\t\"version\": [" \
                                            "\n\t\t\t\t6,\n\t\t\t\t" + \
           "0,\n\t\t\t\t" + \
           "0\n\t\t\t]\n\t\t}\n\t]\n}"
    manifest_file.write(temp)
    manifest_file.close



def generatePackManifest(uuidA, packName, version, description, uuidB):
    pack_manifest_file = open("./Temp/pack_manifest.json", 'w+')
    temp = "{\n\t\"header\": {\n\t\t\"pack_id\": \"" + uuidA + "\",\n\t\t\"name\": \"" + packName + "\",\n\t\t\"packs_version\": \"" + str(
        version[0]) + \
           "." + str(version[1]) + "." + str(version[
                                                 2]) + "\",\n\t\t\"description\": \"" + description + "\",\n\t\t\"modules\": [\n\t\t\t{\n\t\t\t  \"description\": \""
    temp = temp + description + "\",\n\t\t\t  \"version\": \"6.0.0\",\n\t\t\t  \"uuid\": \"" + uuidB + "\",\n\t\t\t  \"type\": \"skin_pack\"\n\t\t\t}\n\t\t]\n\t}\n}"
    pack_manifest_file.write(temp)
    pack_manifest_file.close



def generateSkins(skinsArr, packName, creatorID):
    skins_file = open("./Temp/skins.json", 'w+')
    temp = "{\n\t\"geometry\": \"skinpacks/skins.json\",\n\t\"skins\": ["
    for obj in skinsArr:
        name = spaceAndTooLower(obj.name)
        bodyType = obj.bodyType
        file = obj.file
        temp = temp + "\n\t\t{\n\t\t\t\"localization_name\": \"" + name + "\",\n\t\t\t\"geometry\": \"" + str(
            bodyType) + \
               "\",\n\t\t\t\"texture\": \"" + str(file) + "\",\n\t\t\t\"type\": \"free\"\n\t\t},"
    temp = temp[:-1]
    temp = temp + "\n\n\t],\n\t\"serialize_name\": \"" + packName + "\",\n\t\"localization_name\": \"" + creatorID + "\"\n}"
    skins_file.write(temp)
    skins_file.close



def generateLangs(creatorID, skinsArr, lang_id, packName):
    langs_file = open("./Temp/texts/" + lang_id + ".lang", 'w+')
    temp = ""
    for obj in skinsArr:
        name = spaceAndTooLower(obj.name)
        temp = temp + "skin." + creatorID + "." + name + "=" + obj.name + "\n"
    temp = temp + "skinpack." + creatorID + "=" + packName
    langs_file.write(temp)
    langs_file.close



def makeMCPACK(packName, skinsArr, lang_id):
    with ZipFile(packName + ".mcpack", 'w') as zipObj:
        for obj in skinsArr:
            filePath = "./Temp/" + obj.file
            zipObj.write(filePath, basename(filePath))
        zipObj.write("./Temp/manifest.json", basename("./Temp/manifest.json"))
        zipObj.write("./Temp/pack_manifest.json", basename("./Temp/pack_manifest.json"))
        zipObj.write("./Temp/skins.json", basename("./Temp/skins.json"))
        zipObj.write("./Temp/texts", basename("./Temp/texts"))
        zipObj.write("./Temp/texts/" + lang_id + ".lang", "texts/" + lang_id + ".lang")
    zipObj.close()



def getUUID(id_value):
    result = uuid.uuid4()
    print("\nGenereated: UUID", id_value, ": ", result, end='')
    return str(result)



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



lang_id = "en_US"  
version = [2, 0, 0]  
uuidA = ""
uuidB = ""
creator = ""
creatorID = ""
packName = ""
description = ""
numberOfSkins = 0  



cls()



checkForDir("temp")
checkForDir("Temp")
checkForDir("./Temp/texts")



numberOfSkins = 0
for file in os.listdir("temp"):
    if file.endswith(".png"):
        numberOfSkins += 1

if (numberOfSkins <= 0):
    print(boldred + "ERROR: " + red + "No Skins Found in Skins Folder..." + reset)
else:
    print(boldgreen + "\t\t\t   Skins in the \"temp\" folder will be used.".upper() + reset)
    print(boldgreen + "\t\t\t\t  Number of Skins:".upper() + white + reset, numberOfSkins)
    skinFiles = os.listdir("temp")
    creator = input(green + "\nPlease Your Name: " + white)
    packName = input(green + "Please Your Pack's Name: " + white)
    description = input(green + "Please Your Pack's Description: " + white)
    print("Trying to Get Uuid From the Internet...")
    try:
        uuidA = getUUID(1)
        uuidB = getUUID(2)
        print("\nSuccess!")
    except:
        print("ERROR: Failed to Get Uuid From the Internet... ")
        print("ERROR: Recommended Uuid Generator: https://www.uuidgenerator.net/version4")
        uuidA = input(green + "Please Your First Uuid: " + white)
        uuidB = input(green + "Please Your Second Uuid: " + white)
    skinsArr = createSkins(skinFiles, packName)

    print("\n\tSkin Data")
    for obj in skinsArr:
        print("Name:", obj.name, "- File:", obj.file, "- Body Type:", obj.bodyType, sep=' ')

    creatorID = (creator + uuidA[len(uuidA) - 4:])
    copySkins(skinsArr)
    print("\n\nCopied Skins to Pack.")
    generateManifest(packName, uuidA, version, uuidB)
    print("Created manifest.json.")
    generatePackManifest(uuidA, packName, version, description, uuidB)
    print("Created pack_manifest.json.")
    generateSkins(skinsArr, packName, creatorID)
    print("Created skins.json.")
    generateLangs(creatorID, skinsArr, lang_id, packName)
    print("Created " + lang_id + ".lang")
    makeMCPACK(packName, skinsArr, lang_id)
    print("Packed Into .mcpack File")
    shutil.rmtree("./Temp")
    print("\n\tDONE!")
