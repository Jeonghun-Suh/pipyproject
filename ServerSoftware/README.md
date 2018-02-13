
# Software for Linux Server

## FTP server setup
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
  
	1. service vsftpd status

then you will get

	vsftpd is stopped
  
Let's start configuration.
  
	1. vi /etc/vsftpd/vsftpd.conf

'i' is the insert command and 'ctrl + c', ':wq' means 'quit with save the modified things'

set the (you should find each conpoments and revise them)

	1.	anonymous_enable = NO
	2.	local_enable = YES
	3.	write_enable=YES
	4.	local_umask=022
	5.	dirmessage_enable=YES
	6.	xferlog_enable=YES
	7.	connect_from_port_20=YES
	8.	xferlog_file=/var/log/xferlog
	9.	xferlog_std_format=YES
	10.	chroot_local_user=YES
	11.	listen=YES
	12.
	13.	pam_service_name=vsftpd
	14.	userlist_enable=YES
	15.	tcp_wrappers=YES

now we can run the vsftpd

	1. service vsftpd start
	2. netstat -anp | grep vsftpd
	3. chkconfig vsftpd on
	4. chkconfig --list | grep vsftpd

additional configuration settings

	1. vi /etc/sysconfig/iptables-config

then revise it as

	IPTABLES_MODULES="ip_conntrack_ftp"

and restart the iptables service with

	1. service iptables restart
	2. service vsftpd restart

## APM(apache, PHP, Mysql) setup
