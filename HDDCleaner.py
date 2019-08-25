import pathlib #filepathing
import glob #merging files
import os #deleting files
global sDir
###

class Projects:
    def __init__(Paths, dicProjects = {
        }): 
         Paths.dicProjects = dicProjects
         
    # getter method 
    def get_dictionary(Paths): 
        return Paths.dicProjects 
      
    # setter method 
    def set_dictionary(Paths, x): 
        Paths.dicProjects = x 

def DeleteFiles(sPath, aExtensions):
    for sPathAndFilename in glob.iglob(os.path.join(sPath, aExtensions)):
        print(sPathAndFilename)
        x = raw_input("sd")
        os.remove(sPathAndFilename)
    DeleteEmptyDirectory(sPath)

###
def PathThroughHDD(lFileList, sDir = os.getcwd()):
        sNewDefaultPath = ""
        for y in lFileList:
            for sPathAndFilename in glob.iglob(os.path.join(sDir, y)):
                sNewDefaultPath = sPathAndFilename
                if "Tech" in y or "TECH" in y:
                    FindProjects(y, sNewDefaultPath)
                try:
                    sD = os.listdir(sPathAndFilename)
                    PathThroughHDD(sD, sNewDefaultPath)
                except:
                    continue
                
        return
 
###
def FindProjects(key, Path):
    print(Path)
    dicProj = Projects()
    dicToAppend = dicProj.get_dictionary()
    sKeyNew = ""
    iIndexNumber = 0
    if "Tech" in key or "TECH" in key:
        sKeyNew = "Tech"
        if key.find(sKeyNew) == -1:
            sKeyNew = "TECH"
        iIndexNumber = key.find(sKeyNew)
        z = iIndexNumber - 1
        while z != -1:
            if key[z].isalpha():
                sKeyNew = key[z] + sKeyNew
            z = z - 1
        z = iIndexNumber + 4
        while z < len(key) -1:
            if key[z].isalpha():
                sKeyNew = sKeyNew + key[z]
            z = z + 1
        if sKeyNew in dicToAppend:
            aNewValue = dicToAppend.get(sKeyNew)
            aNewValue.append(Path)
            dicToAppend[sKeyNew] = aNewValue
            dicProj.set_dictionary(dicToAppend)
        else:
            dicToAppend[sKeyNew] = [Path]
            dicProj.set_dictionary(dicToAppend)
    dicToAppend = dicProj.get_dictionary()
    return        

def DeleteEmptyDirectory(sPath):
    try:
        os.rmdir(sPath)
    except:
        print(sPath + ": is not empty.")

sDir = os.getcwd()
lFileList = os.listdir(sDir)
PathThroughHDD(lFileList)

dicProj = Projects()
dicToAppend = dicProj.get_dictionary()
print(dicToAppend)

f = open('HardDriveFiles.txt','w')
for key, val in dicToAppend.items():
    stringx = key + ":" + "\n"
    stringy = val
    f.write(stringx)
    f.write(''.join(val))
    f.write("\n")
f.close()
