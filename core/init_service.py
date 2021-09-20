from multiprocessing import Process
from subprocess import Popen, PIPE, STDOUT
from core.flask import *
from core.ftpserver import *

def init_service():
    init_flask=Popen("python3 /core/flask.py", stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    
    init_ftp=Popen("python3 /core/ftpserver.py", stdin=PIPE, stdout=PIPE, stderr=STDOUT)   
    