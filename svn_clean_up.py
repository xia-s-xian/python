#/usr/bin/env python3
# -*- coding:utf-8 -*-



import pysvn
import time

client = pysvn.Client()

path='C:/Users/DELL/Desktop/VA9638B_V8000_MultiCore'

def clean_up_svn():
    client.cleanup(path,fix_recorded_timestamps=True, clear_dav_cache =True,vacuum_pristines=True, include_externals=True)

if __name__=="__main__":
    clean_up_svn()
