#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import shutil
import operator as op

def string_deal():
    file_a="F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore/SecureFlashBootloader/output"
    file_sec="ecureFlas"
    fiel_end="/binary/SecureFlashBootloader.bin"
    
    file_b="/bin"
    file_sec="ecureFlas"
    file_c=file_a+file_b;
    print(file_c);

    listfile=os.listdir(file_a)
    for name in listfile:
        print(type(name))                 #打印数据类型
        print(name[1:10])                 #使用切片 提取字符串指定数据个数，打印
        if op.eq(name[1:10],file_sec):
            sec_c=file_a+name+fiel_end
            print(sec_c)
    else:
        print("end")

if __name__=="__main__":
    string_deal()
   
