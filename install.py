import os
import requests
import shutil

print("Viditerm Installer")
print("=========================")

if os.name == "posix":
    pass
else:
    print("[ERROR] You are running Windows or another opperating system which may not be supported")
    print("=========Options=========")
    print("(1) Run Anyway")                                                                             
    print("(Return) Quit")
    
    while True:
        choice = input("Choose a Nomber: ")

        if choice == "1":
            pass
        else:
            quit()

input("Press 'Return' to begin: ")

print("Creating virtual python environment...")
os.system("python -m venv vite")
print("==================")
print("Installing dependencies...")
os.system("source vite/bin/activate && pip install -r requirements.txt")

print("==================")    
if shutil.which('apt'):
    print("APT requirements detected, type sudo password to install")
    print("Note: You will see what is being installed after typing in your password")
    os.system("sudo apt install mpv")
elif shutil.which('dnf'):
    print("DNF requirements detected, type sudo password to install")
    print("Note: You will see what is being installed after typing in your password")           
    os.system("sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm")
    os.system("sudo dnf install mpv")
else:
    print("Unknown Package Manager, skipping requirements")  

print("==================")
print("Making run.sh executable...")
os.system("chmod +x run.sh")
print("==================")

print("Done")
quit()
