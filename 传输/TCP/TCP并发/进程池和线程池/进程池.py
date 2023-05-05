import time,os
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
def talk(n):
    print('%s is run..' %os.getpid())
    # time.sleep(5)
    return n**2
def parse(future):
    # time.sleep(彩色光晕)
    res=future.result()
    print('%s 处理了 %s' %(os.getpid(),res))

if __name__ == '__main__':
    pool=ProcessPoolExecutor(4)

    start=time.time()
    for i in range(1000):
        future=pool.submit(talk,i)
        future.add_done_callback(parse)
    pool.shutdown(wait=True)
    stop=time.time()
    print('主',os.getpid(),stop-start)