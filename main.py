import random
import requests
import re
import os
import time
from colorama import Fore, Style
from bs4 import BeautifulSoup
from datetime import timedelta, datetime


green_color = "\033[1;93m"

def close():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


close()

os.system("python update.py")

start = input(green_color + """ 

  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ▄████▄   ██▀███   ▄▄▄        █████▒▄▄▄█████▓
 ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██   ▒ ▓  ██▒ ▓▒
 ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒████ ░ ▒ ▓██░ ▒░
 ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▒  ░ ░ ▓██▓ ░
 ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒░▒█░      ▒██▒ ░
 ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░      ▒ ░░
 ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░ ░          ░
                           
   ██████  ██ ▄█▀ ██▓ ███▄    █
 ▒██    ▒  ██▄█▒ ▓██▒ ██ ▀█   █
 ░ ▓██▄   ▓███▄░ ▒██▒▓██  ▀█ ██▒
   ▒   ██▒▓██ █▄ ░██░▓██▒  ▐▌██▒
 ▒██████▒▒▒██▒ █▄░██░▒██░   ▓██░
 ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒

\t[developer] - WHITE71wolf


(1) - (Beta) minecraft.novaskin.me   (4) - (Beta) skinsmc.org    
(2) - (Beta) mskins.net              (5) - Exit
(3) - (Beta) nicemarkmc.com
> """)




if start == "1" or start == "2" or start == "3" or start == "4":
    if not os.path.exists('image'):
        os.mkdir('image')
    else:    
        pass

DIR = "image"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}

# download and save skin 
def save(url, file=None):
    res = requests.get(url, headers=headers)
    if not file:
        if res.headers.get('content-disposition'):
            d = res.headers.get('content-disposition')
            fname = str(re.findall("filename=(.+)", d)[0]).replace('"','')
            with open(f'./image/{fname}', 'wb') as file:
                for data in res.iter_content(chunk_size=8192):
                    file.write(data)
    else:
        with open(f'./image/{file}.png', 'wb') as file:
            for data in res.iter_content(chunk_size=8192):
                file.write(data)




if start == "1":
    close()
    count = int(input(Style.NORMAL + Fore.RESET + "Enter Count: "))
    close()
    from_date = datetime.today()
    while True:
        url_content = "https://minecraft.novaskin.me/gallery/random/"
        res = requests.get(url_content)
        html = BeautifulSoup(res.text, "lxml")
        s = html.find('a', {'class':'hovercard visible-xs-block'})['href']
        data_id = s.split('/')[-1]
        url = f'https://minecraft.novaskin.me/skin/{data_id}/download'
        save(url, file=data_id)
        from_date = from_date + timedelta(seconds=1)
        print(from_date.strftime(f'[%H:%M:%S] [INFO]: Done ./image/{data_id}.png'))
        file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if file == count:
            exit()



if start == "2":
    close()
    count = int(input(Style.NORMAL + Fore.RESET + "Enter Count: "))
    close()
    from_date = datetime.today()
    while True:
        url = "https://mskins.net/en/skins/random"
        response = requests.get(url)
        html = BeautifulSoup(response.text, "html.parser")
        p = html.find_all('a')
        skin_id = str(p[39]['href']).split("/")[-1]
        save(f"https://mskins.net/en/skin/{skin_id}/download")
        from_date = from_date + timedelta(seconds=1)
        print(from_date.strftime(f'[%H:%M:%S] [INFO]: Done ./image/{skin_id}.png'))
        file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if file == count:
            exit()





if start == "3":
    close()
    count = int(input(Style.NORMAL + Fore.RESET + "Enter Count: "))
    close()
    from_date = datetime.today()
    while True:
        rands = random.randint(1, 1497791)
        url = "https://cdn2.nicemarkmc.com/skins/64x64/" + str(rands) + ".png"
        res = requests.get(url)
        if res.status_code == 200:
            save(url, file=str(rands))
            from_date = from_date + timedelta(seconds=1)
            print(from_date.strftime(f'[%H:%M:%S] [INFO]: Done ./image/{str(rands)}.png'))
            file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
            if file == count:
                exit()




if start == "4":
    close()
    count = int(input(Style.NORMAL + Fore.RESET + "Enter Count: "))
    close()
    from_date = datetime.today()
    while True:
        url = "https://skinsmc.org/"
        response = requests.get(url)
        html = BeautifulSoup(response.text, "html.parser")
        p = html.find_all('img')
        skin_two = str(p[6]['src']).replace('/skinrender/','')[:2]
        skin_name = str(p[6]['src']).replace('/skinrender/','')
        save(url="https://skinsmc.org/textures/"+skin_two+"/"+skin_name, file=skin_name.replace('.png',''))
        from_date = from_date + timedelta(seconds=1)
        print(from_date.strftime(f'[%H:%M:%S] [INFO]: Done ./image/{skin_name}'))
        file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if file == count:
            exit()


if start == "5":
    close()
    exit()