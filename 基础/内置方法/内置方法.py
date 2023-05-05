name='啊 ycF'
print(name.strip())             #去除空格
print(name.startswith('y'))     #是否以y开头
print(name.endswith('f'))       #是否以f结尾
print(name.replace(' ','*',1))  #将空格替换成*，指定个数为1
print(name.split(' '))          #切片分割
print(name.upper())             #转换为大写
print(name.lower())             #转换为小写
print(name[1])                  #输出索引为1的字符
print(name[0:3])                #输出索引0到3的字符，顾头不顾尾
print(name[-1:-3:-1])           #倒着输出，步长为1
print(name[:-1])                #顾头不顾尾，不写代表从头开始
print(name[:])                  #顾头不顾尾，不写代表全部
print(name.index('y'))          #输出y对应的索引
print(name.find('y'))           #输出y对应的索引
print(name.strip('F'))          #去除左右两边对应的字符

#赋值给列表，并删除索引为3的属性
n=list(name)
del n[3]
print(n)

print('my name is egon'.capitalize())   #将首字母大写
print('my name is egon'.swapcase()) #全部转换为大写
print('my name is egon'.title())    #每个单词的首字母转为大写

print('asda123'.isalnum())          #判断是否是数字和字母组成，可以纯字母或者数字
print('asfg'.isalpha())             #判断是否是纯字母
print('asf'.islower())              #判断是否是全部小写
print('AS'.isupper())               #判断是否是全部大写
print('    '.isspace())             #判断是否是全部空格，可以是tab键，可以回车
print('My Name Is Ycf'.istitle())   #判断首字母是否大写
print('1111'.isdigit())             #判断是否是纯数字

print('info egon'.center(50,'-'))   #center居中显示（宽度，以什么分割）
print('info egon'.ljust(50,'-'))    #ljust左侧显示（宽度，以什么分割）
print('info egon'.rjust(50,'-'))    #rjust右侧显示（宽度，以什么分割）
print('info egon'.zfill(50))        #zfill用0补充（宽度）
print('a\tb\tc'.expandtabs(5))      #expandtabs（间隔的宽度）

info='egon:18:male'
l=info.split(':')       #以:进行切片存为列表
print(l,type(l))
new_info='-'.join(l)    #用-进行拼接成字符串
print(new_info,type(new_info))
num=['a','b','c']
print(type(num))
print('*'.join(info),type(info))    #将列表用*拼接成字符串
print('/*-456ads'.strip('/*-ads'))  #去除左右两边包含/*-ads的
name='****egon****'
print(name.lstrip('*'))             #去除左边带*的
print(name.rstrip('*'))             #去除右边带*的


print('my name is %s my age is %s' %('ycf',22))     #按位置进行传输一
print('my name is {} my age is {}'.format('ycf',22))    #按位置进行传输二
print('my name is {name} my age is {age}'.format(name='ycf',age=22))    #用关键字传参
print('my name {2} is {0}{0} my age is {1}{1}{0}'.format('ycf',2,3,))  #按照传参的索引对{}对应的数字进行传值
