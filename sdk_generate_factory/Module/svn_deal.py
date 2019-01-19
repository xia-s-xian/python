import os

#absolutPath_svn=r"../check_out_code/VA9638B_V8000_MultiCore"
#absolutPath = os.path.abspath(absolutPath_svn)


def DeleteSvnDir(delDirName):

    if os.path.isfile(delDirName):
        try :
            #print (delDirName)
            # 如果文件是只读类型，会弹出[WinError 5] 拒绝访问，所以修改文件的类型
            os.chmod(delDirName, stat.S_IWRITE )
            os.remove(delDirName)
        except:
            pass
    elif os.path.isdir(delDirName):
        for item in os.listdir(delDirName):
            itemsrc = os.path.join(delDirName, item)
            DeleteSvnDir(itemsrc)
        try:
            os.rmdir(delDirName)
            #print (delDirName)
        except:
            #print (delDirName)
            pass       

def FindSvnDir(OrginPath):
    
     for root, dirs, fileNames in os.walk(OrginPath):

        for dirName in dirs:
            if dirName == ".svn":
                  delDirNameTemp = os.path.join(OrginPath, root)
                  delDirName = os.path.join(delDirNameTemp, dirName)
                  #print (delDirName)
                  DeleteSvnDir(delDirName)
            # 这里不用递归调用函数，因为os.walk函数就递归遍历了所有文件和文件夹
            #else :
                #FindSvnDir(dirName)



if __name__=="__main__":
    FindSvnDir(absolutPath)                        
