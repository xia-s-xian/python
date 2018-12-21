#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys,os
sys.path.append(r'F:\8.ZGW\4_VA9638项目\18_集成发布\VA9638B_V8000_MultiCore\ReleaseMCUTop(modify).py')
'''
问题1：目前代码能够获得top核压缩文件，那么底下如何获得相应路径，并对此解压，
       解压后，又如何获得相应top核代码路径和代码
       解：根据最新的生成zip时间来判断
'''

def get_new_zip_file():
    output_dir=r"F:\8.ZGW\4_VA9638项目\18_集成发布"
    listfile=os.listdir(output_dir)
    for name in listfile:
        print(name)

if __name__=="__main__":
    #print(sys.path)
    #get_new_zip_file()
    os.system(r"python F:\8.ZGW\4_VA9638项目\18_集成发布\VA9638B_V8000_MultiCore\ReleaseMCUTop(modify).py")
