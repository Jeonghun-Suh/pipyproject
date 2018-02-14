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

print 'all modules are succesfully called'

#you should modify this tag for each rpi3
tag = '00' 

def get_timestamp():
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	return st

def save_data(server_path, local_path):
	ftp.storbinary('STOR '+server_path, open(local_path, 'rb'))

def read_data(server_path, local_path):
	ftp.retrbinary('RETR '+server_path, open(local_path, 'wb').write)

def make_dir(dir):
	if directory_exists(dir) is False:
	        ftp.mkd(dir)

def directory_exists(dir):
    filelist = []
    ftp.retrlines('LIST',filelist.append)
    for f in filelist:
        if f.split()[-1] == dir and f.upper().startswith('D'):
            return True
    return False



# this is the body of the function
while True:
	i = 0
	st = get_timestamp()
	datetimenow = str(datetime.datetime.now())
	file = open('data/data'+str(st),'w')

	while i < 30:
		file.write(datetimenow+'|'+str(usclass.dist())+'|'+readmcp.read_one_line()+'\n')
		time.sleep(0.5)
		i+=1

	file.close()
	#make_dir('/data'+tag)
	save_data('/data'+tag+'/data'+str(st)+'.csv','data/data'+str(st))
	
ftp.quit()