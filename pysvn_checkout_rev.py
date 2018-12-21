#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pysvn
import time

client = pysvn.Client()

reversion=1   #1 为更新到最新版本

def svn_checkout(url,path,rev=1):

    rev_num=pysvn.Revision( pysvn.opt_revision_kind.number, rev )
    rev_head=pysvn.Revision(pysvn.opt_revision_kind.head)
    
    if(rev!=1):
        rev=rev_num
    else:
        rev=rev_head
    
    client.checkout(url,path,revision=rev)

if __name__=="__main__":
    
    path='C:/Users/DELL/Desktop/VA9638B_V8000_MultiCore'
    url_top_bt='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'
    svn_checkout(url_top_bt,path,reversion)
