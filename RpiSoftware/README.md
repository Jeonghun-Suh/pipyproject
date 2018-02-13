# This is a client software for Raspberry Pi 3

@@ Author: Jeonghun Suh

@@ Email: chemist1104@kaist.ac.kr

@@ Brief: this is an introduction for the rpi3 with IoT

If you don't have a MCP3008 class for python, open the terminal and

	sudo apt-get update
	sudo apt-get install build-essential python-dev python-smbus git
	cd ~
	git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
	cd Adafruit_Python_MCP3008
	sudo python setup.py install

or just enter the directory in this folder

	cd Adafruit_Python_MCP3008
	sudo python setup.py install

After this, you can run the measurement.py

Thanks!
