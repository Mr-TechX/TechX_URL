# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# AUTHOR : MrTechX | ToolsX | UlisesCamacho
# PROJECT : URL Spoofer with Python
# VERSION : 1.6.0
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
import gdshortener                                                                              
import os                                                                                       
import time                                                                                     
from colorama import Fore,Back,Style
def ascii():                                                                                        
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
 _______        _    __   __  _    _ _____  _      
|__   __|      | |   \ \ / / | |  | |  __ \| |     
   | | ___  ___| |__  \ V /  | |  | | |__) | |     
   | |/ _ \/ __| '_ \  > <   | |  | |  _  /| |     
   | |  __| (__| | | |/ . \  | |__| | | \ \| |____ 
   |_|\___|\___|_| |_/_/ \_\  \____/|_|  \_|______|

   code by: MrTechX | ToolsX | UlisesCamacho

''')

def clear():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux
    else:
        os.system("clear")

def load():
    print(Fore.LIGHTGREEN_EX+"Generando tu nuevo url💀...")
    
def get_url_shortened():
    request_gdshortener = gdshortener.ISGDShortener()
    url = input(Fore.LIGHTGREEN_EX+"💀 Ingresa tu link >>> "+Fore.LIGHTRED_EX)
    custom_url_part = input(Fore.LIGHTGREEN_EX+"Ingresa palabras clave💀 >>> "+Fore.LIGHTRED_EX)
    true_custom_url_part = "https://" + custom_url_part + "@"
    load()
    time.sleep(1)
    shortened_url = request_gdshortener.shorten(url)
    newurl = shortened_url[0]
    final_url = newurl.replace("https://", true_custom_url_part)
    print(Fore.LIGHTGREEN_EX+"Toma tu nuevo link💀 >>> "+Fore.LIGHTRED_EX + final_url+Fore.LIGHTBLUE_EX)

clear()
ascii()
get_url_shortened()
