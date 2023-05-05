from multiprocessing import Process #导入方法
import time #导入时间模块

class Myprocess(Process):
    def __init__(self,x):
        super().__init__()
        self.name=x
    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)  # 模拟进程运行的时间
        print('%s is done' %self.name)



if __name__ == '__main__':
    # Process(target=task,kwargs={'task':'子进程'})    #用kwargs执行
    p=Myprocess('子进程1')
    p.start()   #告诉操作系统要开启一个子进程的信号
    print('主进程')