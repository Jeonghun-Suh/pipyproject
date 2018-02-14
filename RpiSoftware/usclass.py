##  @file     usclass.py
#   @brief    usclass module. just for reading the ultrasoninc sound sensor data
#   @author   Jeonghun Suh (Dep. of Physics, chemist1104@kaist.ac.kr)
#   @date     Feb 13, 2018

import RPi.GPIO as gpio
import time

#GPIO set warnings function is important part for running without any errors.
#it is needed to ignore all the warnings
gpio.setwarnings(False)

#gpio mode (gpio.BCM or gpio.BOARD)
gpio.setmode(gpio.BCM)

#If you need to change the GPIO pin, please revise this part also
trig=23
echo=24

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

#this function returns the distance value. but the value is quite rough
def dist():
    #gpio cleanup and launching the first pulse wave
	gpio.output(trig,False)
	time.sleep(0.1)
	gpio.output(trig,True)
	time.sleep(0.0001)
    
	now = time.clock()
    
	pulse_start = now
	pulse_end = now
    
	while gpio.input(echo) == 0:
		pulse_start = time.clock()

		#If it takes too long time, program would not wait for it
		if pulse_start - now > 1:
			break

	while gpio.input(echo) == 1:
		pulse_end = time.clock()

	dur = pulse_end - pulse_start
	dist = dur*17150
	if dist < 0:
		dist = 3000

	return dist

# this function exports the input value of 'echo'
# (trig has only output value)
def print_echo():
    gpio.output(trig,True)
    time.sleep(0.0001)
    print gpio.input(echo) 


#this function is for test
def ticktack():
    gpio.output(trig,True)
    time.sleep(0.5)
    gpio.output(trig,False)
    time.sleep(0.5)

