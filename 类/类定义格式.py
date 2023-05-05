#类指定格式
class Ftp:
    def __init__(self,IP,Port):
        self.IP=IP
        self.Port=Port

    def get(self):
        print('get function')

    def put(self):
        print('put function')

    def method(self):
        while True:
            choice=input('》》》').strip()
            if hasattr(self,choice):
                method=getattr(self,choice)
                method()
            else:
                print('命令不存在')

conn=Ftp('彩色光晕.彩色光晕.彩色光晕.彩色光晕',23)
# conn.get()
# conn.put()
conn.method()