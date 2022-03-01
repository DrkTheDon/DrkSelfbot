#!/usr/bin/python3

#####################################################
## Dark's SelfBot (DrkSelfBot)                     ##
## A discord Selfbot.                              ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
import discord
from colorama import Fore
import time
import os
import itertools
from datetime import datetime




# Useful Defines
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Global Variables
bot = discord.Client()
TOKEN = "YOUR_TOKEN_HERE" # This is for Debugging/Developing
now = datetime.now()
curtime = now.strftime("%H:%M")

# Main 
clearcmd()

print(f"{Fore.YELLOW}[*] Initializing")
time.sleep(3.5)
clearcmd()


@bot.event
async def on_ready():
    print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Conntected to {Fore.YELLOW}{bot.user}                                                                  {Fore.LIGHTWHITE_EX}Press {Fore.YELLOW}CTRL + C {Fore.LIGHTWHITE_EX}to quit")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}[!]{Fore.LIGHTWHITE_EX} Send {Fore.YELLOW}drk$help{Fore.LIGHTWHITE_EX} to start!\n\n")
    

@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
    if message.content == "drk$help":
        await message.channel.send(f"@{message.author} This bot is under development!") 
        print(f"{Fore.BLUE}{curtime} {Fore.YELLOW}[*] {Fore.LIGHTWHITE_EX}Sent {Fore.RED}This bot is under development!{Fore.LIGHTWHITE_EX} in {Fore.YELLOW}#{message.channel} ")

# Main Run
try:
    bot.run(TOKEN, bot=False)
except discord.errors.LoginFailure:
    print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Inproper Token or disabled account.")
    time.sleep(0.5)
    quit()
