#-*- coding:utf-8 -*-
"""
This script runs the RandU application using a development server.
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from os import environ
from RandU import app



if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
