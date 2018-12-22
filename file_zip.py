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
'''
def read_zip_file(pathzip,pathout):
    from zipfile import ZipFile

    file_name = pathzip

    with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
#    zip.printdir()

    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
'''
    
def CopyFileToZip(flist, dpath):

    print("write to ", dpath)
    fzip = zipfile.ZipFile(dpath, 'w')

    fns = [ os.path.abspath(fn)  for fn in flist ]

    print(type(fns))
    
    fns = set(fns)
    
    for src_path in fns:

        if(not os.path.isfile(src_path) ):
            print("not exist:", src_path)
            continue

        dst_path = os.path.relpath(src_path, src_root_dir)
        dst_path = os.path.join("py_test_file", dst_path)
        fzip.write(src_path, dst_path)
        
    fzip.close()
        


if __name__=="__main__":

    dir_s=r"C:\Users\DELL\Desktop\FlashUpgradeTool.zip"
    out='C:/Users/DELL/Desktop/外部flash bin2'+".zip"
    out=r"C:\Users\DELL\Desktop\V3.0.6_20181220.zip"
    testdir=r"C:/Users/DELL/Desktop/FlashUpgradeTool"
    
    src_root_dir = os.path.abspath(testdir)
    
    file_li=[]
    for files in os.listdir(testdir):
        print(files)
        file_path = testdir + r"/" + files
        print(file_path)
        file_li.append(files)
        if os.path.isdir(file_path):
            continue
      
    print(file_li)
    
    CopyFileToZip(file_li,dir_s)
    
'''
    zip = zipfile.ZipFile(dir,"w",zipfile.ZIP_DEFLATED)
    if os.path.isdir(testdir):
        for d in os.listdir(testdir):
            zip.write(testdir+os.sep+d)


    zip.close()
#    zipDir(dir,out)
    
#    read_zip_file(out,out_zip)
'''
