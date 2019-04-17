print("Importing dependencies")

try:
    import time
except:
    print("Couldn't import time library")

try:
    import shutil
except:
    print("Couldn't import shutil")

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

superColliderURL = "https://github.com/supercollider/supercollider/releases/download/Version-3.10.2/SuperCollider-3.10.2-Windows-x64-VS.exe"

scdURL = "https://github.com/moz-ljp/foxdotautoinstaller/releases/download/v0.3/startup.scd"

gitURL = "https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe"

superColliderFoxQuark = 'Quarks.install("FoxDot")'

foxInstalled = False

gitInstalled = False

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

    createStartup = input("Would you like to make a startup file for foxdot? (y/n): ")
    createStartup = createStartup.lower()

    if(createStartup == "y"):
        makeStartup()

    presGap()
    
    website = input("Do you want to visit their website (y/n): ")
    website = website.lower()
    if(website == "y"):
        os.system("start https://foxdot.org")

    presGap()
    
    myWeb = input("Would you like to visit my website? (y/n): ")
    myWeb = myWeb.lower()
    if(myWeb == "y"):
        os.system("start http://moz-programs.ml/home.html")

    mygithub = input("Would you like to visit my website? (y/n): ")
    mygithub = mygithub.lower()
    if(mygithub == "y"):
        os.system("start https://github.com/moz-ljp/foxdotautoinstaller/")

    print("Thankyou for using this tool")

def makeStartup():

    with open("FoxDot-Startup.py", "w") as file:
            file.write('import time\nimport os \nos.system("start scide.exe")\ntime.sleep(10)\nos.system("python -m FoxDot")')

    username = getpass.getuser()

    downloadDesktop = '/Users/'+username+'/Desktop/'

    
    print("Your startup file will be created")
    print("Where would you like your startup file installed")
    print("To enter an exact path, type the PATH (C:/Users/whatever")
    print("To install at desktop, type DESKTOP")
    location = input("")

    if(location != "DESKTOP"):
        shutil.move("FoxDot-Startup.py", location+"/FoxDot-Startup.py")
    elif(location == "DESKTOP"):
        shutil.move("FoxDot-Startup.py", "C:"+downloadDesktop+"/FoxDot-Startup.py")
        

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
        print("Installing GIT")
        presGap()
        urllib.request.urlretrieve(gitURL, downloadDesktop+'/Git-64.exe')
        print("Please run through the GIT setup")
        os.system(downloadDesktop+'/Git-64.exe')
        os.remove(downloadDesktop+'/Git-64.exe')
        presGap()
        gitInstalled = True


    gitInstalled = True


    if(gitInstalled == True):
        try:
            null = open("/dev/null", "w")
            subprocess.Popen("scide.exe", stdout=null, stderr=null)
            null.close()
            print("SuperCollider already installed")
      
            print("Installing SuperCollider")
            urllib.request.urlretrieve(superColliderURL, downloadDesktop+'/SuperCollider-Windows-x64-VS.exe')
            presGap()
            print("Please run through the SuperCollider setup")
            presGap()
            os.system(downloadDesktop+'/SuperCollider-Windows-x64-VS.exe')
            presGap()
            os.remove(downloadDesktop+'/SuperCollider-Windows-x64-VS.exe')
                
            with open("startup.scd", "w") as file:
                file.write('Quarks.install("FoxDot"); FoxDot.start')
            try:
                shutil.move("startup.scd", "C:/Users/"+username+"/AppData/Local/SuperCollider/startup.scd")
            except:
                print("Something went wrong moving the scd file")
                print("Using alternative method")
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
