@echo off

rem run as admin
rem Set these variables before running

set link=C:\Users\Cristian Aldea\AppData\Roaming\.minecraft
set target=C:\Users\Cristian Aldea\OneDrive - Concordia University - Canada\game-files\.minecraft

echo %link%
echo %target%

mklink /D "%link%\saves" "%target%\saves"
mklink /D "%link%\resourcepacks" "%target%\resourcepacks"
mklink /D "%link%\screenshots" "%target%\screenshots"
mklink /D "%link%\shaderpacks" "%target%\shaderpacks"

pause