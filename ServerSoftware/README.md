
# Software for Linux CentOS 7 Server

## FTP server setup
This program is for CentOS 7 Linux server (I think the other UNIX based OSs will be OK.) .

Firstly, Server should be working as a FTP server (Because Data taking from the RPi go through the FTP.)

For install the vsftp(acronym of 'Very Stable FTP') follow this

confirm if there is vsftpd or not

	rpm -qa vsftpd*
  
if there is no vsftpd,

	yum install vsftpd -y	
	rpm -qa vsftpd*
  
then you will get the message below
  
	vsftpd-VERSION.NUMBERS.
 
you can start the vsftpd service now, but it needs some configurations.
confirm with the command below
  
	service vsftpd status

then you will get

	vsftpd is stopped
  
Let's start configuration.
  
	vi /etc/vsftpd/vsftpd.conf

'i' is the insert command and 'ctrl + c', ':wq' means 'quit with save the modified things'

set the (you should find each conpoments and revise them)

	anonymous_enable = NO
	local_enable = YES
	write_enable=YES
	local_umask=022
	dirmessage_enable=YES
	xferlog_enable=YES
	connect_from_port_20=YES
	xferlog_file=/var/log/xferlog
	xferlog_std_format=YES
	chroot_local_user=YES
	listen=YES
	
	pam_service_name=vsftpd
	userlist_enable=YES
	tcp_wrappers=YES

now we can run the vsftpd

	service vsftpd start
	netstat -anp | grep vsftpd
	chkconfig vsftpd on
	chkconfig --list | grep vsftpd

additional configuration settings

	vi /etc/sysconfig/iptables-config

then revise it as

	IPTABLES_MODULES="ip_conntrack_ftp"

and restart the iptables service with

	service iptables restart
	service vsftpd restart

## APM(apache, PHP, Mysql) setup

### the packages for the install
confirm the packages with

	rpm -qa libjpeg* libpng* freetype* gd-* gcc gcc-c++ gdbm-devel libtermcap-devel

and setup them(if you don't have them)

	yum install libjpeg* libpng* freetype* gd-* gcc gcc-c++ gdbm-devel libtermcap-devel
	
### Install the Apache
	
	yum install httpd
	
### Install the MariaDB
At first, you should make the yum repository
	
	vi /etc/yum.repos.d/MariaDB.repo
	
and paste below

	# MariaDB 10.1 CentOS repository list 
	# http://downloads.mariadb.org/mariadb/repositories/
	[mariadb]
	name = MariaDB
	baseurl = http://yum.mariadb.org/10.2/centos7-amd64
	gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
	gpgcheck=1

and install it

	yum install MariaDB-server MariaDB-client
	
### Install the PHP7(latest ver. in Feb 13, 2018)

At First, you should make an yum repo

	rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
	rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
	
and you can install it

	yum install php70w

(this is for install PHP7)

and you can also install PHP7 packages

	yum install php70w-mysql php70w-pdo php70w-pgsql php70w-odbc php70w-mbstring php70w-mcrypt php70w-gd
	yum install php70w-pear php70w-pdo_dblib php70w-pecl-imagick php70w-pecl-imagick-devel php70w-xml php70w-xmlrpc

### Confirm the installation

	httpd -v
	php -v
	mysql -V

with those three commands, you can confirm the installation and its version.

### Apache configuration

you can open the configuration file with vi editor

	vi /etc/httpd/conf/httpd.conf

and revise it as

	...
	User nobody
	Group nobody
	...
	ServerName your.domain.name:80
	...
	
or

	...
	User nobody
	Group nobody
	...
	ServerName 127.0.0.0:80 (or your ip4 address)
	...

if you don't know about your ip address,

	ifconfig
	
this command will show it.

then let's open the firewall port

	vi /etc/sysconfig/iptables
	
and add below line just after the "-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT"

	-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT

the sequence of the lines are very important in this part

	service iptables restart
	iptables -nL
	
and start apache server

	systemctl start httpd
	systemctl enable httpd
	
or

	service httpd start
	systemctl enable httpd

then, you can confirm it

	ps -ef |grep httpd
	
