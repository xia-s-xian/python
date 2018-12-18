#/usr/bin/env python3
# -*- coding:utf-8 -*-

#之前测试无法还原的问题，通过重启电脑得以解决

import pysvn
import time

client = pysvn.Client()

path='C:/Users/DELL/Desktop/VA9638B_V8000_MultiCore'

def revert_svn_ver(path_dir):
    client.revert(path_dir,recurse=True)

if __name__=="__main__":
    revert_svn_ver(path)
