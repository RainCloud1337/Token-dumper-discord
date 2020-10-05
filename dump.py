import re
import time, random, os, sys, urllib
from urllib.parse import unquote
from colorama import Fore
try:
    import requests
except ImportError:
    print ('[*] pip install requests')
    print ('[-] you need to install requests Module')
    exit()
try:
    from colorama import Fore
except ImportError:
    print ('[*] pip install colorama')
    print ('[-] you need to install requests Module')
    exit()
try:
    from googlesearch import search
except ImportError:
    print ('[*] pip install google search')
    print ('[-] you need to install requests Module')
    exit()

def menusel():
    print(f"""{Fore.RED}

▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █    ▓█████▄  █    ██  ███▄ ▄███▓ ██▓███  ▓█████  ██▀███
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▒██▀ ██▌ ██  ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ░██   █▌▓██  ▒██░▓██    ▓██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░▓█▄   ▌▓▓█  ░██░▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ░▒████▓ ▒▒█████▓ ▒██▒   ░██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒     ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░    ░ ▒  ▒ ░░▒░ ░ ░ ░  ░      ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
  ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ░ ░  ░  ░░░ ░ ░ ░      ░   ░░          ░     ░░   ░
             ░ ░  ░  ░      ░  ░         ░       ░       ░            ░               ░  ░   ░
{Fore.WHITE}
[1] : Crawl Links
[2] : Scrape Links
[3] : Exit
""")

    sel = input("> ")
    if sel=="1":
        clear()
        print("[*] Starting Cralwer")
        Crawler()

    elif sel=="2":
        clear()
        print("[*] Starting Scraper")
        Scraper()

    elif sel=="3":
        clear()
        print("[*] Exiting")
        exit()

clear = lambda: os.system('cls')

def menu():
    clear()
    menusel()

def Crawler():

    # Using readlines()
    siteslst = open('sites.txt', 'r')
    Sites = siteslst.readlines()

    # Delete Last Sites
    f = open("tokens.txt", "w")
    f.write("")
    f.close()

    count = 0
    for line in Sites:
        data = requests.get(line)
        Token = re.findall(r'([\w-]{24}\.[\w-]{6}\.[\w-]{27})', data.text)

        with open('tokens.txt', 'a') as filehandle:
            for listitem in Token:
                filehandle.write('%s\n' % listitem)
                print('%s' % listitem)

    print(f'{Fore.GREEN}[!] Finsihed Crawling | Tokens Located in tokens.txt')
    input()
    menu()

def Scraper():
    print("[*] How many links would you like to scrape")

    scrnum = input("> ")

    # Delete Last Sites
    f = open("sites.txt", "w")
    f.write("")
    f.close()

    # Write All Scraped Sites
    f = open("sites.txt", "a")
    for url in search('site:"pastebin.com" Discord Tokens', stop=int(scrnum)):
        print(Fore.YELLOW + url)
        f.write(f'{url}\n')
    f.close()
    print(f'{Fore.GREEN}[!] Finsihed Scraping | You Can Now Crawl The Sites')
    input()
    menu()

menu()
