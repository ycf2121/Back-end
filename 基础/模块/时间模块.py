
#时间模块
import time
print('时间戳',time.time())
print('当前时间',time.strftime('%y-%m-%d'))
print('当前时区时间对象',time.localtime())
print('世界标准时间',time.gmtime())

#时间转换
#时间戳转换为结构化时间
print(time.localtime(134654654))
print(time.gmtime(134654654))

#结构化时间转换为时间戳
print(time.mktime(time.localtime()))
print(time.mktime(time.gmtime()))

#结构化时间转换为字符串形式
print(time.strftime('%y-%m-%d',time.localtime()))
print(time.strftime('%y-%m-%d',time.gmtime()))

#字符串时间转换为结构化时间
print(time.strptime('2023-04-13 00:31:31','%Y-%m-%d %H:%M:%S'))

#linux操作系统或unix操作系统时间
print(time.asctime())
print(time.ctime())
print(time.strftime('%a %b %d %H %M %S %Y'))

#结构化的时间转换成操作系统时间
print(time.asctime(time.localtime()))

#时间戳转换为操作系统图时间
print(time.ctime(123456789))

#datetime模块转换
import datetime
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(29222323323))
print(datetime.datetime.now() + datetime.timedelta(days=3))
print(datetime.datetime.now() + datetime.timedelta(weeks=-114.3))
s=datetime.datetime.now()
print(s.replace(year=2021,month=2,day=1))
