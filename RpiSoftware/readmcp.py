##  @file     readmcp.py
#   @brief    readmcp module. for reading the analogue data with Adafruit_MCP3008 module
#   @author   Jeonghun Suh (Dep. of Physics, chemist1104@kaist.ac.kr)
#   @date     Feb 13, 2018

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# if you need to change the GPIO Channel, you should revise this part
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def read(i):
	return mcp.read_adc(i)

def read_one_line():
	line = str(read(0))+'|'+str(read(1))+'|'+str(read(2))+'|'+str(read(3))+'|'+str(read(4))+'|'+str(read(5))+'|'+str(read(6))+'|'+str(read(7))
	return line
