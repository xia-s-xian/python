#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#pysvn 参考Url：http://pysvn.tigris.org/docs/pysvn_prog_ref.html#pysvn_revision

import pysvn
import time

client = pysvn.Client()

#check out the current version of the pysvn project

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

##默认情况下，版本设置为1，则pysvn将checkout svn 最新得版本，如果指定版本，checkou指定版本
rev_top_bt = 1
rev_dsp = 1
rev_mpflash3_0 = 1
rev_bluetunes = 1
rev_dsp_tools = 1 
rev_demoEQ = 1
rev_eck = 1

def svn_updata():
    rev=pysvn.Revision(pysvn.opt_revision_kind.number,3832)
    client.update(path,revision=rev)

def svn_checkout(url,path,rev=1):

    rev_num=pysvn.Revision( pysvn.opt_revision_kind.number, rev )
    rev_head=pysvn.Revision(pysvn.opt_revision_kind.head)

    if(rev!=1)
        rev=rev_num
    else:
        rev=rev_head
    
    client.checkout(url,path,revision=rev)

def svn_checkout_mod():
    svn_checkout(url_top_bt,path_top_bt，rev_top_bt)
  #  get_info(url_top_bt,3861)
    print("checkout multicor end\n")
    
    svn_checkout(url_dsp,path_dsp，rev_dsp)
  #  get_info(url_dsp,3778)
    print("checkout dsp end\n")
    
    svn_checkout(url_mpflash3_0,path_mpflash3_0，rev_mpflash3_0)
 #   get_info(url_mpflash3_0,3818)
    print("checkout url_mpflash3_0 end\n")
    
    svn_checkout(url_bluetunes,path_bluetunes，rev_bluetunes)
  #  get_info(url_bluetunes,3849)
    print("checkout url_bluetunes end\n")
    
    svn_checkout(url_dsp_tools,path_dsp_tools，rev_dsp_tools)
 #   get_info(url_dsp_tools,3361)
    print("checkout url_dsp_tools end\n")
    
    svn_checkout(url_demoEQ,path_demoEQ，rev_demoEQ)
 #   get_info(url_demoEQ,2986)
    print("checkout url_demoEQ end\n")
      

def get_info(url,rev):
   revision=pysvn.Revision(pysvn.opt_revision_kind.head)
   end=pysvn.Revision(pysvn.opt_revision_kind.number,rev)
   log_messages = client.log(url, revision_start=revision, revision_end=end,
        limit=0)
   for log in log_messages:
       timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.date))
       print ('[%s]\t%s\t%s\n  %s\n' % (log.revision.number, timestamp,
            log.author, log.message))
       
def revert_svn_ver(path_dir):
    client.revert(path_dir,recurse=True)

def clean_up_svn():
    client.cleanup(path,fix_recorded_timestamps=True, clear_dav_cache =True,vacuum_pristines=True, include_externals=True)

def revert_svn_mod():
    revert_svn_ver(path_top_bt)
    revert_svn_ver(path_dsp)
    revert_svn_ver(path_mpflash3_0)
    revert_svn_ver(path_bluetunes)
    revert_svn_ver(path_dsp_tools)
    revert_svn_ver(path_demoEQ)

print
if __name__=="__main__":
   # revert_svn_mod()
    svn_checkout_mod()
   # get_info()
   # revert_svn_ver(path_top_bt)
   
    print("END")
    
   
