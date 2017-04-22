#!/bin/bash
echo $1
echo $2
echo $3
timeout 15 xterm -e "airodump-ng --bssid $2 -c $3 mon0 -w temp/dump" &
#echo "airodump-ng --bssid $2 -c $3 mon0"