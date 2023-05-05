from gevent import spawn,monkey;monkey.patch_all()
from socket import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.彩色光晕',8080))
server.listen(5)
server.setblocking(False)

conn_1=[]
while True:
    try:
        print('总连接数[%s]' %len(conn_1))
        conn,addr=server.accept()
        conn_1.append(conn)

    except BlockingIOError:
        del_l=[]
        for conn in conn_1:
            try:
                data=conn.recv(1024)
                if len(data) == 0:
                    del_l.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                pass
            except ConnectionResetError:
                del_l.append(conn)

        for conn in del_l:
            conn_1.remove(conn)
