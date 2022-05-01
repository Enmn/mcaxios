import os
import platform
from notify import update
try:
    from pathlib import Path
    from PIL import Image
    from bs4 import BeautifulSoup
    import requests
except ImportError:
    if platform.system() == "Linux":
        os.system('pip3 install pillow')
        os.system('pip3 install bs4')
        os.system('pip3 install requests')
        os.system('pip3 install pathlib')
    if platform.system() == "Windows":
        os.system('pip install pillow')
        os.system('pip install bs4')
        os.system('pip install requests')
        os.system('pip install pathlib')

# This is Color's
underline = "\033[4m"
green = "\033[0;32m"
boldgreen = "\033[1;32m"
reset = "\033[0;0m"
white = "\033[0;37m"
boldwhite = "\033[1;37m"

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
cls()

# Will Update the Project if an Update Is Available
update()
savedir = "./Temp"

def banner():
    darkblue = "\033[1;30m"
    print(darkblue + '''
                 ███╗   ███╗ ██████╗ █████╗ ██╗  ██╗██╗ ██████╗ 
                 ████╗ ████║██╔════╝██╔══██╗╚██╗██╔╝██║██╔═══██╗
                 ██╔████╔██║██║     ███████║ ╚███╔╝ ██║██║   ██║
                 ██║╚██╔╝██║██║     ██╔══██║ ██╔██╗ ██║██║   ██║
                 ██║ ╚═╝ ██║╚██████╗██║  ██║██╔╝ ██╗██║╚██████╔╝
                 ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ''')
    print(boldgreen + '''
               
\t\t      Thank you for installing the project\n\t\t     We hope you read all the requirements'''.upper()+ '\n\t          ' + underline + 'https://github.com/Enmn/Mcattire#requirements' + reset)
    print('''               ''')
banner()

interface = input(boldgreen + f'''\n[{white + "1" + boldgreen}] To Generator or Random Minecraft Skins\n[{white + "2" + boldgreen}] To Steal Any Skin for Any Player\n[{white + "3" + boldgreen}] To Skin Pack Maker\n[{white + "4" + boldgreen}] To Skin Composition\n[{white + "5" + boldgreen}] To Show Current Version\n[{white + "6" + boldgreen}] To Exit\n\n{green + "[" + boldwhite + "Choose the Options" + green}]:~# ''' + white)
if interface == '1':
    os.system('python3 ./src/skins.py')
elif interface == '2':
    os.system('python3 ./src/theft.py')
elif interface == '3':
    os.system('python3 ./src/pack.py')
elif interface == '4':
    os.system('python3 ./src/composition.py')
elif interface == '5':
    version = open('.version', 'r').read()
    print('\n' + boldwhite + "Mcaxios Version ({version})".format(version=green + version + boldwhite))
elif interface == '6':
    exit()
