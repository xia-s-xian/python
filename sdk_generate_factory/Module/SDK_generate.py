#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import operator as op
import shutil                           #高级文件操作，主要用来文件的复制
#shutil.copy(s,d)  s:源文件  d:目标文件
sys.path+=["./Module"]
import ReleaseMCUTop as get_top
import zipfile

def mkdir(path):
    folder=os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("new foldr "+path)
    else:
        print("This floder is exit")

def rmfile(path):
   os.rmdir(path)                         #删除文件夹

def cp_f(c, t):
    # 自己写遍历并且一个个cp
    dir_list = os.listdir(c)
    for f in dir_list:
        file_path = c + '/' + f
        if os.path.isdir(file_path):
            continue   # 跳过文件夹
        shutil.copy(file_path, t)

def fun_make_release_file(file_dir):

    targetpath="../SDK/"+file_dir   #模块在被调用是  “../”代表的是最先python程序运行所处的文件目录的上一级
    
    mkdir(targetpath)                           #创建新的文件夹
    
    file1 = targetpath+"/Code_Image"
    mkdir(file1)
   
    file2 = targetpath+"/Code_SRC"
    mkdir(file2)
    file3 = targetpath+"/Code_SRC/DSP"
    mkdir(file3)
    file4 = targetpath+"/Code_SRC/MCUTOP"
    mkdir(file4)
    file5 = targetpath+"/ECK_Image"
    mkdir(file5)
    file6 =targetpath+"/Tools"
    mkdir(file6)
    file7 = targetpath+"/Tools"
    mkdir(file7)
    file8 = targetpath+"/doc"
    mkdir(file8)
    ''' 
    rep_s="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/Public file/VA9638B Release Test_12_x.xlsx"
    
    rep_temp="F:/8.ZGW/4_VA9638项目/18_集成发布/daily_build_note/"
   # print(file_s[5:9])
    rep_d=rep_temp+file_dir+"/VA9638B Release Test_"+file_dir[5:10]+".xlsx"
    shutil.copy(rep_s,rep_d)
    '''
    print("MAKE FILES END")

def fun_copy_image(file_dir):
    
    top_s="../check_out_code/VA9638B_V8000_MultiCore/coretop/output/va9638b_top_Release/binary/va9638b_top.bin"
    image_d="../SDK/"+file_dir+"/Code_Image"
    shutil.copy(top_s,image_d)

    bt_s="../check_out_code/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release/binary/va9638b_bt_release_en.bin"
    shutil.copy(bt_s,image_d)

    sec_release_s="../check_out_code/VA9638B_V8000_MultiCore/SecureFlashBootloader/output/SecureFlashBootloader_release/binary/SecureFlashBootloader_release.bin"   
    shutil.copy(sec_release_s,image_d)

    sec_debug_s="../check_out_code/VA9638B_V8000_MultiCore/SecureFlashBootloader/output/SecureFlashBootloader_debug/binary/SecureFlashBootloader_debug.bin"   
    shutil.copy(sec_debug_s,image_d)

    mass_pro_s="../check_out_code/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_mass_pro/binary/va9638b_bt_mass_pro_en.bin"
    shutil.copy(mass_pro_s,image_d)
    
    old_mass_pro_name="../SDK/"+file_dir+"/Code_Image/va9638b_bt_mass_pro_en.bin"
    new_mass_pro_name="../SDK/"+file_dir+"/Code_Image/ExtFlash.bin"
    os.rename(old_mass_pro_name,new_mass_pro_name)

#copy debug_info
    cDir="../check_out_code/VA9638B_V8000_MultiCore/corebt/output/va9638b_bt_release/debuginfo"
    tDir="../SDK/"+file_dir+"/Code_Image/debuginfo"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在

    print("COPY IMAGE END")
    
