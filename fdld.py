import urllib.request
import urllib
import sys, os
def printError(name):
    print ("error: try '"+str(name)+" -h' to get some help")
def printVersion(name,version):
    print ("software "+str(name)+", version "+str(version))

def printHelp(name,version):
    authorinfo = "\ncreated by tianqi qin, started on 3nd June in 2018\nsoftware "+str(name)+", version "+str(version) 
    print ("Usage: \n\t"+str(name)+" [option] <url> \n" +
            "\n" + 
            "Options: \n"+
            "\t-v,-version \tprint version of "+str(name)+"\n"+
            "\t-h,-help    \tprint help information about how to use " + str(name) + "\n" +
            authorinfo)

def doSetDownloadPath(argvs):
    return True


def doDownloadFile(url,name):
    def callbackdownload(blocknum,blocksize,totalsize):
        per = 100.0*blocknum*blocksize/totalsize
        if per > 100.0:
            per = 100.0
        print ('\r',"downloading...["+str(int(per) * '=')+"]","%.2f"%per,end='%')  
    try: 
        pwd = os.getcwd()
        print (pwd)
        filename = os.path.basename(url)
        urllib.request.urlretrieve(url,pwd + "\/" + filename,callbackdownload)
    except:
        print ("\nerror: download falied! netword lost or not standard")