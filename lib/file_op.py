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
#delet folder
#os.remove(path) 删除文件
#path="文件路径"
#shutil.rmtree(path)

#--------------------------------------------------------------------------#

if __name__ == "__main__":
