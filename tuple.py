#!/usr/bin/env python3
# -*- coding:utf-8 -*-

url_top_bt='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'
url_dsp='http://10.0.2.88/svn/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'
url_mpflash3_0='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0'
url_bluetunes='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638'
url_dsp_tools='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DSPTool'
url_demoEQ='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ'
url_eck='http://10.0.2.88/svn/VimcBT/VA9638B/ECK/Tri-Mode'

##默认情况下，版本设置为1，则pysvn将checkout svn 最新得版本，如果指定版本，checkou指定版本
rev_top_bt = 1
rev_dsp = 1
rev_mpflash3_0 = 1
rev_bluetunes = 1
rev_dsp_tools = 1 
rev_demoEQ = 1
rev_eck = 1

tuple=(url_top_bt,rev_top_bt, \
       url_dsp,rev_dsp,\
       url_mpflash3_0,rev_mpflash3_0, \
       url_bluetunes,rev_bluetunes,  \
       url_dsp_tools,rev_dsp_tools,\
       url_demoEQ,rev_demoEQ,\
       url_eck,rev_eck\
       )

if __name__=="__main__":
    print(tuple)
