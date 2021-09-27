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

              @@@  @@@,            
         (@@@@@@@  @@@@@@**        
     @@@@@@@@@@@*  @@@@@@***@@@@   
   @@@@@@@@@*****,@@@@@@@***@@@@@@ 
   @@@@/    *@@@@@@@@@@@,   @@@@@@ 
   ******@@@@@@@@@@@*****@@@@@@@@@ 
    *@@@@@@@@@@@    *@@@@@@@@@@@   
   @@@@@@@@@****,@@@@@@@@@@@*****, 
   @@@@@    @@@@@@@@@@@/    *@@@@@ 
   @@@@@***@@@@@@@@******@@@@@@@@@ 
    ,@@@***@@@@@@   ,@@@@@@@@@@@   
         **@@@@@@   @@@@@@@        
              @@@   @@@            
 _____         _    __  __  _   _ ____  _
|_   _|__  ___| |__ \ \/ / | | | |  _ \| |
  | |/ _ \/ __| '_ \ \  /  | | | | |_) | |
  | |  __/ (__| | | |/  \  | |_| |  _ <| |___
  |_|\___|\___|_| |_/_/\_\  \___/|_| \_\_____|

''')
url = input(Fore.LIGHTGREEN_EX+"💀 Ingresa tu link => "+Fore.LIGHTRED_EX)

shrt = pyshorteners.Shortener()

nurl = shrt.tinyurl.short(url) 

print(Fore.LIGHTGREEN_EX+"🔥 Toma tu nuevo link => " +Fore.LIGHTBLUE_EX+nurl)

time.sleep(2)
print(Fore.LIGHTRED_EX+'''



code by: MrTechX | ToolsX | UlisesCamacho                            
              @@@  @@@,            
         (@@@@@@@  @@@@@@**        
     @@@@@@@@@@@*  @@@@@@***@@@@   
   @@@@@@@@@*****,@@@@@@@***@@@@@@ 
   @@@@/    *@@@@@@@@@@@,   @@@@@@ 
   ******@@@@@@@@@@@*****@@@@@@@@@ 
    *@@@@@@@@@@@    *@@@@@@@@@@@   
   @@@@@@@@@****,@@@@@@@@@@@*****, 
   @@@@@    @@@@@@@@@@@/    *@@@@@ 
   @@@@@***@@@@@@@@******@@@@@@@@@ 
    ,@@@***@@@@@@   ,@@@@@@@@@@@   
         **@@@@@@   @@@@@@@        
              @@@   @@@            
''' )