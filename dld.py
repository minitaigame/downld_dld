import os
import sys
from fdld import *
import re


name = "dld"
version = "1.0.0"
argvs = ['-v','-p','-s','-rl','-h']

# get options from argv
def getOptions():
    options = []
    for i in list(getArgvs()):
        if i in argvs:
            options.append(i)
    if len(options) > 0:
        return options
    else:
        return None
def getArgvs():
    argvsList = str()
    for i in sys.argv:
        argvsList += str(i) + "\n"
    
    argvsList = argvsList.split("\n")
    return argvsList

def getUrl():
    for i in sys.argv:
        url = re.compile(
            r'^(?:http|ftp)s?://',re.IGNORECASE).match(i)
        if not url == None:
            return url.string
    
    print("error: please check your url, make sure it starts with http:// or https://")
    return None

def getPath():
    for i in sys.argv:
        if os.path.isdir(i):
            return i
        else:
            return url.string
    
    print("error: please check your url, make sure it starts with http:// or https://")
    return None

if len(sys.argv) == 1:
    printHelp(name,version)
    sys.exit()

else:
    if len(sys.argv) > 1 and getOptions()!= None:
        # print help
        if '-h' in getOptions():
            printHelp(name,version)
        
        # print single option info
        elif '-h' not in getOptions():
            # print version
            if '-v' in getOptions():
                printVersion(name,version)
        
            #elif '-s' in getOptions():

            #elif '-p' in getOptions():
    elif len(sys.argv) > 1:
        if getUrl() != None:
            doDownloadFile(str(getUrl()),None)
        #if getPath() != None:

    else: 
        printError(name)
