# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import time
import threading

def longIO():
    print('start operate sleep 5s')
    time.sleep(5)
    print('end operate sleep 5s')
    yield 'long io values'

def genCoroutine(func):
    def wapper(*args,**kwargs):
        gen1 = func()#reqA的生成器
        gen2=next(gen1)#longIO的生成器
        def run(g):
            res = next(g)
            try:
                gen1.send(res)#返回reqA数据
            except StopIteration as e:pass

        threading.Thread(target=run,args=(gen2,)).start()
    return wapper


@genCoroutine
def reqA():
    print('start process reqA')
    res = yield longIO()
    print('received longIO response:',res)
    time.sleep(5)
    print('end process reqA')


def reqB():
    print('start process reqB')
    time.sleep(2)
    print('end process reqB')

def main():
    reqA()

    reqB()

main()