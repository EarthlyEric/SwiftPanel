from configobj import ConfigObj

Config=ConfigObj('./config/config.ini')

ftpconfig=Config['FTP']

ftp_user=ftpconfig['ftp_user']
ftp_password=ftpconfig['ftp_password']
ftp_port=int(ftpconfig['ftp_port'])