# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
from tornado import  web

class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index handler get')

