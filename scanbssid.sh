#!/bin/bash
echo $1
timeout 5 xterm -e "airodump-ng $1 -w temp/dump" &