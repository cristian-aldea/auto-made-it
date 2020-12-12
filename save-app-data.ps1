$appdataFolder = "C:\Users\cris"

$pathsToCopy = "\AppData\LocalLow\Team Cherry", 
"\AppData\Roaming\DarkSoulsIII", 
"\AppData\Roaming\Factorio",
"\AppData\Roaming\dungeon",
"\AppData\Local\HyperLightDrifter",
"\AppData\Local\Downwell_v1_0_5"

foreach ($path in $pathsToCopy) {
    if(Test-Path "$appdataFolder$path") {
        Copy-Item -Path "$appdataFolder$path" -Destination ".$path" -Recurse -Force
    }    
}
