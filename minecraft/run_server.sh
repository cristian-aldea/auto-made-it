#!/bin/sh

java -Xms6G -Xmx6G -jar forge.jar nogui
#java -XX:+UseG1GC -Xms6G -Xmx6G -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UnlockExperimentalVMOptions -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M forge.jar nogui
