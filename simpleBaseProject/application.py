# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

'''
这里引出配置setting和陆由Handler
'''

import tornado.web
from views.index import *
from views.template_express import *
from config import settings
import  os
from views.ormHandlers import *



class Application(tornado.web.Application):
    def __init__(self):
        handlers= (
            # (r'/', IndexHandler),
            # (r'/sunck',SunckHandler,{"word1": "good", "word2": "nice"}),
            # 反向解析
            web.url(r'/kaigo', KaigeHandler, {"word1": "good", "word2": "nice"}, name='kaigoIndex'),

            (r'/write', WriteHandler),
            (r'/json1', Json1Handler),
            (r'/json2', Json2Handler),
            (r'/defaultheader', HeaderHandler),
            (r'/status', StatusHandler),
            (r'/redirect', Redirect),
            # iserror?flag=0
            (r'/iserror', ErrorInfoHandler),

            # '''陆由传参数'''
            # 正则匹配解析Uri:  http://xxx/liuyifei/good/nice/pretty
            # (r'/liuyifei/(？P<p1>\w+)/(?p<p2>\w+)/(?P<p2>\w+)',LiuyifeiHandler) 这里p1-p3对应需要把h1-h3改为p1-p3
            (r'/liuyifei/(\w+)/(\w+)/(\w+)', LiuyifeiHandler),
            # get 方式
            # zhangmanyu？a=1&b=2&c=3
            (r'/zhangmanyu', ZhangmanyuHandler),

            # post
            (r'/postfile', PostFileHandler),

            #request对象
            (r'/zhuyin',ZhuyinHandler),

            #upload file
            (r'/upfile',UploadFileHandler),
            #template expression parameter
            (r'/template', Template_expressionHandler),
            (r'/trans',TransHandler),
            #继承
            (r'/cart', CartHandler),
            # orm
            (r'/students', StudentsHandler),

            (r'/(.*)$',web.StaticFileHandler,{"path":os.path.join(config.BASE_DIRS,"static/html"),"default_filename":"index.html"}),


        )

        super(Application,self).__init__(handlers,**settings)

