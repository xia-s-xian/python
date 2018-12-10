@echo off
set UV=C:\Keil_v5\UV4\UV4.exe

set UV_PRO_PATH=F:\8.ZGW\4_VA9638项目\18_集成发布\VA9638B_V8000_MultiCore\SecureFlashBootloader\SecureFlashBootloader.uvproj
echo Init building ...
echo .>build_log.txt
%UV% -j0 -r %UV_PRO_PATH% -t"SecureFlashbootloader
" -o %cd%\build_log.txt
type build_log.txt
echo Done.
pause
