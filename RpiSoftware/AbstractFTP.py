##  @file     measurement.py
#   @brief    measurement of all the sensor datas and recored it to the data directory. 
#			  with readmcp and usclass modules
#   @author   Jeonghun Suh (Dep. of Physics, chemist1104@kaist.ac.kr)
#   @date     Feb 14, 2018

# this is for permission to the FTP server
from ftplib import FTP

ftpad = '116.38.151.198'
ftpid = 'pi01'
ftppw = 'capprules'

ftp = FTP(ftpad)
ftp.login(ftpid, ftppw)

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
