from threading import Thread
from core.ftpserver import *
from core.flask import *

FTP_service=Thread
FTP_service(target=FTP())
FTP_service.start()

Flask_service=Thread
FTP_service(target=run())
Flask_service.start()
