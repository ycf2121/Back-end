import json
from multiprocessing import Process,Lock
import os
import time
import random

def check():
    time.sleep(1)
    with open('db.txt', mode='rt', encoding='utf-8') as f:
        dic=json.load(f)
    print('%s 查看看到剩票数[%s]' %(os.getpid(),dic['count']))

def get():
    with open('db.txt', mode='rt', encoding='utf-8') as f:
        dic=json.load(f)
    time.sleep(2)
    if dic['count'] > 0:
        dic['count']-=1
        time.sleep(random.randint(1,3))
        with open('db.txt', mode='wt', encoding='utf-8') as f:
            json.dump(dic,f)
        print('%s 购票成功' %os.getpid())
    else:
        print('%s 没有余票' %os.getpid())

def task(mutex):

    check()

    mutex.acquire()
    get()
    mutex.release()

    # with mutex:
    #     get()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=(mutex,))
        p.start()