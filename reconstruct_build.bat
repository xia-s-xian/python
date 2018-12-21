:: Run after build
:: build_bin.bat "$KARM"\ARMCC\bin @L $L %L
:: build_bin.bat <fromelf bin locate dir> <output name> <output target dir> <output taget file extension >

::Key Code 	Description 
::% 		File name with extension (PROJECT1.UVPROJ) 
::# 		File name with extension and complete path specification (C:\MYPROJECT\PROJECT1.UVPROJ) 
::@ 		File name without extension or path specification (PROJECT1) 
::$ 		Path name of a file. Path names get extended with a backslash. For example, $P could generate C:\MYPROJECT\. 
::! 		File name with extension and relative path specification to the current folder (.\SRC\TEST.C) 
::~ 1 		Line number of the current cursor position 
::^ 1 		Column number of the current cursor position 

::file Code Description 
::$D 		Device name as selected from the Device Database. 
::E 		Editor file name currently in focus. 
::F 		Depending on the context, this File Code returns: 
::			 The file selected in the window Project. 
::			 The currently active editor file. 
::			 The file that is currently translated by a build process. 
 
::H 		Application HEX file name (PROJECT1.H86). 
::$J 		Absolute compiler system include folder. Compiler base folders are listed in the field Project — Manage — Project Items — Folder/Extensions - ARMCC Folder. The include path depends on the compiler selected in Options for Target - Code Generation - ARM Compiler. 
::K 		Absolute root folder of the development toolchain, regardless of the Key Code used. 
::L 		Linker output file. Typically the executable file used for debugging (PROJECT1). 
::$M 		CPU mask revision number. 
::P 		Current project file name. 
::X 		µVision executable program file (..\UV4\UV4.EXE). Works for For Key Code %, # @. 
::$X 		XTAL clock frequency in MHz as specified in Options for Target — Target — XTAL. 
::^X 		XTAL clock frequency in kHz as specified in Options for Target — Target — XTAL. 

