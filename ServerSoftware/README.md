
# Software for Linux Server

This program is for CentOS 7 Linux server (I think the other UNIX based OSs will be OK.) .

Firstly, Server should be working as a FTP server (Because Data taking from the RPi go through the FTP.)

For install the vsftp(acronym of 'Very Stable FTP') follow this

confirm if there is vsftpd or not

	1. rpm -qa vsftpd*
  
if there is no vsftpd,

	1. yum install vsftpd -y
  2. rpm -qa vsftpd*
  
then you will get the message below
  
  vsftpd-VERSION.NUMBERS.
 
you can start the vsftpd service now, but it needs some configurations.
confirm with the command below
  
  1.  service vsftpd status

then you will get

  vsftpd is stopped
  
Let's start configuration.
  
  1.  vi /etc/vsftpd/vsftpd.conf

'i' is the insert command and 'ctrl + c', ':wq' means 'quit with save the modified things'

set the

  1.  anonymous_enable = NO
  2.  local_enable = YES
  3.  write_enable = YES
  4.  local_umask = 022
  5.  dirmessage_enable = YES
  6.  xferlog_enable = YES
  7.  connect_from_port_20 = YES
  8.  xferlog_file = /var/log/xferlog
  9.  xferlog_str_format = YES
  10. 
