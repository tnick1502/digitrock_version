set version=3.50
set mydir=C:\DigitRock
goto main

:update
echo Update DigitRock...
rd /s /q %mydir%
goto install_main
:update_end
goto end 

:install_main
echo Install DigitRock...
md %mydir%

if exist "\\192.168.0.1\files\Digitrock\%version%" goto installIP
if exist "Z:\Digitrock\%version%" goto installIZ

:install_end
goto run

:installIP
echo installIP
xcopy /y /e "\\192.168.0.1\files\Digitrock\%version%\*.*" "%mydir%\*.*"
:enstallIP_end
goto run

:installIZ
echo installZ
xcopy /y /e "Z:\Digitrock\%version%\*.*" "%mydir%\*.*"
:install_zip_end
goto run

:run
cd %mydir%
python %mydir%\app.py
:run_end
goto end

:main
if exist %mydir% goto update
if not exist %mydir% goto install_main

:end

PAUSE