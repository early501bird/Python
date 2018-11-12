# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler

class PCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('liwei','good')
        # 等同于self.set_header('set-cookie',"liwei=good11;path=/")
        self.write('set cookie ok')

class GetPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #获取cookie
        cookie=self.get_cookie('liwei',default='未登录')
        self.write('get cookie : '+cookie)

class ClearPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('liwei')
        self.write('clear cookie name:liwei')
        cookie = self.get_cookie('liwei',default="no sigin")
        self.write('cookie:'+cookie)