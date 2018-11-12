# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
from orm.orm import ORM
import config
import os
import json

#单例类装饰器
def singleton(cls,*args,**kargs):
    instances={}
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args,**kargs)
        return instances[cls]
    return _singleton

@singleton
class Student(ORM):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def save(self):
        filename = os.path.join(config.settings['down_path'], self.name)
        str = json.dumps(self,default=lambda obj:obj.__dict__,sort_keys=True,indent=4)
        with open(filename,'w') as f:
            f.write(str)
        print('orm save student name:{0},age:{1}'.format(self.name,self.name))