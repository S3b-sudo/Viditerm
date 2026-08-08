from simple_term_menu import TerminalMenu
from rich import print
import os

os.system("clear")

while True: #Start Screen
    print(""" [green]__     __  __        __  __    __                                       
/  |   /  |/  |      /  |/  |  /  |                                      
$$ |   $$ |$$/   ____$$ |$$/  _$$ |_     ______    ______   _____  ____  
$$ |   $$ |/  | /    $$ |/  |/ $$   |   /      \  /      \ /     \/    \ 
$$  \ /$$/ $$ |/$$$$$$$ |$$ |$$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$ |  $$ | __ $$    $$ |$$ |  $$/ $$ | $$ | $$ |
  $$ $$/   $$ |$$ \__$$ |$$ |  $$ |/  |$$$$$$$$/ $$ |      $$ | $$ | $$ |
   $$$/    $$ |$$    $$ |$$ |  $$  $$/ $$       |$$ |      $$ | $$ | $$ |
    $/     $$/  $$$$$$$/ $$/    $$$$/   $$$$$$$/ $$/       $$/  $$/  $$/ """)
    print(" ")
    print("[bold] [red] ===================================================================================")
    print("[bold] [red] |                                  IMPORTANT                                      |")
    print("[bold] [red] ===================================================================================")
    print("[bold] [red] |               You NEED to have MPV installed and added to your                  |")
    print("[bold] [red] |                PATH(Linux) or Environment variables (Windows)                   |")
    print("[bold] [red] |                          for this to work properly.                             |")
    print("[bold] [red] ===================================================================================")
    options = ["Continue", "Help", "Quit"]
    terminal_menu = TerminalMenu(options, status_bar="[Arrow keys] - Move cursor | [Return] - Select")
    menu_entry_index = terminal_menu.show()
    choice = options[menu_entry_index]
    
    if choice == "Continue":
        break
    
    if choice == "Help":
        print("[bold] [white] ===================================================================================")
        print("[bold] [white] |                                     Help                                        |")
        print("[bold] [white] ===================================================================================")
        print("[bold] [white] |                               Install on linux                                  |")
        print("[bold] [white] |                      Debian/Ubuntu: sudo apt install mpv                        |")
        print("[bold] [white] |                      Fedora/Redhat: sudo dnf install mpv                        |")
        print("[bold] [white] |                        Once installed reopen Videterm                           |")
        print("[bold] [white] |                                                                                 |")
        print("[bold] [white] |                              Install on Windows                                 |")
        print("[bold] [white] |                      Go to: https://mpv.io/installation/                        |")
        print("[bold] [white] |         Pick ether the first or second version, the choice is up to you.        |")
        print("[bold] [white] ===================================================================================")
        print("[bold] [white] |                               (Return) - Quit                                   |")
        print("[bold] [white] ===================================================================================")
        input()
        quit()
    
    
    if choice == "Quit":
        quit()

os.system("clear")

