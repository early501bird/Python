# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import time
import threading

gen=None


def longIO():
    def run():
        print('start operate')
        time.sleep(5)
        try:
            global gen
            gen.send('continue send yield process')
        except StopIteration as e:
            pass
    threading.Thread(target=run).start()

def genCoroutine(func):
    def wapper(*args,**kwargs):
        global gen
        gen = func(*args,**kwargs)
        next(gen)
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