#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import stat
import datetime,platform
import schedule,time
import shutil

#sys.path+=["./Module"]
#sys.path+=["../SDK_generate_factory"]

#import svn_deal as detl

from Module import * 

#import checkout_ver_ver as checkout_ver
#import build as build
#import SDK_generate as SDK_generate
#import svn_deal as svn_deal

#sys.path.append(r"../check_out_code/VA9638B_V8000_MultiCore/tools/build.py")


url_top_bt='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'
url_dsp='http://10.0.2.88/svn/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'
url_mpflash3_0='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0'
url_bluetunes='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638'
url_dsp_tools='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DSPTool'
url_demoEQ='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ'
url_eck='http://10.0.2.88/svn/VimcBT/VA9638B/ECK/Tri-Mode'

url_dsp_comp="http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DSPTool"
url_dfu_fro_4M = "http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0_dfu_for_4M"
url_sp_test_tool="http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/SPTestTool2.0"


##默认情况下，版本设置为None，则pysvn将checkout_ver svn 最新得版本，如果指定版本，checkou指定版本
rev_top_bt = None
rev_dsp = None
rev_mpflash3_0 = None
rev_bluetunes = None
rev_dsp_tools = None 
rev_demoEQ = None
rev_eck = None

rev_dsp_comp = None
rev_dfu_fro_4M = None
rev_sp_test_tool= None

path_top_bt="../check_out_code/VA9638B_V8000_MultiCore"
path_dsp="../check_out_code/BTAudio_Digitalgain"
path_mpflash3_0="../check_out_code/MPFlashTool"
path_bluetunes="../check_out_code/For 9638"
path_dsp_tools="../check_out_code/DSPTool"
path_demoEQ="../check_out_code/DemoEQ"
path_eck="../check_out_code/ECK"

path_dspcomp="../check_out_code/DSPComposite"
path_dfu_fro_4M ="../check_out_code/MPFlashTool_dfu_for_4M"
path_sp_test_tool ="../check_out_code/SPTestTool2.0"

absolutPath_svn=r"../check_out_code/VA9638B_V8000_MultiCore"
absolutPath = os.path.abspath(absolutPath_svn)

#absolutPath_svn


#路径版本配置
tuple=(url_top_bt,rev_top_bt,path_top_bt, \
       url_dsp,rev_dsp,path_dsp, \
       url_mpflash3_0,rev_mpflash3_0,path_mpflash3_0 , \
       url_bluetunes,rev_bluetunes,path_bluetunes,  \
       url_dsp_tools,rev_dsp_tools,path_dsp_tools,\
       url_demoEQ,rev_demoEQ,path_demoEQ,\
       url_eck,rev_eck,path_eck,\
       url_dsp_comp,rev_dsp_comp,path_dspcomp,\
       url_dfu_fro_4M,rev_dfu_fro_4M,path_dfu_fro_4M,\
       url_sp_test_tool,rev_sp_test_tool,path_sp_test_tool,\
       )


            

def delete_temp_checkout_ver():
    top="../check_out_code/va9638b"
    multi_core="../check_out_code/VA9638B_V8000_MultiCore"
    multi_core_svn="C:/Users/DELL/Desktop/python/check_out_code/VA9638B_V8000_MultiCore"
    if os.path.exists(top):   # 判断存在
       shutil.rmtree(top)
    
    #print(multi_svn)                     
    svn_deal.FindSvnDir(absolutPath)
    svn_deal.FindSvnDir(absolutPath)
    if os.path.exists(multi_core):
       shutil.rmtree(multi_core)

def delete_sdk_svn_info( ):
    #print("a")
    file_dir="2019-01-19"
    mp="../SDK/"+file_dir+"/Tools/MPFlashTool3.0"
    mp = os.path.abspath(mp)
    print(mp)
    svn_deal.FindSvnDir(mp)
    
    bluetoooth="../SDK/"+file_dir+"/Tools/BlueTones"
    bluetoooth = os.path.abspath(bluetoooth)
    svn_deal.FindSvnDir(bluetoooth)
    
    demoeq="../SDK/"+file_dir+"/Tools/DemoEQ"
    demoeq = os.path.abspath(demoeq)
    svn_deal.FindSvnDir(demoeq)
    
    svn_deal.FindSvnDir(demoeq)
    dsp_composite="../SDK/"+file_dir+"/Tools/DSPComposite"
    svn_deal.FindSvnDir(dsp_composite)
    dfu_for_4M="../SDK/"+file_dir+"/Tools/MPFlashTool_dfu_for_4M"
    svn_deal.FindSvnDir(dfu_for_4M)
    sptest="../SDK/"+file_dir+"/Tools/SPTestTool2.0"
    svn_deal.FindSvnDir(sptest)
    #svn_deal.FindSvnDir()


def generate_sdk(file_daily):
    
    delete_temp_checkout_ver()
    
    checkout_ver.check_out_handle(tuple)
    print("-----checkout_ver end--------")
 
    root_dir=r".."
    build.build_target(path_top_bt)
    print("-----build end--------")

    SDK_generate.SDK_generate_main(file_daily)

    #delete_sdk_svn_info(file_daily)
    
    print("-----SDK generate end--------")
    now = datetime.datetime.now()
    print(now)

    input()
    
def run_task():
    now = datetime.datetime.now()
    print(now)
    now_string=str(now)
    file_name=now_string[0:18]
    file_name1=file_name.replace(" ","_")
    file_name2=file_name1.replace(":","_")
    
    generate_sdk(file_name2)

def every_day(): 
    while True:
        schedule.run_pending()
        time.sleep(1)

#schedule.every().day.at("9:00").do(run_task)
#schedule.every().day.at("10:50").do(run_task)
schedule.every().day.at("11:00").do(run_task)
#schedule.every().day.at("16:18").do(run_task)

#注意：程序在执行的时候，相关文件和文件夹需要关闭，否则会失败
if __name__=="__main__":
    #delete_temp_checkout_ver()
    run_task()
    #every_day()
    #delete_sdk_svn_info()
