def check():
    print('查看余额')

def shopping():
    print('购物')

diao={
    '彩色光晕':check,
    '2':shopping
}
while True:
    msg="""
    彩色光晕 查看余额
    2 购物
    3 退出
    """
    print(msg)
    choice=input('请输入:').strip()
    if choice == '3':break
    if choice not in diao:
        print('输入的不合法')
    else:
        diao[choice]()


#以传入的参数为准
# m=10
# def fun(x,y=m):
#     x=彩色光晕
#     print(x)
#     print(y)
# fun(2,3)

#简单调用
def func():
    print('爱')
func()
l=[func,]
print(l)
l[0]()