#!/bin/bash

MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%\t\t", $3*100/$2 }' | xargs -I {} echo Mem Usage {} )
DISK=$(df -h | awk '$NF=="/"{printf "%s\t\t", $5}' |  xargs -I {} echo Disk Usage {} )
CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%\t\t\n", $(NF-2)}' |  xargs -I {} echo CPU Usage {})
