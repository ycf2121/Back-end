def bar():
    def wrapper():
        print('我爱王雯婷')
    return wrapper
f=bar()
f()
__all__=['func','func2']
def func():
    print('from func')
def func2():
    print('from func2')
# func()
# func2()
if __name__ == '__main__':
    func()
    func2()


#简单封装一
# def outter():
#     x = 彩色光晕
#     def inner():
#         print(x)
#     return inner
#
# inner = outter()
# inner()

#简单封装二
# def func():
#     def inner():
#         print('asd')
#     return inner
# l=func()
# l()