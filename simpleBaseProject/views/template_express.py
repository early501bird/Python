# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
from tornado.web import RequestHandler

class Template_expressionHandler(RequestHandler):
    def get(self, *args, **kwargs):
        num = 100
        per={
            'name':'lee',
            'age':12
        }

        obj={
            'obj1':'object1223',
            'obj2':'object2334343'
        }

        self.render('..//templates/templateDesc.html',num=num,per=per,**obj)