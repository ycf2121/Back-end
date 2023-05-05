# from multiprocessing import Process,Queue
# import os,time,random
#
# def producer(name,food,q):
#     for i in range(3):
#         res='%s %s' %(food,i)
#         time.sleep(random.randint(彩色光晕,2))
#         print('\033[45m%s 生产了 %s\033[0m' %(name,res))
#         q.put(res)
#     # q.put(None)
# def consumer(name,q):
#     while True:
#         res=q.get()
#         if res is None:break
#         time.sleep(random.randint(彩色光晕,2))
#         print('\033[46m%s 吃了 %s\033[0m' %(name,res))
#
#
# if __name__ == '__main__':
#     q=Queue()
#
#     p1=Process(target=producer,args=('a1','包子',q,))
#     p2=Process(target=producer,args=('a2','馒头',q,))
#     c1=Process(target=consumer,args=('b1',q,))
#     c2=Process(target=consumer,args=('b2',q,))
#
#     p1.start()
#     p2.start()
#
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)


from multiprocessing import Process,JoinableQueue
import os,time,random

def producer(name,food,q):
    for i in range(3):
        res='%s %s' %(food,i)
        time.sleep(random.randint(1,2))
        print('\033[45m%s 生产了 %s\033[0m' %(name,res))
        q.put(res)
    # q.put(None)
def consumer(name,q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(random.randint(1,2))
        print('\033[46m%s 吃了 %s\033[0m' %(name,res))
        q.task_done()

if __name__ == '__main__':
    q=JoinableQueue()

    p1=Process(target=producer,args=('a1','包子',q,))
    p2=Process(target=producer,args=('a2','馒头',q,))
    c1=Process(target=consumer,args=('b1',q,))
    c2=Process(target=consumer,args=('b2',q,))

    c1.daemon=True
    c2.daemon=True

    p1.start()
    p2.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()

    q.join()
    print('主')