##  @file     AbstractMath.py
#   @brief    AbstractMath class definition.
#   @author   Jeonghun Suh
#   @date     Feb 12, 2018

import math

## This part is a pre-definition of the program
#this is multiplier for last result (danger_level)
set_coeff = 0.1

#those are coefficients for the each values. These are some kinds of weights.
coff_lst = [1.1, 2.2, 0.41, 1.15]
lent = len(coff_lst)
const = 0.1
	
#danger_time_predefinition
danger_time_list = [[230000,235959], [0,15959]]

#function of determining the danger level
def danger_level(lst):
	total = 0.0	
	for i in range(lent):
		total += lst[i]*coff_lst[i]

	fin = 2.0*(1.0/ (math.exp(-1.0*const*total)+1.0) - 0.5)
	return fin


#This function converts a time_stamp(HH:MM:SS) format to a real value(unit: Hours) 
def time_to_real(local_time_stamp):
	ltime = local_time_stamp
	ltime_real = float(ltime[0])*10 + float(ltime[1]) + (float(ltime[3])*10.0 + float(ltime[4]))/60.0 + (float(ltime[6])*10 + float(ltime[7]))/3600.0


	return ltime_real


#This function converts a time_stamp(HH:MM:SS) format to a pseudo-real value(HHMMSS) 
def time_to_pseudoreal(local_time_stamp):
	ltime = local_time_stamp
	ltime_temp = int(ltime[0])*100000+int(ltime[1])*10000+int(ltime[3])*1000+int(ltime[4])*100+int(ltime[6])*10+int(ltime[7])*1

	return ltime_temp


#This function is used to evaluate the time values
def evaluate_time(initial_value, local_time):
	frv = 0
	if danger_time_list[0][0] < local_time < danger_time_list[0][1]:
		frv += 1.0
	elif danger_time_list[1][0] < local_time < danger_time_list[1][1]:
		frv += 1.0
	elif 12.0 < local_time < 24.0 :
		frv += abs(local_time - 23.0) / 24.0 
	elif 0.0 < ltime_real < 12.0:
		frv += abs(local_time - 1.0) / 24.0


	return frv
