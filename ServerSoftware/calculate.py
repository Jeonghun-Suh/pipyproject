##  @file     calculate.py
#   @brief    Software body.
#   @author   Jeonghun Suh
#   @date     Feb 12, 2018
import math
import time
from time import localtime, strftime
from AbstractFile import filename
from AbstractMath import *

while True:
	time_value = 0.0
	dcv = 0.0
	scv = 0.0
	lcv = 0.0
	
	now = strftime("%Y%m%d%H%M%S", localtime())
	path_dir = "/home/clients/data"
	fname = filename(now, path_dir)
	file1 = open('/home/clients/data/'+fname, "r")
	file2 = open('/home/clients/display/'+'dangerlevels', 'a')

	lines = file1.readlines()
	data_length = float(len(lines))

	for item in lines:
		lst = item.split('|')

		#this is local time stamp
		ltime = lst[0].split(' ')[1].split('.')[0]

		#from the time stamp value, extract the localtime for calculation
		ltime_temp = time_to_pseudoreal(ltime)
		ltime_real = time_to_real(ltime)


		#calculation of time_value
		tempvalue = evaluate_time(time_value, ltime_real)
		time_value += tempvalue	

		#calculation of distance_correlated_value
		if float(lst[1]) < 3000.0:
			dcv += 1.0
	
		#calculation of sound_correlated_value
		if float(lst[2]) < 50.0:
			scv += float(lst[2])/50.0

		#calculation of light_correlated_value
		if float(lst[3]) < 100.0:
			lcv += float(lst[3])/100.0
	
	time_value = time_value / data_length
	dcv = dcv / data_length
	scv = scv / data_length
	lcv = lcv / data_length
	lst = [time_value, dcv, scv, lcv]

	file2.write(str(now)+','+fname.strip('.csv').strip('data')+','+str(danger_level(lst))+'\n')

	file1.close()
	file2.close()
	time.sleep(15)


