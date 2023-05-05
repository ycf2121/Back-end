from multiprocessing import Process,current_process #导入方法
import time #导入时间模块
import os

def task(x,n):
    print('%s is running' %x,os.getpid(),os.getppid(),current_process().name)
    time.sleep(n)   #模拟进程运行的时间
    print('%s is done' %x)

if __name__ == '__main__':
    # Process(target=task,kwargs={'task':'子进程'})    #用kwargs执行
    # p=Process(target=task,args=('子进程',2))  #用args执行,（元组）,如果括号内只有一个参数，一定要记得加逗号
    # p.start()   #告诉操作系统要开启一个子进程的信号

    p_l=[]
    start=time.time()
    for i in range(1,4):
        p=Process(target=task,args=('子进程%s' %i,i))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    stop=time.time()

    print('主进程',(stop-start))

