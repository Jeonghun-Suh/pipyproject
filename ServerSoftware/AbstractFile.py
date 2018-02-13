##  @file     AbstractFile.py
#   @brief    AbstractFile class definition.
#   @author   Jeonghun Suh
#   @date     Feb 12, 2018
import os

def filename(now, path_dir):
	file_list = os.listdir(path_dir)
	diff = []
	minimum = int(now)
	i = len(file_list) - 1
	
	for i in range(len(file_list)):
		if len(file_list[i].split('.')) != 2:
			print ('warning: unexpected files in the data dir')
			continue
		elif file_list[i].split('.')[1] != 'csv':
			print ('warning: unexpected files in the data dir')
			continue

		time_of_file = file_list[i].split('data')[1].split('.csv')[0]
		diff = ( abs(int(now) - int(time_of_file)))
		
		if diff < minimum:
			minimum = diff
			minimum_index = i

	return file_list[minimum_index]
