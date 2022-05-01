import os
import random
import re
import time
import uuid
from requests import Session
from bs4 import BeautifulSoup




def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
cls()



divisor = 5
DIR = "temp"
session = Session()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}



print("\033[0;0m")



def save(url):
    res = session.get(url, headers=headers)
    name = str(uuid.uuid4().hex)
    with open('./' + DIR + '/' + name + '.png', 'wb') as f:
        for data in res.iter_content(chunk_size=8192):
            f.write(data)



def checkForDir(path):
    if not os.path.exists(path):
        os.mkdir(path)



checkForDir(DIR)
count = -1
file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print("\033[s", end="")
while True:
    count += 1
    print("\033[u", end="")
    print("In This Interface You Will See Almost All Stats\n")
    print("[+] How Often: " + str(count))
    print("[+] How Files: " + str(file))
    time.sleep(0.1)
    numberSites = ["1", "2", "3", "4"]
    introduction = random.choice(numberSites)



    if introduction == "1":
        allsite = []
        l = "https://skinsmc.org/"
        r = session.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^/skin/")}):
            allsite.append(link.get('href'))
            del allsite[divisor:]
        for urls in allsite:
            url = 'https://skinsmc.org' + urls
            res = session.get(url)
            html = BeautifulSoup(res.content, "html.parser")
            for download in html.findAll('a', attrs={'href': re.compile("^/textures/")}):
                uri = 'https://skinsmc.org' + download.get('href')
                save(uri)
                file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])



    if introduction == "2":
        allsite = []
        l = "https://mskins.net/en/skins/random"
        r = session.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('a', attrs={'class':'skin_link', 'href': re.compile("^https:")}):
            allsite.append(link.get('href'))
            del allsite[divisor:]
        for urls in allsite:
            skinname = urls.split("/")[-1]
            url = 'https://mskins.net/en/skin/' + skinname + '/download'
            save(url)
            file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
           
    

    if introduction == "3":
        for i in range(divisor):
            rands = random.randint(1, 1497791)
            url = "https://cdn2.nicemarkmc.com/skins/64x64/" + str(rands) + ".png"
            save(url)
            file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

           


    if introduction == "4":
        allsite = []
        links = []
        l = "https://www.minecraftiplist.com/skins/reshuffle/"
        r = session.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^/skinview/")}):
            allsite.append(link.get('href'))
            del allsite[divisor:]
        for urls in allsite:
            url = 'https://www.minecraftiplist.com' + urls
            res = session.get(url)
            html = BeautifulSoup(res.content, "html.parser")
            for png in html.findAll('a', attrs={'href': re.compile("^https://mctexture2")}):
                links.append(png.get('href'))
        for All in links:
            save(All)
            file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])



    if introduction == "5":
        allsite = []
        links = []
        l = 'https://mc-skins.com/'
        r = session.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^https:"), 'class':'_self cvplbd'}):
            allsite.append(link.get('href'))
            del allsite[divisor:]
        for urls in allsite:
            res = session.get(urls)
            html = BeautifulSoup(res.content, "html.parser")
            for png in html.findAll('div', attrs={'class':'nice-minecraft'}) or html.findAll('div', attrs={'class':'skin-previews-wrapper'}):
                a = png.decode_contents().strip()
                text = BeautifulSoup(a, "html.parser")
            for img in text.findAll('img'):
                links.append(img.get('src'))      
        for All in links:
            save(All)
            file = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
