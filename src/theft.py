import uuid
import time
import requests
import json
import base64
import os



# This is Color's
red = "\033[0;31m"
boldred = "\033[1;31m"
darkblue = "\033[1;30m"
underline = "\033[4m"
green = "\033[0;32m"
boldgreen = "\033[1;32m"
reset = "\033[0;0m"
white = "\033[0;37m"
boldwhite = "\033[1;37m"

name = str(uuid.uuid4().hex) + '.png'
session = requests.Session()

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def checkForDir(path):
    if not os.path.exists(path):
        os.mkdir(path)



def save(url):
    res = session.get(url)
    with open(f'./Skins/{name}', 'wb') as f:
        for data in res.iter_content(chunk_size=8192):
            f.write(data)


cls()
checkForDir('Skins')
username = input(green + f"Now You Must Enter The Name Of The Player ({white + 'Mojang' + green}): " + reset)
print(green + 'Loading, Please Wait a Few Seconds...')
time.sleep(2)
response = session.get('https://api.mojang.com/users/profiles/minecraft/' + username)
print("Ensure That The Player's Name is Present...")
time.sleep(1.40)
try:
    responsejson = json.loads(response.content)
except json.decoder.JSONDecodeError:
    print('\nERROR: Name Not Found' + reset)
    exit()
print("Player Name Already Exists!")
time.sleep(0.10)
uuidminecraft = responsejson["id"]
byte = session.get('https://sessionserver.mojang.com/session/minecraft/profile/' + uuidminecraft).json()['properties'][0]['value']
img = json.loads(base64.b64decode(byte))['textures']['SKIN']['url']
save(img)
print('Installation Completed')
print(f"You Will Find The File in {white + '{h}' + os.path.abspath('Skins/' + name)}'".format(h="'"))
