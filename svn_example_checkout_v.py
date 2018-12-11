#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pysvn
import time

client = pysvn.Client()


#check out the current version of the pysvn project

svn_file=3844

svn_url='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'

muli_core='F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore'
dsp='D:/4_ZGW/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'

work_path = 'F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore'
url='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/branches/VA9638B_V8009_UI'

path='C:/Users/DELL/Desktop/VA9638B_V8000_MultiCore'


url_top_bt='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'
url_dsp='http://10.0.2.88/svn/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'
url_mpflash3_0='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0'
url_bluetunes='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638'
url_dsp_tools='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DSPTool'
url_demoEQ='http://10.0.2.88/svn/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ'
url_eck='http://10.0.2.88/svn/VimcBT/VA9638B/ECK/Tri-Mode'

path_top_bt='F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore'
path_dsp='D:/4_ZGW/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'
path_mpflash3_0='D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/MPFlashTool/V3.0'
path_bluetunes='D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/ImageExplorer/For 9638'
path_dsp_tools='D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/DSPTool'
path_demoEQ='D:/4_ZGW/VimcBT/Hawkeye/trunk/Release/MPTool/DemoEQ'
path_eck='D:/4_ZGW/VimcBT/VA9638B/ECK/Tri-Mode/'

def svn_updata():
    rev=pysvn.Revision(pysvn.opt_revision_kind.number,3832)
    client.update(path,revision=rev)

def svn_checkout():
    client.checkout(url_mpflash3_0,
    path_mpflash3_0,revision=pysvn.Revision(pysvn.opt_revision_kind.head))

def svn_checkout_bluetunes():
    client.checkout(url_bluetunes,
    path_bluetunes,revision=pysvn.Revision(pysvn.opt_revision_kind.head))

def svn_checkout_dsp_tools():
    client.checkout(url_dsp_tools,
    path_dsp_tools,revision=pysvn.Revision(pysvn.opt_revision_kind.head))

def svn_checkout_demoEQ():
    client.checkout(url_demoEQ,
    path_demoEQ,revision=pysvn.Revision(pysvn.opt_revision_kind.head))
    

def get_info():
   revision=pysvn.Revision(pysvn.opt_revision_kind.head)
   end=pysvn.Revision(pysvn.opt_revision_kind.number,2986)
   log_messages = client.log(url_demoEQ, revision_start=revision, revision_end=end,
        limit=0)
   for log in log_messages:
       timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.date))
       print ('[%s]\t%s\t%s\n  %s\n' % (log.revision.number, timestamp,
            log.author, log.message))
print
if __name__=="__main__":
    svn_checkout_dsp_tools()
    get_info()
