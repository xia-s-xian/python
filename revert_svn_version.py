#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pysvn
import time

client = pysvn.Client()

path='C:/Users/DELL/Desktop/VA9638B_V8000_MultiCore'

def revert_svn_ver():
    client.revert(path,recurse=True)

if __name__=="__main__":
    revert_svn_ver()