def fun_cp_files(file_dir):
   
    cDir="../check_out_code/MPFlashTool"
    tDir="../SDK/"+file_dir+"/Tools/MPFlashTool3.0"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
       
    cDir="../check_out_code/For 9638"
    tDir="../SDK/"+file_dir+"/Tools/For 9638"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    des="../SDK/"+file_dir+"/Tools/BlueTones"  #重命名  
    os.rename(tDir,des) 

    cDir="../check_out_code/DemoEQ"
    tDir="../SDK/"+file_dir+"/Tools/DemoEQ"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="../check_out_code/DSPComposite"
    tDir="../SDK/"+file_dir+"/Tools/DSPComposite"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="../check_out_code/DSPComposite"
    tDir="../SDK/"+file_dir+"/Tools/DSPComposite"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="../check_out_code/MPFlashTool_dfu_for_4M"
    tDir="../SDK/"+file_dir+"/Tools/MPFlashTool_dfu_for_4M"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    cDir="../check_out_code/SPTestTool2.0"
    tDir="../SDK/"+file_dir+"/Tools/SPTestTool2.0"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录

    '''
    cDir="../check_out_code/Public file/doc"
    tDir="../SDK/"+file_dir+"/doc"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
        # shutil.copy(cDir, tDir)     # 不能copy目录
    '''
    print("Copy TOOLS END")
        
def fun_cp_eck(file_dir):
    
    cDir="../check_out_code/ECK"
    tDir="../SDK/"+file_dir+"/Eck_Image"
    if os.path.exists(tDir):   # 判断存在
        cp_f(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在

    print("Copy ECK END")

def unzip_file_fun(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')
        
    print("---unzip end----")

def zip_file(src_dir):
    zip_name = src_dir +'.zip'
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('==压缩成功==')
    z.close()


def get_top_src(file_dir):
    #releas_top_path="../check_out_code/VA9638B_V8000_MultiCore/coretop/ReleaseMCUTop.py"
    file_path = r"../check_out_code/VA9638B_V8000_MultiCore/coretop/va9638b_top.uvproj"
    get_top.get_top_src_main(file_path)

    #zip_path = r"../check_out_code/va9638br_coretop_20181225194419.zip"
    unzip_path=r"../check_out_code"
    
    unzip_file=r"../check_out_code"
    for files in unzip_file:
        if(op.eq(files,"va9638b")):
            shutil.rmtree(unzip_file+"va0638b")

    zip_name="va9638br"
    listfile=os.listdir(r"../check_out_code")
    for names in listfile:
        if(op.eq(names[0:8],zip_name)):
            zip_path_file=unzip_path+"/"+names
            print(zip_path_file)
            unzip_file_fun(zip_path_file,unzip_path)

    cDir="../check_out_code/va9638b"
    tDir="../SDK/"+file_dir+"/Code_SRC/MCUTOP"
    if os.path.exists(tDir):   # 判断存在
        os.rmdir(tDir)
        shutil.copytree(cDir, tDir)
    else:
        shutil.copytree(cDir, tDir)   # 目标文件夹必须不存在
 
    for names in listfile:
        if(op.eq(names[0:8],zip_name)):
            zip_path_file=unzip_path+"/"+names
            os.remove(zip_path_file)
        
def get_dsp_src(file_dir):
    #zip_dsp_path=r"../check_out_code/BTAudio_Digitalgain"  
    #zip_file(zip_dsp_path)

    dsp_s="../check_out_code/BTAudio_Digitalgain"
    dsp_d="../SDK/"+file_dir+"/Code_SRC/DSP/BTAudio_Digitalgain"
    shutil.copy(dsp_s,dsp_d)

    

    os.remove(dsp_s)

def SDK_generate_main(daily_file_dir):
    fun_make_release_file(daily_file_dir)    #创建文件夹
    fun_copy_image(daily_file_dir)           #复制image
    fun_cp_files(daily_file_dir)             #拷贝tools
    fun_cp_eck(daily_file_dir)               #拷贝eck

    get_top_src(daily_file_dir)              #获得top_source
    get_dsp_src(daily_file_dir)              #获得dsp_source
   
     
if __name__=="__main__":
    #fun_make_release_file()

    file=os.path.abspath('.')             #擦看当前路径
    print(file)
    
