def register():
    print('注册')
    while True:
        name=input('username>>:').strip()
        with open(r'/后端/函数/c.txt', mode='r', encoding='utf-8') as f:
            for line in f:
                info = line.strip('\n').split(':')
                if name == info[0]:
                    print('用户名已存在，请重新输入')
                    break
            else:
                break
    while True:
        pwd=input('password>>:').strip()
        pwd1=input('password>>:').strip()
        if pwd == pwd1:
            with open(r'/后端/函数/c.txt', mode='a', encoding='utf-8') as f:
                f.write('%s:%s\n' %(name,pwd))
                break
        else:
            print('两次密码输入不一致')

register()