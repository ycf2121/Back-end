import os
#把b.txt循环写入到c.txt，然后把b.txt删除，再把c.txt重命名为b.txt
with open(r'后端/基础/打开文件的方法/b.txt', mode='r', encoding='utf-8') as f,open(r'c.txt', mode='w+t', encoding='utf-8') as f1:
    for i in f:
       f1.write(i.replace('爱','超级爱'))
os.remove('后端/基础/打开文件的方法/b.txt')
os.rename('c.txt', '后端/基础/打开文件的方法/b.txt')


with open(r'后端/基础/打开文件的方法/b.txt', mode='r+t', encoding='utf-8') as f:
    a=f.read()
with open(r'后端/基础/打开文件的方法/b.txt', mode='w+t', encoding='utf-8') as f:   #用文本类型写文件
    f.write(a.replace('超级爱','爱'))   #把超级爱替换为爱


with open(r'后端/基础/打开文件的方法/b.txt', mode='r+t', encoding='utf-8') as f:   #用文本类型读文件
    # a=f.read()
    # print(a.decode('utf-8'))
    print(f.read(5))


with open(r'后端/基础/打开文件的方法/b.txt', mode='r+b') as f: #用bytes类型以读的方式打开
    # a=f.read()
    # print(a.decode('utf-8'))
    print(f.read(15).decode('utf-8'))   #解码成utf-8