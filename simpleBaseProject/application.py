# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import tornado.web
from views.index import IndexHandler
from config import settings

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/',IndexHandler),

        ]

        super(Application,self).__init__(handlers,**settings)