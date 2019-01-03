goto :main

keil after build cmd
--------------------------------------------------------------------------------------------------------------------------------
Keil_v5

release.bat $KARM\ARMCC\bin @L .\output\release %L
release.bat C:\Keil_v5\ARM\ARMCC\bin SecureFlashBootloader .\output\release SecureFlashBootloader.axf
$:路径名指示 
k:开发工具的绝对根文件夹
例如：
$k:C:\Keil_v5                           

---------------------------------------------------------------------------------------------------------------------------------
cmd
After Build - User command #1: release.bat C:\Keil_v5\ARM\ARMCC\bin SecureFlashBootloader .\output\release SecureFlashBootloader.axf

%:表示命令行参数
%var%:表示变量

参数：
%1：C:\Keil_v5\ARM\ARMCC\bin
%2：SecureFlashBootloader
%3：.\output\release
%4：SecureFlashBootloader.axf

set exepath=%3    设置参数3
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set exepath=.\output\release 
set CurDate=%date:~0,4%%date:~5,2%  
%date:~0,4%      变量data 指针从左至右偏移0位，然后从偏移的地方提取4个字符
%date:~5,2%      变量data 指针从左至右偏移5位，然后从偏移的地方提取2个字符
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set CurDate=201812 
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set CurTime=135616 

set CurTime=%CurTime: =0%   
%CurTime: =0%    变量CurTime从左至右偏移0位，然后提取所有值
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set CurTime=135616 

set rpath=.\output\%2_Release_%CurDate%%date:~8,2%_%CurTime%
%date:~8,2%     变量data 指针从右至左偏移8位，然后从偏移的地方提取4个字符
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set rpath=.\output\SecureFlashBootloader_Release_20181213_135616 

set binpath=%rpath%\binary
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set binpath=.\output\SecureFlashBootloader_Release_20181213_135616\binary 

set debugpath=%rpath%\debuginfo
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>set debugpath=.\output\SecureFlashBootloader_Release_20181213_135616\debuginfo 

for /f "delims=" %%i in ('dir /ad /s /b .\output\*_release*') do (del /F /S /Q %%i & rd /S /Q %%i)

C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>for /F "delims=" %i in ('dir /ad /s /b .\output\*_release*') do (del /F /S /Q %i   & rd /S /Q %i ) 
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>(del /F /S /Q C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942   & rd /S /Q C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942 ) 
删除文件 - C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942\binary\SecureFlashBootloader.bin
删除文件 - C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942\binary\SecureFlashBootloader_0.bin
删除文件 - C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942\debuginfo\SecureFlashBootloader.axf
删除文件 - C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942\debuginfo\SecureFlashBootloader.map
删除文件 - C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader\output\SecureFlashBootloader_Release_20181213_132942\debuginfo\SecureFlashBootloader.txt
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if not exist .\output\SecureFlashBootloader_Release_20181213_135616 mkdir .\output\SecureFlashBootloader_Release_20181213_135616    
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if not exist .\output\SecureFlashBootloader_Release_20181213_135616\binary mkdir .\output\SecureFlashBootloader_Release_20181213_135616\binary 
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if not exist .\output\SecureFlashBootloader_Release_20181213_135616\debuginfo mkdir .\output\SecureFlashBootloader_Release_20181213_135616\debuginfo 
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if exist .\output\release\SecureFlashBootloader.axf copy  .\output\release\SecureFlashBootloader.axf .\output\SecureFlashBootloader_Release_20181213_135616\debuginfo\ 
已复制         1 个文件。
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if exist .\output\release\SecureFlashBootloader.map copy  .\output\release\SecureFlashBootloader.map .\output\SecureFlashBootloader_Release_20181213_135616\debuginfo\ 
已复制         1 个文件。
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if exist .\output\release\SecureFlashBootloader.axf C:\Keil_v5\ARM\ARMCC\bin\fromelf --bin --output .\output\SecureFlashBootloader_Release_20181213_135616\binary\SecureFlashBootloader.bin .\output\release\SecureFlashBootloader.axf 
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if exist .\output\SecureFlashBootloader_Release_20181213_135616\binary\SecureFlashBootloader.bin BinsplitCRC .\output\SecureFlashBootloader_Release_20181213_135616\binary\SecureFlashBootloader.bin .\output\SecureFlashBootloader_Release_20181213_135616\binary\ 0x00 32k 
crc32_data = 0x985BF579
BinsplitCRC splits input file SecureFlashBootloader.bin to generate 1 binary files:SecureFlashBootloader_0.bin(32768) 
C:\Users\DELL\Desktop\VA9638B_V8000_MultiCore\SecureFlashBootloader>if exist .\output\release\SecureFlashBootloader.axf C:\Keil_v5\ARM\ARMCC\bin\fromelf --text -c -s --output .\output\SecureFlashBootloader_Release_20181213_135616\debuginfo\SecureFlashBootloader.txt .\output\release\SecureFlashBootloader.axf 
".\output\release\SecureFlashBootloader.axf" - 0 Error(s), 0 Warning(s).
Build Time Elapsed:  00:00:03

:main
date
time

