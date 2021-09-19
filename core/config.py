from configobj import ConfigObj

Config=ConfigObj('./config/config.ini')

ftp=Config['FTP']

ftp_user=ftp['ftp_user']
ftp_password=ftp['ftp_password']
ftp_port=int(ftp['ftp_port'])

jvm=Config['JVM']

jvm_max_ram=jvm['jvm_max_ram']
jvm_min_ram=jvm['jvm_min_ram']
jvm_costume=jvm['jvm_costume']