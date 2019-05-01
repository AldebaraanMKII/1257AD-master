@echo off

REM Create build directory
if not exist "C:\Users\Krzysiek\Desktop\1257AD-master\Build" mkdir "C:\Users\Krzysiek\Desktop\1257AD-master\Build"


REM Copy files to build folder
xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Compiler" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Header" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Process" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\ID" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Module" "C:\Users\Krzysiek\Desktop\1257AD-master\build"


xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Modmerger" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Custom Troop Trees" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Freelancer" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

REM xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Formations" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

REM xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Pre Battle Orders and Deployment" "C:\Users\Krzysiek\Desktop\1257AD-master\build"


REM NEW v2.1
xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Floris Bank" "C:\Users\Krzysiek\Desktop\1257AD-master\build"  

REM NEW v2.3
REM xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Character Creation" "C:\Users\Krzysiek\Desktop\1257AD-master\build"

REM xcopy /s /y /Q "C:\Users\Krzysiek\Desktop\1257AD-master\Source Kits\Generic Presentation Utilities" "C:\Users\Krzysiek\Desktop\1257AD-master\build"



REM Execute compile.bat
start /d "C:\Users\Krzysiek\Desktop\1257AD-master\build" compile.bat


REM wait for it to finish
TIMEOUT 20


REM Copy ID_ files to ID folder
xcopy /s /y "C:\Users\Krzysiek\Desktop\1257AD-master\build\ID_*.*" "C:\Users\Krzysiek\Desktop\1257AD-master\ID"
xcopy /s /y "C:\Users\Krzysiek\Desktop\1257AD - Enhanced Edition\variables.txt" "C:\Users\Krzysiek\Desktop\1257AD-master\Module"



REM Removes build directory
@RD /S /Q "C:\Users\Krzysiek\Desktop\1257AD-master\build"














