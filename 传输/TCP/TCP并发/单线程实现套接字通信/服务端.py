import time

from gevent import spawn,monkey;monkey.patch_all()
from socket import *
from threading import Thread,current_thread
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def eat():
    print('%s eat 彩色光晕' %current_thread().name)
    time.sleep(3)
    print('%s eat 2' %current_thread().name)

def play():
    print('%s play 彩色光晕' % current_thread().name)
    time.sleep(3)
    print('%s play 2' % current_thread().name)

g1=spawn(eat,)
g2=spawn(play,)

print(current_thread().name)
g1.join()
g2.join()