while True:
    print(""" [green]__     __  __        __  __    __                                       
/  |   /  |/  |      /  |/  |  /  |                                      
$$ |   $$ |$$/   ____$$ |$$/  _$$ |_     ______    ______   _____  ____  
$$ |   $$ |/  | /    $$ |/  |/ $$   |   /      \  /      \ /     \/    \ 
$$  \ /$$/ $$ |/$$$$$$$ |$$ |$$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$ |  $$ | __ $$    $$ |$$ |  $$/ $$ | $$ | $$ |
  $$ $$/   $$ |$$ \__$$ |$$ |  $$ |/  |$$$$$$$$/ $$ |      $$ | $$ | $$ |
   $$$/    $$ |$$    $$ |$$ |  $$  $$/ $$       |$$ |      $$ | $$ | $$ |
    $/     $$/  $$$$$$$/ $$/    $$$$/   $$$$$$$/ $$/       $$/  $$/  $$/ """)
    print(" ")
    print("Play video files inside the terminal!")
    print("========================================================================")
    options = ["Play video", "Play video (Ascii)", "About" ,"Quit"]
    terminal_menu = TerminalMenu(options, status_bar="[Arrow keys] - Move cursor | [Return] - Select")
    menu_entry_index = terminal_menu.show()
    choice = options[menu_entry_index]

    if choice == "About":
        print("Created by:")
        print("""   [red]█████████   ████████  ███████████ 
 [red]███▒▒▒▒▒███ ███▒▒▒▒███▒▒███▒▒▒▒▒███
[green]▒███    ▒▒▒ ▒▒▒    ▒███ ▒███    ▒███
[green]▒▒█████████    ██████▒  ▒██████████ 
 [blue]▒▒▒▒▒▒▒▒███  ▒▒▒▒▒▒███ ▒███▒▒▒▒▒███
 [blue]███    ▒███ ███   ▒███ ▒███    ▒███
[yellow]▒▒█████████ ▒▒████████  ███████████ 
 [yellow]▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  
https://github.com/S3b-sudo/Viditerm""")
        
    if choice == "Quit":
        print("[bold] [yellow] Thanks for using Videterm by Seb :)")
        quit()
   
    if choice == "Play video":
        break
    
    if choice == "Play video (Ascii)":
        os.system("clear")
        print(""" [green]__     __  __        __  __    __                                       
/  |   /  |/  |      /  |/  |  /  |                                      
$$ |   $$ |$$/   ____$$ |$$/  _$$ |_     ______    ______   _____  ____  
$$ |   $$ |/  | /    $$ |/  |/ $$   |   /      \  /      \ /     \/    \ 
$$  \ /$$/ $$ |/$$$$$$$ |$$ |$$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$ |  $$ | __ $$    $$ |$$ |  $$/ $$ | $$ | $$ |
  $$ $$/   $$ |$$ \__$$ |$$ |  $$ |/  |$$$$$$$$/ $$ |      $$ | $$ | $$ |
   $$$/    $$ |$$    $$ |$$ |  $$  $$/ $$       |$$ |      $$ | $$ | $$ |
    $/     $$/  $$$$$$$/ $$/    $$$$/   $$$$$$$/ $$/       $$/  $$/  $$/ """)
    print(" ")
    print("  Mode: Askii")
    print("[bold] [white] ===================================================================================")
    print("[bold] [white] |                                 Video Player                                    |")
    print("[bold] [white] ===================================================================================")
    print("[bold] [white] |(Full Path) - Plays the video | (Youtube Link) - Plays youtube video | (1) - Quit|")
    print("[bold] [white] ===================================================================================")
    print("[bold] [yellow] HINT: You can drag and drop videos in the terminal to play them!")
    while True:
            path_resp = input("Enter path: ")
    
            if path_resp == "1":
                print("[bold][yellow] Thanks for using Videterm by Seb :)")
                quit()
            
            os.system(f"env CACA_DRIVER=ncurses mpv -quiet -vo=caca {path_resp}")


os.system("clear")
print(""" [green]__     __  __        __  __    __                                       
/  |   /  |/  |      /  |/  |  /  |                                      
$$ |   $$ |$$/   ____$$ |$$/  _$$ |_     ______    ______   _____  ____  
$$ |   $$ |/  | /    $$ |/  |/ $$   |   /      \  /      \ /     \/    \ 
$$  \ /$$/ $$ |/$$$$$$$ |$$ |$$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$ |  $$ | __ $$    $$ |$$ |  $$/ $$ | $$ | $$ |
  $$ $$/   $$ |$$ \__$$ |$$ |  $$ |/  |$$$$$$$$/ $$ |      $$ | $$ | $$ |
   $$$/    $$ |$$    $$ |$$ |  $$  $$/ $$       |$$ |      $$ | $$ | $$ |
    $/     $$/  $$$$$$$/ $$/    $$$$/   $$$$$$$/ $$/       $$/  $$/  $$/ """)
print(" ")
print(" Mode: Standered")
print("[bold] [white] ===================================================================================")
print("[bold] [white] |                                 Video Player                                    |")
print("[bold] [white] ===================================================================================")
print("[bold] [white] |(Full Path) - Plays the video | (Youtube Link) - Plays youtube video | (1) - Quit|")
print("[bold] [white] ===================================================================================")
print("[bold] [yellow] HINT: You can drag and drop videos in the terminal to play them!")
while True:

    path_resp = input("Enter path: ")
    
    if path_resp == "1":
        print("[bold][yellow]Thanks for using Videterm :)")
        quit()
    
    os.system(f"mpv --no-config --vo=tct {path_resp}")