# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
from tornado import  web
import config,os


class StaticFileHandler(web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticFileHandler,self).__init__(*args,**kwargs)
        self.xsrf_token



# class IndexHandler(web.RequestHandler):
#     def get(self, *args, **kwargs):
#         # self.write('index handler get')
#         url=self.reverse_url('kaigoIndex') #反向解析， kaigoIndex这里对应的是name标签
#         self.write("<a href='{0}'>另一个页面</a>".format(url))
#         # print('index handler get')




class SunckHandler(web.RequestHandler):
    #接收参数
    def initialize(self,word1,word2):
        self.word1=word1
        self.word2=word2
        print('*****')
    def get(self, *args, **kwargs):
        self.write('sunck recv parameter:{0},{1}'.format(self.word1, self.word2))



class KaigeHandler(web.RequestHandler):
    # 接收参数
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        self.write('kaigo recv parameter:{0},{1}'.format(self.word1, self.word2))


class WriteHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('index handler get')
        self.write('index handler get')
        self.write('index handler get')
        # 刷新缓冲区关闭当次请求通道
        # 在finish后就不能再write()
        self.finish()

import json

#response Header:Content-type:application/json
class Json1Handler(web.RequestHandler):
    def get(self, *args, **kwargs):
        per={
            "name":"sunck",
            "age":18,
            "height":155,
            "weight":56
        }
        jstr = json.dumps(per)
        self.set_header('Content-Type','application/json;charset=UTF-8')
        self.set_header('sunck',"good")
        self.write(jstr)

# header:content-type:text/html
class Json2Handler(web.RequestHandler):
    def get(self, *args, **kwargs):
        per={
            "name":"sunck",
            "age":18,
            "height":155,
            "weight":56
        }
        self.write(per)


class HeaderHandler(web.RequestHandler):
    #在进入http响应处理方法前被调用 （get前）重写来预先设置默认的Headers
    def set_default_headers(self):
        self.set_header("Conent-Type","text/html;charset=UTF-8")
        self.set_header('kaige','nice')

    #以下接口的Headers配置都可以在上面的方法中设置
    def get(self, *args, **kwargs):
        #注意这里设置后，会覆盖掉set_default_headers中的设置
        # self.set_header("Conent-Type","application/json;charset=UTF-8")
        self.set_header('kaige','good')
        pass

    def post(self, *args, **kwargs):pass


'''设置返回的状态码statusCode'''
class StatusHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(999,'test set status 304') #注意这里如果不填写后面的描述信息，则会报错。
        self.write('set status 304')

'''重定向'''
class Redirect(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')
        print('redirect url')


'''抛出http错误状态码,默认500.抛出错误后，tornado会调用write_error方法处理，并返回给浏览器界面'''
class ErrorInfoHandler(web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        code =0
        if status_code==500:
            self.write('服务器内部错误')
            code=500
            #返回500界面
        elif status_code==404:
            self.write('资源不存在')
            code =404
            #返回404l界面
        else:
            self.write('some error action')
            code = 999

        self.set_status(code,'')

    def get(self, *args, **kwargs):
        flag= int(self.get_query_argument('flag'))
        self.send_error(flag)
        print('send error:',flag)


class LiuyifeiHandler(web.RequestHandler):
    def get(self,h1,h2,h3, *args, **kwargs):
        print(h1,h2,h3)
        self.write('liuyifei uri parameter:')

class ZhangmanyuHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a', default=100)
        b = self.get_query_argument('b', default=100,strip=False) #不去除两边的空格
        c = self.get_query_argument('c', default=100,strip=True)
        print(a,b,c)
        self.write('zhangmanyu is an actress')


class PostFileHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/postfile.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        passwd = self.get_body_argument('passwd')
        hobby = self.get_body_arguments('hobby')
        print(username,passwd,hobby)
        self.write('username:{0},pwd:{1},hobby:{2}'.format(username,passwd,hobby))



class ZhuyinHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        print("method",self.request.method)
        print("host",self.request.host)
        print("uri",self.request.uri)
        print("path",self.request.path)
        print("query",self.request.query)
        print('version',self.request.version)
        print("headers",self.request.headers)
        print('body',self.request.body)
        print('remoteip',self.request.remote_ip)
        print('files',self.request.files)


class UploadFileHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('../templates/upfile.html')

    def post(self, *args, **kwargs):
        filesdict= self.request.files
        for files in filesdict:
            fileArr = filesdict[files]
            for file in fileArr:
                filename = os.path.join( config.settings['down_path'],file['filename'])
                with open(filename,'wb') as f:
                    f.write(file['body'])

        self.write('ok')

