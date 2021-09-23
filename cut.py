# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# AUTHOR : MrTechX | ToolsX | UlisesCamacho
# PROJECT : URL Shortener with Python
# VERSION : 1.5.0
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
import time
import pyshorteners
import os
from colorama import Fore,Back,Style
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
clearConsole()

print(Fore.LIGHTRED_EX+'''


 /$$$$$$$$                  /$$       /$$   /$$       /$$   /$$ /$$$$$$$  /$$      
|__  $$__/                 | $$      | $$  / $$      | $$  | $$| $$__  $$| $$      
   | $$  /$$$$$$   /$$$$$$$| $$$$$$$ |  $$/ $$/      | $$  | $$| $$  \ $$| $$      
   | $$ /$$__  $$ /$$_____/| $$__  $$ \  $$$$/       | $$  | $$| $$$$$$$/| $$      
   | $$| $$$$$$$$| $$      | $$  \ $$  >$$  $$       | $$  | $$| $$__  $$| $$      
   | $$| $$_____/| $$      | $$  | $$ /$$/\  $$      | $$  | $$| $$  \ $$| $$      
   | $$|  $$$$$$$|  $$$$$$$| $$  | $$| $$  \ $$      |  $$$$$$/| $$  | $$| $$$$$$$$
   |__/ \_______/ \_______/|__/  |__/|__/  |__/       \______/ |__/  |__/|________/


''')
url = input(Fore.LIGHTGREEN_EX+"💀 Ingresa tu link => "+Fore.LIGHTRED_EX)

shrt = pyshorteners.Shortener()

nurl = shrt.tinyurl.short(url) 

print(Fore.LIGHTGREEN_EX+"🔥 Toma tu nuevo link => " +Fore.LIGHTBLUE_EX+nurl)

time.sleep(4)
print(Fore.LIGHTMAGENTA_EX+'''



coded by: MrTechX | ToolsX | UlisesCamacho                            
 /$$      /$$        /$$$$$$$$                  /$$       /$$   /$$
| $$$    /$$$       |__  $$__/                 | $$      | $$  / $$
| $$$$  /$$$$  /$$$$$$ | $$  /$$$$$$   /$$$$$$$| $$$$$$$ |  $$/ $$/
| $$ $$/$$ $$ /$$__  $$| $$ /$$__  $$ /$$_____/| $$__  $$ \  $$$$/ 
| $$  $$$| $$| $$  \__/| $$| $$$$$$$$| $$      | $$  \ $$  >$$  $$ 
| $$\  $ | $$| $$      | $$| $$_____/| $$      | $$  | $$ /$$/\  $$
| $$ \/  | $$| $$      | $$|  $$$$$$$|  $$$$$$$| $$  | $$| $$  \ $$
|__/     |__/|__/      |__/ \_______/ \_______/|__/  |__/|__/  |__/
''' )
