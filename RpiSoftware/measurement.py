##  @file     measurement.py
#   @brief    measurement of all the sensor datas and recored it to the data directory. 
#			  with readmcp and usclass modules
#   @author   Jeonghun Suh (Dep. of Physics, chemist1104@kaist.ac.kr)
#   @date     Feb 13, 2018

import AbstractFTP
import usclass
import readmcp
import time
import datetime

tag = '00' 

def get_timestamp():
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	return st



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
	AbstractFTP.make_dir('/data'+tag)
	AbstractFTP.save_data('/data'+tag+'/data'+str(st)+'.csv','data/data'+str(st))
