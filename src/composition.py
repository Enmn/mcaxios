import os
from PIL import Image

# This is Color's
green = "\033[0;32m"
reset = "\033[0;0m"
white = "\033[0;37m"
red = "\033[0;31m"
boldred = "\033[1;31m"
boldwhite = "\033[1;37m"
boldgreen = "\033[1;32m"

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

savedir = "./trash"
headname = input(green + 'Here Enter the Name of the Head: ' + white)
bodyname = input(green + 'Here Enter the Name of the Body: ' + white)

def crop():
    # Opens a Image in RGB Mode
    try:
        img = Image.open(headname)
        right = 64
        bottom = 16
        crop = img.crop((0, 0, right, bottom))
        save_to = os.path.join(savedir, "head.png")
        crop.save(save_to)
    except FileNotFoundError:
        print("\n" + boldred +"ERROR: " + red + "There Is No File Named '{file}'".format(file=headname))
        exit()
crop()



def paste():
    # Here He Sticks the Head of the Skin
    try:
        img = Image.open(bodyname)
        img_two = Image.open('./trash/head.png')
        img = img.convert("RGBA")
        img_two = img_two.convert("RGBA")
        img.paste(img_two, (0, 0, 64, 16))
        save_to = os.path.join(savedir, "skin.png")
        img.save(save_to)
        os.remove("./trash/head.png")
    except FileNotFoundError:
        print("\n" + boldred +"ERROR: " + red + "There Is No File Named '{file}'".format(file=bodyname))
        exit()
paste()
print('\n' + "completed you will find the skin in")
