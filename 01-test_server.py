# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
from tornado import web,ioloop

#ioloop 核心的IO循环模块，封装了Linux的epoll和BSD的kqueue


#业务处理类
class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index handler get ...')


if __name__ == '__main__':
    #Application 是tornado.web的核心应用，是与服务器对应的接口。
    #里面保存了陆由映射表
    app = web.Application([
        (r'/',IndexHandler)  #陆由
    ])
    # listen用来创建一个http服务器的实例并绑定端口
    app.listen(8000)
    '''
    ioloop.IOLoop.current()返回当前线程的IOLoop实例
    start()启动IOLoop实例的IO循环，开启了监听
    '''
    ioloop.IOLoop.current().start()