# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado import web,ioloop
import tornado.httpserver as httpServer

class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index handler get ...')


if __name__ == '__main__':
    app = web.Application([
        (r'/',IndexHandler)  #陆由
    ])

    # app.listen(8000)
    #实例化http服务器对象,代替17行代码
    server = httpServer.HTTPServer(app)
    server.listen(8000)


    ioloop.IOLoop.current().start()