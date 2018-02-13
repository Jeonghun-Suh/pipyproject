##  @file     measurement.py
#   @brief    measurement of all the sensor datas and recored it to the data directory. 
#			  with readmcp and usclass modules
#   @author   Jeonghun Suh (Dep. of Physics, chemist1104@kaist.ac.kr)
#   @date     Feb 13, 2018

import usclass
import readmcp
import time
import datetime

# this is for permission to the FTP server
from ftplib import FTP
ftp = FTP("116.38.151.198")
ftp.login('pi01', 'capprules')

# this is the body of the function
while True:
	i = 0
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	file = open('data/data'+str(st),'w')

	while i < 30:
		file.write(str(datetime.datetime.now())+'|'+str(usclass.dist())+'|'+str(readmcp.read(0))+'|'+str(readmcp.read(2))+'|'+str(readmcp.read(3))+'|'+str(readmcp.read(4))+'|'+str(readmcp.read(5))+'|'+str(readmcp.read(6))+'|'+str(readmcp.read(7))+'\n')
		time.sleep(0.5)
		i+=1

	file.close()
	ftp.storbinary('STOR /data/data'+str(st)+'.csv',open('data/data'+str(st), 'rb'))




