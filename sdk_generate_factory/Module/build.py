#!/usr/bin/env python3
# -*- encode: utf-8 -*-

## exec by python3

import os,platform, re
import zipfile, time


r'''
 µVision can be invoked from a command line to build a project, start the debugger, or download a program to Flash. The command applies to project and multiple-project files:

UV4 〚command〛 〚projectfile〛 〚options〛

Where
command     is one of the commands listed below. If no command is specified, µVision opens the project file in interactive Build Mode.
projectfile     is the name of a project file. µVision project files have the extension .uvproj, multiple-project files the extension .uvmpw. If no project file is specified, µVision opens the project file used last.
options     are additional parameters that specify the project target name or output file.

The following commands are available:
Command     Description
-b  Builds the last current target of a project and exits after the build process finished. Refer to option -t to change the target. For multi-projects, the command builds the targets as defined in the dialog Project - Batch Build.

Examples:
UV4 -b PROJECT1.uvprojx

-c  Clean all project targets of a project. For a multi-project, the command cleans all targets that have been selected in the dialog Project - Batch Build. Refer to the note on Project Menu and Commands for details about the cleaning process.

Examples:
UV4 -c PROJECT1.uvprojx

-cr     Clean all project targets and re-translate the last current target of a project. Refer to option -t to change the target. For multi-projects, the command cleans all targets and re-translates the targets as selected in the dialog Project - Batch Build. Refer to the note on Project Menu and Commands for details about the cleaning process.

Examples:
UV4 -cr PROJECT1.uvprojx

-d  Starts µVision in Debugging Mode. Use this command together with a debug initialization file to execute automated test procedures. Exit the debugging session with the EXIT command.

Examples:
UV4 -d PROJECT1.uvprojx

-f  Downloads the program to Flash and exits after the download process finished.

Examples:
UV4 -f PROJECT1.uvprojx -t"MCB2100 Board"

-r  Re-translates the last current project target and exits after the build process finished. Refer to option -t to change the target. For multi-projects, the command re-translates the targets as defined in the dialog Project - Batch Build.

Examples:
UV4 -r PROJECT1.uvprojx -t"Simulator"

-5  Converts a µVision 4 uvproj file into a µVision 5 uvprojx file. The only valid option with this command is -l for writing a log file.

Examples:
UV4 -5 myoldproject.uvproj -l log.txt
If the conversion fails, error code 20 will be returned.

The following options can be used:
Option  Description
-j0     Hides the µVision GUI. Messages are suppressed. Use this option for batch testing.
-i import_file.xml  Creates a new project or updates an existing project using the data provided by an XML file, which has to be compliant to the schema project_import.xsd available in the directory ..\UV4. The target name may be specified with the option -t. If a project is created from the command line without -t, the device name is used as the name of the target. The GUI is suppressed automatically when using this option.

Examples:
UV4 MyProject.uvprojx –i MyImport.xml

-l logfile  Saves the output of the command in the specified logfile.

Examples:
UV4 -5 myoldproject.uvproj -l log.txt
If the conversion fails, error code 20 will be returned.

-n device_name  Creates a new project with the specified device_name. The target name can be specified with the option -t. By default, the target name is set to the device name. The GUI is suppressed automatically when using this option.

Examples:
UV4 MyProject.uvprojx –n Device1234
UV4 MyProject.uvprojx –i MyImport.xml –n Device5678 -t FlashDebug

-t targetname   Sets targetname as the current target. If not specified, then the last known target is used.

Examples:
UV4 -r PROJECT1.uvprojx -t"MCB2100 Board"

-o outputfile   Specifies the output log file.

Examples:
UV4 -r PROJECT1.uvprojx -o"listmake.prn"
UV4 -r "C:\MyProjects\ARM\Example-mpw.uvmpw" -o "c:\temp\log.txt"

-q  Re-builds the selected targets of a multiple-project. Ensure that each target has another object output folder. Use the menu Projects - Options for Target - Output - Select Folder for Objects.

Examples:
UV4 -r "C:\MyProjects\ARM\Example-mpw.uvmpwx" -q -o "c:\temp\log.txt"

-z  Re-builds all targets of a project or multiple-project. Ensure that each target has another object output folder. Use the menu Projects - Options for Target - Output - Select Folder for Objects.

Examples:
UV4 -b PROJECT1.uvproj -z -o "c:\temp\log.txt"
UV4 -b "C:\MyProjects\ARM\Example-mpw.uvmpwx" -q -z -o "c:\temp\log.txt"

-x  Enables DDE mode and returns complete command output. This option can be used only with the command -d.
-y  Enables DDE mode and returns only command confirmations. This option can be used only with the command -d.

µVision sets the ERRORLEVEL after each build process to indicate the status. Refer to the Windows-help for information about ERRORLEVEL. The values are listed below:
ERRORLEVEL  Description
0   No Errors or Warnings
1   Warnings Only
2   Errors
3   Fatal Errors
11  Cannot open project file for writing
12  Device with given name in not found in database
13  Error writing project file
15  Error reading import XML file
20  Error converting project

Examples:

    Build a Target - builds an application from the command line.
    Program Flash - programs Flash from the command line.
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

def build(p, log='build.log', target=None):
    import sys
    sys.path.append(r"C:\Keil_v5\UV4")

    # find keil exec
    files = [
        r"C:\Keil_v5\UV4\UV4.exe",
        r"D:\Keil_v5\UV4\UV4.exe",
        r"E:\Keil_v5\UV4\UV4.exe",
        ]

    for exe in files:
        if(os.path.isfile(exe)):
           break

    if(not os.path.isfile(exe)):
           print("can't find keil")
           return
           

    if(not os.path.isfile(p)):
        print("Project file not exist:", p)
        return

    exec_cmd = r'%s -j0 -o"%s" -r "%s" ' %(exe, log, p)

    if(target != None): exec_cmd += " -q -t %s"%target
    else: exec_cmd += " -z"

    print(exec_cmd)
    ret = os.popen(exec_cmd)

    #print("output", ret.read())

    ret.close()

def fetch_log_summary(log):
    import re
    '''
    Rebuild target 'VA9638B_Release'

    ".\output\release\va9638b_top_release.axf" - 0 Error(s), 18 Warning(s).

    '''

    print("log file is", log)
    f = open(log, 'r')
    for l in f:
        if(re.match(r".+?uild target '.+?'", l) != None):
            print(l)
            continue
        if(re.match(r".+? Error\(s\), .+? Warning\(s\)", l) != None):
            print(l)
            continue
    f.close()


def build_target(root_path):

    ROOT_DIR=root_path
    print(ROOT_DIR)
    #input()
    project = os.path.join(ROOT_DIR, r"coretop\va9638b_top.uvproj")
    #print（project)
    log = os.path.join(os.getcwd(), "coretop.log")
    print("---- build", project)
    build(project, log,"VA9638B_Release")
    fetch_log_summary(log)

    project = os.path.join(ROOT_DIR, r"corebt\va9638b_bt.uvproj")
    log = os.path.join(os.getcwd(), "corebt.log")
    print("---- build", project)
    build(project, log,"VA9638B_Release")
    fetch_log_summary(log)

    project = os.path.join(ROOT_DIR, r"corebt\va9638b_bt.uvproj")
    log = os.path.join(os.getcwd(), "va9638b_bt.log")
    print("---- build", project)
    build(project, log,"VA9638B_Debug")
    fetch_log_summary(log)

    project = os.path.join(ROOT_DIR, r"corebt\va9638b_bt.uvproj")
    log = os.path.join(os.getcwd(), "va9638b_bt.log")
    print("---- build", project)
    build(project, log,"VA9638B_MassProduct")
    fetch_log_summary(log)

    project = os.path.join(ROOT_DIR, r"SecureFlashBootloader\SecureFlashBootloader.uvproj")
    log = os.path.join(os.getcwd(), "SecureFlashBootloader.log")
    print("---- build", project)
    build(project, log,"Release")
    fetch_log_summary(log)
    
    project = os.path.join(ROOT_DIR, r"SecureFlashBootloader\SecureFlashBootloader.uvproj")
    log = os.path.join(os.getcwd(), "SecureFlashBootloader.log")
    print("---- build", project)
    build(project, log,"Debug")
    fetch_log_summary(log)
 
    
if __name__ == '__main__':
    ROOT_DIR  = r".."

    project = os.path.join(ROOT_DIR, r"coretop\va9638b_top.uvproj")
    log = os.path.join(os.getcwd(), "coretop.log")
    print("---- build", project)
    build(project, log)
    fetch_log_summary(log)

    project = os.path.join(ROOT_DIR, r"corebt\va9638b_bt.uvproj")
    log = os.path.join(os.getcwd(), "corebt.log")
    print("---- build", project)
    build(project, log)
    fetch_log_summary(log)
    
    print("--- done ----")

   # input()
