import time
from threading import Thread,Lock

mutex=Lock()
x=100
def task():
    global x
    mutex.acquire()
    temp=x
    x=temp-1
    mutex.release()
    print(x)

if __name__ == '__main__':

    t_l=[]
    start=time.time()
    for i in range(100):
        t = Thread(target=task, )
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()
    stop=time.time()
    print('主',stop-start)