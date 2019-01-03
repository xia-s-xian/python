import os
import shutil
import zipfile
from os.path import join, getsize

def unzip_file(zip_src, dst_dir):
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
    
if __name__ == "__main__": 
    des=r'C:\Users\DELL\Desktop\FlashUpgradeTool'
    des_zipa=r'C:\Users\DELL\Desktop\FlashUpgradeTool.zip'
    des_zip_unzip=r'C:\Users\DELL\Desktop\新建文件夹 (2)'
    #zip_file(des)
    unzip_file(des_zipa ,des_zip_unzip)
