from flask import Flask, render_template
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from core.config import *

app = Flask('')

@app.route('/')
def main():
  return 'hi'


app.run(host="0.0.0.0", port=3064)