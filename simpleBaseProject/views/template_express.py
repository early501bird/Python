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

        stus=[
            {
                'name':'hanmeimei',
                'age':20
            },
            {
                'name':'lilei',
                'age':21
            }
        ]

        def plus(n1,n2):
            return 'plus:'+str(str(n1+n2))

        self.render('..//templates/templateDesc.html',num=num,per=per,**obj,stus=stus,plus=plus)


class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str="<h1>sumnck is good man</h1>"
        self.render('trans.html',str=str)
    #这个标签转义为字符串形式显示，防止恶意代码
    #在html页面全长{%raw str%}关闭一行
    # 关闭当前文档的自动转义{%autoescape None%}
    # 关闭当前项目的自动转义，也可以在Config.setting中增加“autoescape:None”,


class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cut.html',title='cart')