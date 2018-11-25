# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
from tornado import ioloop
from simpleBaseProject import config
from application import Application

if __name__ == '__main__':
    app = Application()
    app.listen(config.options['port'])
    ioloop.IOLoop.current().start()