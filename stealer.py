import uuid
import time
import requests
import json
import os
try:
    from bs4 import BeautifulSoup
    from yachalk import chalk
except ImportError:
    os.system("sudo pip3 install bs4")
    os.system("sudo pip3 install yachalk")

name = str(uuid.uuid4().hex) + '.png'

def close():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def checkForDir(path):
    if not os.path.exists(path):
        os.mkdir(path)



def save(url):
    res = requests.get(url)
    with open(f'{name}', 'wb') as f:
        for data in res.iter_content(chunk_size=8192):
            f.write(data)


close()
print(chalk.green.bold("""
                      ████     ████                        
                     ░██░██   ██░██                  █████   
                     ░██░░██ ██ ░██  █████   ██████ ██░░░██
                     ░██ ░░███  ░██ ██░░░██ ██░░░░ ░██  ░██
                     ░██  ░░█   ░██░██  ░░ ░░█████ ░░██████
                     ░██   ░    ░██░██   ██ ░░░░░██ ░░░░░██
                     ░██        ░██░░█████  ██████   █████ 
                     ░░         ░░  ░░░░░  ░░░░░░   ░░░░░  
"""))
checkForDir('Skins')
username = input("Now you must enter the name of the player (Mojang) : ")
print('Loading, please wait a few seconds...')
time.sleep(2)
response = requests.get('https://api.mojang.com/users/profiles/minecraft/' + username)
print("Ensure that the player's name is present...")
time.sleep(1.40)
try:
    responsejson = json.loads(response.content)
except json.decoder.JSONDecodeError:
    print(chalk.red('\nERROR: Name not found'))
    exit()
print("Player name already exists!")
time.sleep(0.10)
uuidminecraft = responsejson["id"]
img = 'https://crafatar.com/skins/' + uuidminecraft
save(img)
print('Download completed! ')
print(f"You will find the file in '{os.path.abspath(name)}'")
