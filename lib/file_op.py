#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#python sorce code:https://github.com/python/cpython/tree/master/Lib

#--------------------------------------------------------------------------#
#Compression（压缩） and decompression（解压缩） folder(文件夹) file（文件）
import os
import shutil
import zipfile
from os.path import join, getsize

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')
        
    print("---unzip end----")

def zip_file(src_dir):
    zip_name = src_dir +'.zip'
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('==压缩成功==')
    z.close()

#--------------------------------------------------------------------------#
#Inter-file function call

import sys
import read_zip_file as zip_op
sys.path.append(r'F:\8.ZGW\4_VA9638项目\18_集成发布\VA9638B_V8000_MultiCore\ReleaseMCUTop(modify).py')
sys.path.append(r'C:\Users\DELL\Desktop\py_test_file\zip_file.py')

zip_src=r"F:\8.ZGW\4_VA9638项目\18_集成发布\va9638br_coretop_20181222152058.zip"
des_zip_unzip=r'C:\Users\DELL\Desktop\新建文件夹 (2)'
zip_op.unzip_file(zip_src,des_zip_unzip)

#--------------------------------------------------------------------------#

if __name__ == "__main__":
    every_day()