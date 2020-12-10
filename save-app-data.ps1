$appdataFolder = "C:\Users\cris"

$pathsToCopy = "\AppData\LocalLow\Team Cherry", 
"\AppData\Roaming\DarkSoulsIII", 
"\AppData\Roaming\Factorio",
"\AppData\Roaming\dungeon",
"\AppData\Local\HyperLightDrifter"

foreach ($path in $pathsToCopy) {
    if(Test-Path "$appdataFolder$path") {
        Copy-Item -Path "$appdataFolder$path" -Destination ".$path" -Recurse -Force
    }    
}
