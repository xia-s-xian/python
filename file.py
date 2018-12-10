#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import shutil                           #高级文件操作，主要用来文件的复制
#shutil.copy(s,d)  s:源文件  d:目标文件

def mkdir(path):
    folder=os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("new foldr "+path)
    else:
        print("This floder is exit")

def rmfile(path):
   # rm_folder=os.path.exists(path)
   # if rm_folder:
   os.rmdir(path)                         #删除文件夹
   #  print("delet")


def fun_make_release_file():
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7"
    mkdir(file)                           #创建新的文件夹
    
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/Code_Image"
    mkdir(file)
    
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/Code_SRC"
    mkdir(file)
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/Code_SRC/DSP"
    mkdir(file)
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/Code_SRC/MCUTOP"
    mkdir(file)
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/eck"
    mkdir(file)
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/Tools"
    mkdir(file)
    file = "C:/Users/DELL/Desktop/test_file/2018_12_7/Tools/MPFlashTool2.0"
    mkdir(file)

def fun_copy_image():
    top_s="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/coretop/output/va9638b_top_release_Release/binary/va9638b_top_release.bin"
    top_d="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/2018_12_6/Code_Image"
    shutil.copy(top_s,top_d)

    bt_s="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release_Release/binary/va9638b_bt_release_en.bin"
    shutil.copy(bt_s,top_d)

#    sec_s="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/SecureFlashBootloader/output/SecureFlashBootloader_Release_20181206_130121/binary/SecureFlashBootloader.bin"
#    shutil.copy(sec_s,top_d)   
    
#    bt_Ms="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release_Release/binary/va9638b_bt_release_en(MS).bin"
#    shutil.copy(bt_Ms,top_d)


def cp_f(c, t):
    # 自己写遍历并且一个个cp
    dir_list = os.listdir(c)
    for f in dir_list:
        file_path = c + '/' + f
        if os.path.isdir(file_path):
            continue   # 跳过文件夹
        shutil.copy(file_path, t)

def fun_cp_files():
    cDir="D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool2.0"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/2018_12_7/Tools/MPFlashTool2.0"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/2018_12_7/Tools/For 9638"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/2018_12_7/Tools/DemoEQ"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录


    cDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/2018_12_5/doc"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/2018_12_7/doc"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录
        

     
if __name__=="__main__":
    fun_make_release_file()
    fun_copy_image()
    fun_cp_files()

#    file = "2018_12_6/Tools"
#    rmfile(file)

    #fun_copy_image()
    file=os.path.abspath('.')             #擦看当前路径
    print(file)
