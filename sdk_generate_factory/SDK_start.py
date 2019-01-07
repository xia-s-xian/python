#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import datetime,platform
import schedule,time
import shutil
sys.path+=["./Module"]

import checkout_ver as checkout 
import build as build_target_set
import SDK_generate as sdk_generate
#sys.path.append(r"../check_out_code/VA9638B_V8000_MultiCore/tools/build.py")


url_top_bt='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'
url_dsp='http://10.0.2.88/svn/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'
url_mpflash3_0='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0'
url_bluetunes='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638'
url_dsp_tools='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DSPTool'
url_demoEQ='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ'
url_eck='http://10.0.2.88/svn/VimcBT/VA9638B/ECK/Tri-Mode'

##默认情况下，版本设置为None，则pysvn将checkout svn 最新得版本，如果指定版本，checkou指定版本
rev_top_bt = None
rev_dsp = None
rev_mpflash3_0 = None
rev_bluetunes = None
rev_dsp_tools = None 
rev_demoEQ = None
rev_eck = None

path_top_bt="../check_out_code/VA9638B_V8000_MultiCore"
path_dsp="../check_out_code/BTAudio_Digitalgain"
path_mpflash3_0="../check_out_code/MPFlashTool"
path_bluetunes="../check_out_code/For 9638"
path_dsp_tools="../check_out_code/DSPTool"
path_demoEQ="../check_out_code/DemoEQ"
path_eck="../check_out_code/ECK"

#路径版本配置
tuple=(url_top_bt,rev_top_bt,path_top_bt, \
       url_dsp,rev_dsp,path_dsp, \
       url_mpflash3_0,rev_mpflash3_0,path_mpflash3_0 , \
       url_bluetunes,rev_bluetunes,path_bluetunes,  \
       url_dsp_tools,rev_dsp_tools,path_dsp_tools,\
       url_demoEQ,rev_demoEQ,path_demoEQ,\
       url_eck,rev_eck,path_eck,\
       )


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
                  delDirNameTemp = os.path.join(absolutPath, root)
                  delDirName = os.path.join(delDirNameTemp, dirName)
                  #print (delDirName)
                  DeleteSvnDir(delDirName)
            # 这里不用递归调用函数，因为os.walk函数就递归遍历了所有文件和文件夹
            #else :
                #FindSvnDir(dirName)
            

def delete_temp_checkout():
    top="../check_out_code/va9638b"
    multi_core="../check_out_code/VA9638B_V8000_MultiCore"
    multi_core_svn="../check_out_code/VA9638B_V8000_MultiCore/.svn"
    if os.path.exists(top):   # 判断存在
       shutil.rmtree(top)

    FindSvnDir(multi_core_svn)
    if os.path.exists(multi_core):
        shutil.rmtree(multi_core)
        
def generate_sdk(file_daily):
    
    delete_temp_checkout()

    checkout.check_out_handle(tuple)
    print("-----checkout end--------")
 
    root_dir=r".."
    build_target_set.build_target(path_top_bt)
    print("-----build end--------")

    sdk_generate.SDK_generate_main(file_daily)
    print("-----SDK generate end--------")

def run_task():
    now = datetime.datetime.now()
    now_string=str(now)
    file_name=now_string[0:10]
    generate_sdk(file_name)

def every_day(): 
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every().day.at("15:40").do(run_task)

if __name__=="__main__":
    #delete_temp_checkout()
    run_task()
    every_day()
    

    

