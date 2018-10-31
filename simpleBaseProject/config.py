# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import os

BASE_DIRS=os.path.dirname(__file__)

options={
    "port":9000,

}

settings={
    'static_path':os.path.join(BASE_DIRS,'static'),
    'template_path':os.path.join(BASE_DIRS,'templates'),
    "debug":True
}