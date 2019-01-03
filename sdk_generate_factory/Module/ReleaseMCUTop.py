#!/usr/bin/env python3
## exec by python3

import os,platform, re
import zipfile, time


'''
            <File>
              <FileName>vsys_ipc.c</FileName>
              <FileType>1</FileType>
              <FilePath>..\system\vsys_ipc.c</FilePath>
            </File>
'''

def PlatformAbsPath(p):
    '''return platfrom based path string'''
    if(type(p) != str): return p

    if('inux' in platform.system()):
        p = p.replace("\\", "/")
    elif("indows" in platform.system()):
        p = p.replace("/", "\\")

    if(not os.path.isabs(p)):
        p = os.path.abspath(p)

    p = os.path.normpath(p)

    return p

def KeilProjFiles(UVProjPath, root_path=None, extras=[], excludes=[]):
    '''return files belone to Keil Project
    
    UVProjPath specific the *.uvproj file
    extras   extra files besides UVProj
    excludes specific files by Unix style pathname pattern 
    '''

    import glob, fnmatch
        
    rexs = [re.compile(r"<File>\s*?" +\
              r"<FileName>.+?</FileName>\s*?" +\
              r"<FileType>.+?</FileType>\s*?" +\
              r"<FilePath>(?P<filepath>.+?)</FilePath>\s*?" +\
              r"</File>"),
            re.compile(r"<InitializationFile>(?P<filepath>.+?)</InitializationFile>"),
            re.compile(r"<ScatterFile>(?P<filepath>.+?)</ScatterFile>")
            ]

    proj_dir = os.path.abspath(os.path.dirname(UVProjPath))
    proj_name = os.path.splitext(os.path.basename(UVProjPath))[0]
    proj_path = os.path.abspath(UVProjPath)


    with open(proj_path, "r") as f:
        s = f.read()
    
    filelist = [proj_path]

    workdir_save = os.getcwd()
    os.chdir(proj_dir)

    # find project files
    print("-- append project files --")

    for rex in rexs:
        r = re.findall(rex, s)
        if(r == None): continue

        for path in r:
            fpath = PlatformAbsPath(path)
            filelist.append( fpath )
            #print(fpath)


    # add extra in project root dir
    print("-- append extra files --")
    extra_file =[]

    for ex in extras:
                extra_file += [
                os.path.abspath(fn) for fn in glob.glob(ex,recursive=True)
                ]
    for x in extra_file: print(x)
    filelist += [ fn for fn in extra_file if os.path.isfile(fn) ]
        

        
    # add depended files
    print("-- append depends --")
    dep = []
    dep_files = []
    for root, dirs, files in os.walk(proj_dir, topdown=False):
        for file in files:
            if(not file.endswith(".d")): continue
            dep.append(os.path.join(root,file))
            #print(file)
            
    for fn in dep:
        f = open(fn, 'r', encoding='ascii')
        ret = re.findall(r"[^\s]+?:(.+?)\s", f.read())


        dep_files+= ret
        f.close()

    for fn in dep_files:
        fpath = PlatformAbsPath(fn.strip())
        filelist.append(fpath)
        #print(fpath)

    # remove exclude files
    def pattern_filters(s, patterns):
                for p in patterns:
                        if fnmatch.fnmatch(s, p):
                                return True

                return False
    filelist = [ fn for fn in filelist if not pattern_filters(fn, excludes)]

    # remove duplicate file
    filelist = list(set(filelist))

    # copy files limited in src_root_dir
    #print("-- remove files outside the project --")
    if(root_path != None):
        root_path = PlatformAbsPath(root_path)

        src_list = []
        for fpath in filelist:
            if(fpath.startswith(root_path)):
                src_list.append(fpath)
            else:
                print(fpath)
    os.chdir(workdir_save)

    return src_list
        
# copy files

def CopyFileToDir(flist, dpath):
    if(os.path.exists(dpath)):
        for root, dirs, files in os.walk(dpath, topdown=False):
            for name in files: os.remove(os.path.join(root, name))
            for name in dirs: os.rmdir(os.path.join(root, name))


    os.makedirs(dpath, exist_ok=True)
    for src_path in flist:

        if(not os.path.isfile(src_path) ):
            print("not exist:", src_path)
            continue
        
        dst_path = src_path.replace(src_root_dir, dpath)

        os.makedirs(os.path.dirname(dst_path), exist_ok=True)

        open(dst_path, "wb").write(open(src_path, "rb").read())

def CopyFileToZip(flist, dpath,src_root_dir):
    
    print("write to ", dpath)
    fzip = zipfile.ZipFile(dpath, 'w')

    fns = [ os.path.abspath(fn)  for fn in flist ]

    fns = set(fns)
    
    for src_path in fns:

        if(not os.path.isfile(src_path) ):
            print("not exist:", src_path)
            continue

        dst_path = os.path.relpath(src_path, src_root_dir)
        dst_path = os.path.join("va9638b", dst_path)
        fzip.write(src_path, dst_path)
        
    fzip.close()
        
def get_top_src_main(path):
    PROJ_FILE = path

    extras = ["../example/**","./*.exe","./*.sct","./*.bat", "*/*.tmpl"]
    excludes = ["*/output/*"]

    proj_dir = os.path.abspath(os.path.dirname(PROJ_FILE))
    src_root_dir = os.path.abspath(proj_dir + "/..")
    output_dir = os.path.abspath(
        os.path.join(os.path.dirname(src_root_dir)))
    output_zipfile = os.path.join(output_dir,
        "va9638br_coretop_%s.zip"%time.strftime("%Y%m%d%H%M%S"))

    src_list = KeilProjFiles(PROJ_FILE, root_path=src_root_dir,extras=extras, excludes=excludes)

    print("--- pure file list ----")
    for x in src_list: print(x)
    
    CopyFileToZip(src_list, output_zipfile,src_root_dir)
    print("--- done ----")

if __name__ == '__main__':
    PROJ_FILE = r"coretop/va9638b_top.uvproj"

    extras = ["../example/**","./*.exe","./*.sct","./*.bat", "*/*.tmpl"]
    excludes = ["*/output/*"]


    proj_dir = os.path.abspath(os.path.dirname(PROJ_FILE))
    src_root_dir = os.path.abspath(proj_dir + "/..")
    output_dir = os.path.abspath(
        os.path.join(os.path.dirname(src_root_dir)))
    output_zipfile = os.path.join(output_dir,
        "va9638br_coretop_%s.zip"%time.strftime("%Y%m%d%H%M%S"))

    src_list = KeilProjFiles(PROJ_FILE, root_path=src_root_dir,extras=extras, excludes=excludes)

    print("--- pure file list ----")
    for x in src_list: print(x)
    
    CopyFileToZip(src_list, output_zipfile,src_root_dir)
    print("--- done ----")

    input()
