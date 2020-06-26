@echo off

:: ---------------------------------------------------------------------------------------
:: This script helps people with storing their minecraft saves, resourcespacks,
:: screenshots, and shaders somewhere other than the default .minecraft folder, prefferably
:: in cloud storage (Onedrive, Dropbox, etc.) for easy portability :)
::
:: Notes: run as admin, and set the two below variables before running
::
:: Variables:
:: link: The .minecraft folder where the game looks for saves and such.
:: target: The location where you are storing your saves
:: ---------------------------------------------------------------------------------------

set link=C:\Users\username\AppData\Roaming\.minecraft
set target=C:\Users\username\path\to\cloud\storage

echo %link%
echo %target%

mklink /D "%link%\saves" "%target%\saves"
mklink /D "%link%\resourcepacks" "%target%\resourcepacks"
mklink /D "%link%\screenshots" "%target%\screenshots"
mklink /D "%link%\shaderpacks" "%target%\shaderpacks"

pause
