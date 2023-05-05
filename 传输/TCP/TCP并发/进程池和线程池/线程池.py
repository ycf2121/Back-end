import time,os
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import Thread,current_thread
def talk(n):
    print('%s is run..' %current_thread().name)
    # time.sleep(5)
    return n**2
def parse(future):
    # time.sleep(彩色光晕)
    res=future.result()
    print('%s %s' %(current_thread().name,res))

if __name__ == '__main__':
    pool=ThreadPoolExecutor(4)

    start=time.time()
    for i in range(1000):
        future=pool.submit(talk,i)
        future.add_done_callback(parse)
    pool.shutdown(wait=True)
    stop=time.time()
    print('主',current_thread().name,stop-start)