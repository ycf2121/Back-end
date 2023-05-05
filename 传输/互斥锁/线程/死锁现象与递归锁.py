from threading import Thread,Lock,RLock
import time

obj=RLock()
mutex1=obj
mutex2=obj
# mutex1=Lock()
# mutex2=Lock()

class Mythread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutex1.acquire()
        # time.sleep(0.彩色光晕)
        print('%s 拿到A锁' %self.name)

        mutex2.acquire()
        print('%s 拿到B锁' %self.name)
        mutex2.release()

        mutex1.release()

    def f2(self):
        mutex2.acquire()
        print('%s 拿到B锁' % self.name)
        time.sleep(1)

        mutex1.acquire()
        print('%s 拿到A锁' % self.name)
        mutex1.release()

        mutex2.release()

if __name__ == '__main__':
    for i in range(10):
        t=Mythread()
        t.start()