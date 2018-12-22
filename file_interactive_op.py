#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys,os
import read_zip_file as zip_op
sys.path.append(r'F:\8.ZGW\4_VA9638项目\18_集成发布\VA9638B_V8000_MultiCore\ReleaseMCUTop(modify).py')
sys.path.append(r'C:\Users\DELL\Desktop\py_test_file\zip_file.py')
'''
问题1：目前代码能够获得top核压缩文件，那么底下如何获得相应路径，并对此解压，
       解压后，又如何获得相应top核代码路径和代码
       解：根据最新的生成zip时间来判断
'''

def get_new_zip_file():
    output_dir=r"F:\8.ZGW\4_VA9638项目\18_集成发布"
    listfile=os.listdir(output_dir)
    for name in listfile:
        print(name)


if __name__=="__main__":
    #print(sys.path)
    #get_new_zip_file()
    #os.system(r"python F:\8.ZGW\4_VA9638项目\18_集成发布\VA9638B_V8000_MultiCore\ReleaseMCUTop(modify).py")
    #os.system(r"C:\Users\DELL\Desktop\py_test_file\zip_file.py")
    zip_src=r"F:\8.ZGW\4_VA9638项目\18_集成发布\va9638br_coretop_20181222152058.zip"
    des_zip_unzip=r'C:\Users\DELL\Desktop\新建文件夹 (2)'
    zip_op.unzip_file(zip_src,des_zip_unzip)
