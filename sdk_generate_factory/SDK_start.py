#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
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

def generate_sdk():

    checkout.check_out_handle(tuple)
    print("-----checkout end--------")
 
    root_dir=r".."
    build_target_set.build_target(path_top_bt)
    print("-----build end--------")

    file_daily="2018_01_03"

    sdk_generate.SDK_generate_main(file_daily)
    print("-----SDK generate end--------")


if __name__=="__main__":
    generate_sdk()

    

