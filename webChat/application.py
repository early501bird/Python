# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-



import tornado.web
from views.index import *
import  os
from config import settings


class Application(tornado.web.Application):
    def __init__(self):
        handlers= (

            (r'/home',HomeHandler),
            (r'/students1', StudentsHandler),
            (r'/students2', Students2Handler),
            (r'/students3', Students3Handler),
        )

        super(Application,self).__init__(handlers,**settings)

