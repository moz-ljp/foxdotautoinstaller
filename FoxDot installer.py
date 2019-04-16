print("Importing dependencies")

import time

try:
    import os
except:
    print("Couldn't import os library")

try:
    import sys
except:
    print("Couldn't import sys library")

try:
    import platform
except:
    print("Couldn't import platform library")

try:
    import subprocess
except:
    print("Couldn't import subprocess library")

try:
    import urllib.request
except:
    print("Couldn't import urllib.request library")

try:
    import getpass
except:
    print("Couldn't import getpass library")

try:
    import pyperclip
except:
    pyperClipFound = input("Pyperclip library not found - install? (y/n)")
    pyperClipFound.lower()
    if(pyperClipFound == "y"):
        os.system("pip install pyperclip")
        import pyperclip
    else:
        print("Pyperclip not installed")

superColliderURL = "https://github.com/supercollider/supercollider/releases/download/Version-3.10.2/SuperCollider-3.10.2-Windows-x64-VS.exe"

scdURL = "https://github.com/moz-ljp/foxdotautoinstaller/releases/download/v0.3/startup.scd"

superColliderFoxQuark = 'Quarks.install("FoxDot")'

foxInstalled = False

username = getpass.getuser()

downloadDesktop = '/Users/'+username+'/Desktop/'

def presGap():
    print("")
    print("--------------------------------")
    print("")

def after():

    presGap()
    
    print("FoxDot is now installed and should be fully functional")

    presGap()
    
    website = input("Do you want to visit their website (y/n): ")
    website = website.lower()
    if(website == "y"):
        os.system("start https://foxdot.org")

    print("Thankyou for using this tool")

    presGap()
    
    myWeb = input("Would you like to visit my website? (y/n): ")
    myWeb = myWeb.lower()
    if(myWeb == "y"):
        os.system("start http://moz-programs.ml/home.html")

presGap()

print("FoxDot Installation")

presGap()

print("This installation file is for Windows")

print("Computer name:", os.environ['COMPUTERNAME'])

print("OS:", platform.system())

print("Release:", platform.release())

print("Version:", platform.version())

print("Username:", getpass.getuser())

if(platform.system() == "Windows"):

    try:
        presGap()
        print("Installing FoxDot python library")
        presGap()
        installFox = subprocess.Popen("pip install FoxDot", shell=True, stdout=subprocess.PIPE).stdout
        installDetails = installFox.read()
        presGap()
        print("Install results")
        print("")
        print(installDetails)
        presGap()
        print("Finished installing FoxDot")
        try:
            print("Checking that it's the latest version")
            os.system("pip install FoxDot --upgrade")
        except:
            print("Something went wrong checking if its the latest ")
        foxInstalled = True
        presGap()
    except:
        print("Something went wrong trying to install FoxDot")
        print("Do you have PIP installed?")
        getPip = input("Do you want to try to install PIP? (y/n)")
        getPip = getPip.lower()
        if(getPip == "y"):
            os.system("python get-pip.py")

if(foxInstalled == True):
    try:
        print("Installing SuperCollider")
        urllib.request.urlretrieve(superColliderURL, downloadDesktop+'/SuperCollider-Windows-x64-VS.exe')
        presGap()
        print("Please run through the SuperCollider setup")
        presGap()
        os.system(downloadDesktop+'/SuperCollider-Windows-x64-VS.exe')
        presGap()
        os.remove(downloadDesktop+'/SuperCollider-Windows-x64-VS.exe')
        urllib.request.urlretrieve(scdURL, 'C:/Users/'+username+'/AppData/Local/SuperCollider/startup.scd')
        os.system("start scide.exe")
        presGap()
        time.sleep(10)
        print("Starting FoxDot")
        procTwo = subprocess.Popen("python -m FoxDot", shell=True)
        after()
    except:
        print("Something went wrong trying to install SuperCollider")

input("")
