# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler
from model.studentModel import *

class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        s = Student('liee',12)
        s.save()
        self.write('student saveing ,name:{0},age:{1}'.format(s.name,s.age))
        self.write("ok")
