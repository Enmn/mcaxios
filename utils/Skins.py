import os
import random
import re
import time
import uuid
try:
    import requests
    from bs4 import BeautifulSoup
    from yachalk import chalk
except ImportError:
    os.system("pip3 install requests")
    os.system("pip3 install yachalk")
    os.system("pip3 install bs4")

def close():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
close()


# File settings and changes
divisor = 5
DIR = "temp"
session = requests.Session()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}



def save(url):
    res = session.get(url, headers=headers)
    name = str(uuid.uuid4().hex)
    with open(f'{DIR}/{name}' + '.png', 'wb') as f:
        for data in res.iter_content(chunk_size=8192):
            f.write(data)

def checkForDir(path):
    if not os.path.exists(path):
        os.mkdir(path)

while True:
    numberSites = ["1", "2", "3", "4"]
    introduction = random.choice(numberSites)
    if introduction == "1" or introduction == "2" or introduction == "3" or introduction == "4" or introduction == "5":
        checkForDir(DIR)



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
           
    

    if introduction == "3":
        for i in range(divisor):
            rands = random.randint(1, 1497791)
            url = "https://cdn2.nicemarkmc.com/skins/64x64/" + str(rands) + ".png"
            res = session.get(url)
            save(url)
           


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



    if introduction == "5":
        allsite = []
        links = []
        l = 'https://mc-skins.com/'
        r = session.get(l)
        soup = BeautifulSoup(r.content, "html.parser")
        for link in soup.findAll('a', attrs={'href': re.compile("^https:"), 'class':'_self cvplbd'}):
            allsite.append(link.get('href'))
            del allsite[5:]
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
