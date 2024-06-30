#!/usr/bin/env python3

import sys
import os
from colorama import Fore, init
from helplist import helpp
from modules import AdminLogin, bruteforce, port, SpideRparam, sql, subdomain, WebSec, wordpress

try:
    import requests
except ImportError:
    os.system("clear")
    print("\n Please Install requests\npip3 install requests")
    sys.exit()

try:
    import ipapi
except ImportError:
    os.system("clear")
    print("\n Please Install ipapi\npip3 install ipapi")
    sys.exit()

try:
    import builtwith
except ImportError:
    os.system("clear")
    print("\n Please Install builtwith\npip3 install builtwith")
    sys.exit()

try:
    import bs4
except ImportError:
    os.system("clear")
    print("\n Please Install bs4\npip3 install bs4")
    sys.exit()

init(autoreset=True)

def main_menu():
    while True:
        try:
            helpp.Banner()
            helpp.infolist1()
            number = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "$ ").lower()
        except KeyboardInterrupt:
            print("\n Good Luck :)")
            sys.exit()

        if number == '4':
            sys.exit()

        elif number == "3":
            helpp.infolist3()
        
        elif number == "":
            print(Fore.RED + " [!]" + Fore.BLUE + " Pilih nomor nya bambang mo di tonjok si risky? haa... :))))")
            input("")

        elif number == '1':
            try:
                information_gathering_menu()
            except KeyboardInterrupt:
                print("")
                sys.exit()

        elif number == "2":
            cms_detection_menu()

def information_gathering_menu():
    helpp.Banner()
    helpp.infolist2()
    infor = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "Information Gathering" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "$ ").lower()

    if infor == "1":
        helpp.Banner()
        AdminLogin.__start__()

    elif infor == "2":
        helpp.Banner()
        bruteforce.__start__()

    elif infor == "3":
        helpp.Banner()
        SpideRparam.__start__()

    elif infor == "4":
        helpp.Banner()
        sql.__start__()

    elif infor == "5":
        helpp.Banner()
        port.__start__()

    elif infor == "6":
        helpp.Banner()
        WebSec.__start__()

    elif infor == "7":
        helpp.Banner()
        subdomain.__start__()

    elif infor == "8":
        helpp.Banner()
        wordpress.__start__()

    elif infor == "9":
        input(Fore.RED + " [!]" + Fore.GREEN + " Back To Menu (Press Enter...) ")

    elif infor == "10":
        sys.exit()

    elif infor == "":
        input(Fore.RED + " [!]" + Fore.GREEN + " sibaa pilih lah bang (Press Enter...) ")

def cms_detection_menu():
    # Pastikan fungsi yang tepat dipanggil di sini
    helpp.infolist1()  # Ganti sesuai fungsi yang ada di helpp
    try:
        numcms = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "CMS Detection" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "$ ").lower()
    except KeyboardInterrupt:
        print("")
        sys.exit()

    if numcms == "1":
        helpp.infowp()
        try:
            wp = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "RRSEC" + Fore.BLUE + "~" + Fore.WHITE + "@ROOT" + Fore.RED + "/" + Fore.CYAN + "CMS" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "WordPress" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "$ ").lower()
        except KeyboardInterrupt:
            print("")
            sys.exit()

        if wp == "1":
            helpp.Banner()
            wordpress.wpplug()

        elif wp == "2":
            helpp.Banner()
            wordpress.user()

        elif wp == "3":
            try:
                input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
            except KeyboardInterrupt:
                print("\n")
                sys.exit()

    elif numcms == "2" or numcms == "3":
        helpp.Banner()
        print(Fore.RED + " [!]" + Fore.BLUE + " Coming Soon! ")
        try:
            input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

    elif numcms == "4":
        try:
            input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

    elif not numcms:
        try:
            input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

if __name__ == "__main__":
    main_menu()
