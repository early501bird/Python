# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
import tornado.web
from tornado.web import RequestHandler

#normal cookies
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
        # self.clear_all_cookies()
        self.write('clear cookie name:liwei')
        cookie = self.get_cookie('liwei',default="no sigin")
        self.write('cookie:'+cookie)


#safe cookies
class SafeCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie('secretName',"mysecret name")
        self.write('set secretname cookie : mysecret name')
        print('secret cookie,secretName:',self.get_secure_cookie('secretName'))



class CookieNumHandler(RequestHandler):
    def get(self, *args, **kwargs):
        count=self.get_cookie('count',"未登录")

        # if not count:
        #     count=1
        # else:
        #     count=int(count)
        #     count+=1
        # self.set_cookie('count',str(count))

        self.render('cookieNum.html',count=count)
        #通过testXSRF.html可以以get方式模拟请滶伪造 以上修改cookie建议放在Post中实现


class PostxsrfCookie(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postXSRF.html')

    def post(self, *args, **kwargs):
        count=self.get_cookie('count',None)
        if not count:
            count = 1
        else:
            count = int(count)
            count+=1
        self.set_cookie('count',str(count))
        self.redirect(r'cookienum')

class SetxsrfCookie(RequestHandler):
    def get(self, *args, **kwargs):
        #设置_xsrf
        self.xsrf_token
        self.finish("OK")



class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        next=self.get_argument('next','/')
        url='login?next='+next
        self.render('login.html',url=url)

    def post(self, *args, **kwargs):
        name=self.get_arguments('username')
        pwd=self.get_arguments('passwd')
        next = self.get_argument('next', '/')
        print(next)
        if name[0]=='1' and pwd[0]=='1':
            self.redirect(next+"?flag=logined")
        else:
            self.redirect('/login?next='+next)

class HomeHandler(RequestHandler):
    #验证用户逻辑,成功Return　True，
    # 失败则自动会重定向到config.py中login_url所指向的陆由
    def get_current_user(self):
        flag=self.get_argument('flag',None)
        return flag


    #由get_cuurent_user()验证通过才能Get
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('home.html')