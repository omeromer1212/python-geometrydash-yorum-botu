import asyncio
from colorama import Fore,Style
import gd
import time
client = gd.Client()
dailyweeeklyoptexists = False
from datetime import datetime
print(f"""{Fore.LIGHTCYAN_EX}{Style.DIM}                                                                                                                                                                
  ____ ____     ____ ___  __  __ __  __ _____ _   _ _____   ____   ___ _____
 / ___|  _ \   / ___/ _ \|  \/  |  \/  | ____| \ | |_   _| | __ ) / _ \_   _|
| |  _| | | | | |  | | | | |\/| | |\/| |  _| |  \| | | |   |  _ \| | | || |
| |_| | |_| | | |__| |_| | |  | | |  | | |___| |\  | | |   | |_) | |_| || |
 \____|____/   \____\___/|_|  |_|_|  |_|_____|_| \_| |_|   |____/ \___/ |_|
Made by xXOmerXx#1995                                                                                                                                                       {Fore.RESET}""")
print(f"{Fore.LIGHTCYAN_EX}msgs will be sent every 50 sec to avoid overflow{Fore.RESET}")
user = input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Enter your username:\n{Fore.RED}>{Fore.RESET}")
passw = input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Enter your password: (only sent to gd servers for auth):\n{Fore.RED}>{Fore.RESET}")
id = int(input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Enter lvl id for spam (leave 0 for daily or weekly):\n{Fore.RED}>{Fore.RESET}"))
comment = input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Write your comment you desire to be spammed (dont write more than 100 chars, it will be cutted off):\n{Fore.RED}>{Fore.RESET}")
per = int(input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Enter comment's percentage (leave 0 to be no percentage):\n{Fore.RED}>{Fore.RESET}"))
commentnumber = int(input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Enter the number of comments u would like to spam:\n{Fore.RED}>{Fore.RESET}"))
if id == 0:
    dailyorweekly = int(input(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}You selected daily or weekly, 0 for daily, 1 for weekly:\n{Fore.RED}>{Fore.RESET}"))
    dailyweeeklyoptexists = True


async def main():
    await client.login(user, passw)
    level = await client.get_level(id)
    for i in range(commentnumber):
        await level.comment(comment, per)
        rightnow = datetime.now()
        date = datetime.ctime(rightnow)
        print(f"{Fore.LIGHTRED_EX}Succesfully commented on level (id) {Fore.LIGHTBLUE_EX}{str(id)}{Fore.RESET} //{Fore.LIGHTRED_EX} Comment: {Fore.LIGHTBLUE_EX}{comment}{Fore.RESET} {Fore.LIGHTRED_EX}On {date}{Fore.RESET}")
        time.sleep(55)

async def dailyorweeklymain():
    await client.login(user, passw)
    if dailyorweekly == 0:
        level = await client.get_daily()
        for i in range(commentnumber):
            await level.comment(comment, per)
            rightnow = datetime.now()
            date = datetime.ctime(rightnow)
            print(f"{Fore.LIGHTRED_EX}Succesfully commented on level (id) {Fore.LIGHTBLUE_EX}{str(id)}{Fore.RESET} //{Fore.LIGHTRED_EX} Comment: {Fore.LIGHTBLUE_EX}{comment}{Fore.RESET} {Fore.LIGHTRED_EX}On {date}{Fore.RESET}")
            time.sleep(50)
    elif dailyorweekly == 1:
        level = await client.get_weekly()
        for i in range(commentnumber):
            await level.comment(comment, per)
            rightnow = datetime.now()
            date = datetime.ctime(rightnow)
            print(f"{Fore.LIGHTRED_EX}Succesfully commented on level (id) {Fore.LIGHTBLUE_EX}{str(id)}{Fore.RESET} //{Fore.LIGHTRED_EX} Comment: {Fore.LIGHTBLUE_EX}{comment}{Fore.RESET} {Fore.LIGHTRED_EX}On {date}{Fore.RESET}")
            time.sleep(50)

if dailyweeeklyoptexists == True:
    asyncio.run(dailyorweeklymain())
elif dailyweeeklyoptexists == False:
    asyncio.run(main())


