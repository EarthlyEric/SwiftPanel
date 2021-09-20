from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from core.config import *


FTP_PORT = ftp_port

FTP_USER = ftp_user

FTP_PASSWORD = ftp_password

FTP_DIRECTORY = "./server"


def FTP():
    authorizer = DummyAuthorizer()

    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "pyftpdlib based ftpd ready."



    address = ('0.0.0.0', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 300
    server.max_cons_per_ip = 100

    server.serve_forever()

FTP()