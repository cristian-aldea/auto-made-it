<# =============================================================================
This script allows you to store your minecraft game data somewhere other than the 
default directory by creating symlinks.

These symlinks are stored within the .minecraft directory and point to actual folders
somewhere else on your computer.

One cool thing this allows you to do is to have your minecraft saves stored on the cloud!

Notes:  
- Administrator priviledges might be required to run this script
- Before running this script, you need to set the two variables below:

Variables:
- link: The .minecraft folder where Minecraft stores your game files
- target: The folder where you want to store your game files
============================================================================= #>

$link = "C:\Users\cris\AppData\Roaming\.minecraft"
$target = "C:\path\to\your\game\files"

$gameDirs = "saves", "resourcepacks", "screenshots", "shaderpacks"

Write-Host "link: $link"
Write-Host "target: $target`n"


foreach ($gameDir in $gameDirs) {
    $linkDir = "$link\$gameDir"
    $targetDir = "$target\$gameDir"
    if ( -not (Test-Path  -PathType Container -Path $linkDir)) {
        Write-Host "`nCreating link from $targetDir to $linkDir"
        New-Item -ItemType SymbolicLink -Path $linkDir -Target $targetDir
    }
    else {
        Write-Host "Folder $linkDir already exists, skipping for now"
    }
}

Write-Host ""
