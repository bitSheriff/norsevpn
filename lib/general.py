    
import logging
import os, sys, string, subprocess


## 
# @private
# @brief    Get string from a OS command
#
# @param cmnd   Command which is executed
# @returns      Returns the string which the OS returned on the stdout
def getOSString(cmnd):
    call = os.popen(cmnd, 'r')
    return call.read()

def osCommandThread(cmnd):
    subprocess.Popen([sys.executable, cmnd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def getGitLatestTag():
    return getOSString("git describe --tags --abbrev=0")

def getGitHashLong():
    return getOSString("git rev-parse HEAD")

def getGitHashShort():
    return getOSString("git rev-parse --short HEAD")

def logFileHeader():
    logging.basicConfig(filename='norsevpn.log',
    filemode='w', encoding='utf-8',
    level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
    
    logging.info("norseVPN version: " + getGitLatestTag())
    logging.info("norseVPN git-hash: " + getGitHashLong())
    logging.info("nordvpn version: " + getOSString("nordvpn --version") )
    logging.info("openvpn version: " + getOSString("openvpn --version") )


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)