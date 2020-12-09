$appdataFolder = "C:\Users\cris"

$pathsToCopy = "\AppData\LocalLow\Team Cherry", 
"\AppData\Roaming\DarkSoulsIII", 
"\AppData\Roaming\Factorio"

foreach ($path in $pathsToCopy) {
    Copy-Item -Path "$appdataFolder$path" -Destination ".$path" -Recurse
    # Write-Host "$appdataFolder$path"
}

