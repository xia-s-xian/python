#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import operator as op
import shutil                           #高级文件操作，主要用来文件的复制
#shutil.copy(s,d)  s:源文件  d:目标文件

file_dir="2018_12_21"

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


def cp_f(c, t):
    # 自己写遍历并且一个个cp
    dir_list = os.listdir(c)
    for f in dir_list:
        file_path = c + '/' + f
        if os.path.isdir(file_path):
            continue   # 跳过文件夹
        shutil.copy(file_path, t)

def fun_make_release_file():

    mkdir(file_dir)                           #创建新的文件夹
    
    file1 = file_dir+"/Code_Image"
    mkdir(file1)
   
    file2 = file_dir+"/Code_SRC"
    mkdir(file2)
    file3 = file_dir+"/Code_SRC/DSP"
    mkdir(file3)
    file4 = file_dir+"/Code_SRC/MCUTOP"
    mkdir(file4)
    file5 = file_dir+"/ECK"
    mkdir(file5)
    file6 =file_dir+"/Tools"
    mkdir(file6)
    file7 = file_dir+"/Tools"
    mkdir(file7)
    

    
    '''
    file = "2018_12_7"
    mkdir(file)                           #创建新的文件夹
    
    file = "2018_12_7/Code_Image"
    mkdir(file)
    
    file = "2018_12_7/Code_SRC"
    mkdir(file)
    file = "2018_12_7/Code_SRC/DSP"
    mkdir(file)
    file = "2018_12_7/Code_SRC/MCUTOP"
    mkdir(file)
    file = "2018_12_7/ECK"
    mkdir(file)
    file = "2018_12_7/Tools"
    mkdir(file)
    file = "2018_12_7/Tools"
    mkdir(file)
    '''
    rep_s="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/Public file/VA9638B Release Test_12_x.xlsx"
    
    rep_temp="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"
   # print(file_s[5:9])
    rep_d=rep_temp+file_dir+"/VA9638B Release Test_"+file_dir[5:10]+".xlsx"
    shutil.copy(rep_s,rep_d)

    print("MAKE FILES END")

def fun_copy_image():
    
    top_s="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/coretop/output/va9638b_top_release_Release/binary/va9638b_top_release.bin"
    top_d="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/Code_Image"
    shutil.copy(top_s,top_d)

    bt_s="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release_Release/binary/va9638b_bt_release_en.bin"
    shutil.copy(bt_s,top_d)

#    sec_s="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/SecureFlashBootloader/output/"
#    file_sec="ecureFlas"
#    fiel_end="/binary/SecureFlashBootloader.bin"
#    listfile=os.listdir(sec_s)
#    for name in listfile:
#       if op.eq(name[0:10],file_sec):
#            sec_all=sec_c+name+fiel_end
#            print(sec_all)

    file_a="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/SecureFlashBootloader/output/"   
    file_sec="secureFlas"
    fiel_end="/binary/SecureFlashBootloader.bin"
    
    file_b="/bin"
    file_sec="SecureFlas"
    file_c=file_a+file_b;
    print(file_c);

    listfile=os.listdir(file_a)
    for name in listfile:
#        print(type(name))                 #打印数据类型
#        print(name[0:10])                 #使用切片 提取字符串指定数据个数，打印
        if op.eq(name[0:10],file_sec):
            sec_c=file_a+name+fiel_end
            shutil.copy(sec_c,top_d)  
            print(sec_c)
    else:
        print("end")
        
#    SecureFlashBootloader_Release_20181207_144505/binary/SecureFlashBootloader.bin
#    shutil.copy(sec_s,top_d)       
#    bt_Ms="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release_Release/binary/va9638b_bt_release_en(MS).bin"
#    shutil.copy(bt_Ms,top_d)


#copy debug_info
    cDir="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release_Release/debuginfo"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/Code_Image/debuginfo"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在

    print("COPY IMAGE END")
    


def fun_cp_files():
   
    cDir="D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/Tools/MPFlashTool3.0"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
       
    cDir="D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/Tools/For 9638"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/Tools/DemoEQ"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录


    cDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/Public file/doc"
    tDir="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/doc"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    print("Copy TOOLS END")
        
def fun_cp_eck():
    
#    top_s="D:/4_ZGW/VimcBT/VA9638B/ECK/Tri-Mode/9638B_6_8_ECK_TriCore_TriMode_V0.2.7_singlelink.vfi"
#    top_d="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/ECK"
#    shutil.copy(top_s,top_d)

    top_s="D:/4_ZGW/VimcBT/VA9638B/ECK/Tri-Mode/9638B_6_8_ECK_TriCore_TriMode_V0.2.8_multilink.vfi"
    top_d="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"+file_dir+"/ECK"
    shutil.copy(top_s,top_d)

    print("Copy ECK END")
     
if __name__=="__main__":
 #   fun_make_release_file()
  
 #   fun_copy_image()
    fun_cp_files()
    fun_cp_eck()

    file=os.path.abspath('.')             #擦看当前路径
    print(file)
    
