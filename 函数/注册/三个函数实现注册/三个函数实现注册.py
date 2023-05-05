def check_user():
    while True:
        x=input('请输入用户名:').strip()
        if x.isalpha():
            return x
        else:
            print('用户名必须为字符')
def check_pwd():
    while True:
        y=input('请输入密码:').strip()
        yy=input('请再次输入密码:').strip()
        if y==yy:
            return y
        else:
            print('两次输入的密码不一致')
def db_hanle(x,y):
    with open(r'a.txt', mode='a+t', encoding='utf-8') as f:
        f.write('%s:%s\n' %(x,y))
def register():
    xx=check_user()
    yy=check_pwd()
    db_hanle(xx,yy)

register()