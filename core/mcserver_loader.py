import os
from subprocess import Popen, PIPE, STDOUT
from core.config import *


def start_mcserver():
    os.chdir('./server')
    server = Popen(f"java -Xmx{jvm_max_ram}G -Xms{jvm_min_ram}G {jvm_costume} -jar  server.jar nogui", stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    os.chdir(f'{os.getcwd()}')
    while True:
       return server.stdout.readline()

