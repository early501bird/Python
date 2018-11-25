# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import os

BASE_DIRS=os.path.dirname(__file__)


options={
    "port":8000,

}

settings={
    'down_path':os.path.join(BASE_DIRS,'download'),

    # 设置静态文件目录'''
    'static_path':os.path.join(BASE_DIRS,'static'),

    # 设置模板文件目录
    'template_path':os.path.join(BASE_DIRS,'templates'),
    # 设置是否可以工作在调试模式下，默认False（正式的生产模式下）
    # True时：1,应用会监控源代码，当有保存改动时便会重新启动服务，减少手动重启的操作。（可以通过’autoreload‘:true单独设置）
    #        2,如果保存代码时出现错误，则自动重新会失败；当修改正确后，系统则不能再次重新，只能通过手动重启服务
    #        3,取消缓存编译的模板（可以通过compiled_template_cache=false单独设置）
    #        4,取消缓存靜态文件的Hashwfhg（可以通过staic_hash_cache=false单独设置）
    #        5,提供追踪信息（可以通过serve_traceback=true单独设置）
    "debug":True,
    #关闭项目页面自动转义，一般不建议使用
    # "autoescape":None

    "cookie_secret":"zXAClMAcTxWv/lFOZBHFAlOw7rONTEwntiHwGrvWcT8=",

    "xsrf_cookies":False,#开启XSRF保护

    "login_url":'/login',
}