#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os,platform, re
import zipfile, time

def zipDir(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()

#解压
def read_zip_file(pathzip,pathout):
    z = zipfile.ZipFile(pathzip, 'r')
    z.extractall(pathout)
    z.close()
    

if __name__=="__main__":

    dir="D:/4_ZGW/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain"
    out='D:/4_ZGW/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'+".zip"

    zipDir(dir,out)
    
    #read_zip_file(out,dir)
