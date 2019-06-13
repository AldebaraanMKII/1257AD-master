@echo off

REM Create build directory
if not exist "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Build" mkdir "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Build"


REM Copy files to build folder
xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Compiler" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Header" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Process" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\ID" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Module" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"


xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Modmerger" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Custom Troop Trees" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Freelancer" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

REM xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Formations" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

REM xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Pre Battle Orders and Deployment" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"


REM NEW v2.1
xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Floris Bank" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"  

REM NEW v2.3
REM xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Character Creation" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"

REM xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Generic Presentation Utilities" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"


REM NEW v3.0
xcopy /s /y /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Source Kits\Decapitation" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"




REM Execute compile.bat
start /d "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build" compile.bat


REM wait for it to finish
TIMEOUT 20


REM Copy ID_ files to ID folder
xcopy /s /y "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build\ID_*.*" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\ID"
xcopy /s /y "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD - Enhanced Edition\variables.txt" "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\Module"



REM Removes build directory
@RD /S /Q "C:\Program Files (x86)\Mount&Blade Warband\Modules\1257AD-master\build"














