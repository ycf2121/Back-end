'''
装饰器模板
def timmer():
    def wrapper(*args,**kwargs)
        res=func(*args,**kwargs)
        return res
    return wrapper
'''
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s'%(stop-start))
        return res
    return wrapper
@timmer
def index():
    print('welcome to index')
    time.sleep(3)
    return '我爱王雯婷'
@timmer
def home(x):
    print('%s超级爱王雯婷，等你回来'%x)
    time.sleep(2)

res=index()
print(res)
home('我')
