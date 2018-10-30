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
    server = httpServer.HTTPServer(app)
    # server.listen(8000)
    server.bind(8000)
    server.start(4) #4porcessers

    ioloop.IOLoop.current().start()