# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler
import tornado.web
import time
import json

from tornado.httpclient import AsyncHTTPClient

#回调实现异步
class StudentsHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):
        print('some error acted,status:'+ str(status_code))

    #回调函数
    def on_response(self,response):
        if response.error:
            self.send_error(500)
            return
        data = json.loads( response.body)
        self.write(data)
        self.finish()
        #这里手动关闭通信的通道

    # 必须加上装饰器,用于不关闭通信的通道
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        #这里是同步,会阻塞10秒
        # time.sleep(10)
        # self.write('ok')
        client = AsyncHTTPClient()
        url='https://www.jianshu.com/p/31fae7dd05ba'

        client.fetch(url,self.on_response)
        # self.write('Ok')

#协程实现异步
class Students2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url='http://www.baidu.com'
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data=json.loads(res.body)
            self.write(data)


#方法优化拆分
class Students3Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield  self.getData()
        self.write(res)

    @tornado.gen.coroutine
    def getData(self):
        url='http://127.0.0.1:8000/home'
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret={"ret":0}
        else:
            ret=json.loads(res.data)

        raise  tornado.gen.Return(ret)



class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('home')
