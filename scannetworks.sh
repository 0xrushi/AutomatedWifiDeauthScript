#!/bin/bash
echo $1
echo $2
echo $3
echo $4
timeout 15 xterm -e "airodump-ng --bssid $3 -c $4 $1 -w temp/dump" &
#echo "airodump-ng --bssid $2 -c $3 mon0"