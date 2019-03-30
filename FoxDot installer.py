print("Importing dependencies")

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

scdURL = "https://github-production-release-asset-2e65be.s3.amazonaws.com/178582065/d1242d00-530d-11e9-8a94-8fab2dca6cf5?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20190330%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190330T170408Z&X-Amz-Expires=300&X-Amz-Signature=d15c75fedb152922722085de3d628cccb6a412634c394f37bd066d6ea1b35221&X-Amz-SignedHeaders=host&actor_id=39520581&response-content-disposition=attachment%3B%20filename%3DfoxinstallSupercollider.scd&response-content-type=application%2Foctet-stream"

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
        urllib.request.urlretrieve(scdURL, downloadDesktop+'/initial-run.scd')
        proc = subprocess.Popen(downloadDesktop+'/initial-run.scd', shell=True)
        print("Press CTRL + Enter on line 1 and wait")
        input("Press enter when it is complete")
        print("Press CTRL + Enter on line 3 and wait")
        input("Press enter when it is complete")
        print("Press CTRL + Enter on line 5 and wait")
        input("Press enter when it is complete")
        presGap()
        print("Starting FoxDot")
        after()
        procTwo = subprocess.Popen("python -m FoxDot", shell=True)
    except:
        print("Something went wrong trying to install SuperCollider")

input("")
