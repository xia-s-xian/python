#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import stat
import datetime,platform
import schedule,time
import shutil

sys.path+=["./Module"]

import checkout_ver as checkout
import build as build_target_set
import SDK_generate as sdk_generate
import svn_deal as delete_svn_folder

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


##默认情况下，版本设置为None，则pysvn将checkout svn 最新得版本，如果指定版本，checkou指定版本
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
path_dfu_fro_4M ="./check_out_code/MPFlashTool_dfu_for_4M"
path_sp_test_tool ="./check_out_code/SPTestTool2.0"

absolutPath_svn=r"../check_out_code/VA9638B_V8000_MultiCore"
multi_svn = os.path.abspath(absolutPath_svn)




#路径版本配置
tuple=(url_top_bt,rev_top_bt,path_top_bt, \
       url_dsp,rev_dsp,path_dsp, \
       url_mpflash3_0,rev_mpflash3_0,path_mpflash3_0 , \
       url_bluetunes,rev_bluetunes,path_bluetunes,  \
       url_dsp_tools,rev_dsp_tools,path_dsp_tools,\
       url_demoEQ,rev_demoEQ,path_demoEQ,\
       url_eck,rev_eck,path_eck,\
       )


            

def delete_temp_checkout():
    top="../check_out_code/va9638b"
    multi_core="../check_out_code/VA9638B_V8000_MultiCore"
    multi_core_svn="C:/Users/DELL/Desktop/python/check_out_code/VA9638B_V8000_MultiCore"
    if os.path.exists(top):   # 判断存在
       shutil.rmtree(top)
    
    print(multi_svn)                     
    delete_svn_folder.FindSvnDir(multi_svn)
    
    if os.path.exists(multi_core):
       shutil.rmtree(multi_core)

def delete_sdk_svn_info():
    print("a")
    #delete_svn_folder.FindSvnDir()
    #delete_svn_folder.FindSvnDir()


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

schedule.every().day.at("9:08").do(run_task)


#注意：程序在执行的时候，相关文件和文件夹需要关闭，否则会失败
if __name__=="__main__":
    #delete_temp_checkout()
    run_task()
    #every_day()
    

    

