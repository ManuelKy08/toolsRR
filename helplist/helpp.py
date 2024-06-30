import os
from colorama import Fore
import time
import sys
def Banner():
    
    os.system("clear")
    
    print(Fore.LIGHTGREEN_EX+"""\n    
    ██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗ ██████╗
    ██║ ██╔╝██╔═══██╗██║ ██╔╝██╔═══██╗██║ ██╔╝     ██╔════╝██╔════╝██╔════╝
    █████╔╝ ██║   ██║█████╔╝ ██║   ██║█████╔╝█████╗███████╗█████╗  ██║     
    ██╔═██╗ ██║   ██║██╔═██╗ ██║   ██║██╔═██╗╚════╝╚════██║██╔══╝  ██║     
    ██║  ██╗╚██████╔╝██║  ██╗╚██████╔╝██║  ██╗     ███████║███████╗╚██████╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝ ╚═════╝
     ====================================================================
     **                  Instagram : @risky.manuel                     **
     **                  Telegram  : @kikikokok9                       **
     **                  Email     : riskymanuel08@proton.me           **
     ====================================================================          
          """)
# R
def infolist1():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"$"+Fore.RED+"]"+Fore.CYAN+" Just Choise Asshole \n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Vote me SiR!!\n")
    time.sleep(0.1)
    print(Fore.BLUE+" [2] Exit . . .\n")

def infolist2():
    time.sleep(0.1)
    print(Fore.GREEN+"  [1]"+Fore.BLUE+" - Admin Page Finder")    
    print(Fore.CYAN+"  **********************")
    time.sleep(0.2)

    print(Fore.GREEN+"  [2]"+Fore.BLUE+" - Brute Force")   
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [3]"+Fore.BLUE+" - Port Scan")   
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [4]"+Fore.BLUE+" - Spider Param")   
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [5]"+Fore.BLUE+" - SQL Injection Scan")    
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [6]"+Fore.BLUE+" - Subdomain Finder")
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [7]"+Fore.BLUE+" - Web Security Tools")    
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [8]"+Fore.BLUE+" - WordPress Scanner")    
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [9]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"  **********************")
    time.sleep(0.1)

    print(Fore.GREEN+"  [10]"+Fore.BLUE+" - Exit :) \n")

def infolist3():
    Banner()
    time.sleep(0.1)
    try:
        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
    except:
        print("")
        print("\n")
        sys.exit()