import os
import sys
from yachalk import chalk


def close():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

        
close()
print(chalk.rgb(0, 255, 247).bold("""
\t┌──────────────────────────────────────────────────────────────────────┐
\t│                                                                      │
\t│ ▄▄▄  ▄▄▄     ▄▄▄▄     ▄▄▄▄    ▄▄   ▄▄▄   ▄▄▄▄▄▄   ▄▄▄   ▄▄    ▄▄▄▄   │
\t│ ███  ███   ██▀▀▀▀█  ▄█▀▀▀▀█   ██  ██▀    ▀▀██▀▀   ███   ██  ▄█▀▀▀▀█  │
\t│ ████████  ██▀       ██▄       ██▄██        ██     ██▀█  ██  ██▄      │
\t│ ██ ██ ██  ██         ▀████▄   █████        ██     ██ ██ ██   ▀████▄  │
\t│ ██ ▀▀ ██  ██▄            ▀██  ██  ██▄      ██     ██  █▄██       ▀██ │
\t│ ██    ██   ██▄▄▄▄█  █▄▄▄▄▄█▀  ██   ██▄   ▄▄██▄▄   ██   ███  █▄▄▄▄▄█▀ │
\t│ ▀▀    ▀▀     ▀▀▀▀    ▀▀▀▀▀    ▀▀    ▀▀   ▀▀▀▀▀▀   ▀▀   ▀▀▀   ▀▀▀▀▀   │
\t│                                                                      │
\t│                                                                      │
\t└──────────────────────────────────────────────────────────────────────┘
"""))
print(("\t  Thank you very much for installing the tool, We wish you a beautiful".upper()))
print(('\t\t\tFollow me on my GitHub account!'.upper()))
print(('        \t\tGitHub: '.upper()) + chalk.underline('https://github.com/Enmn'))
one = input(chalk.bold("\nPress Enter if You Are Ready..."))
os.system('python3 ./utils/Skins.py')
exit()
