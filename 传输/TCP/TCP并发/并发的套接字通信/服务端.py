from socket import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def talk(conn):
    while True:
        try:
            data=conn.recv(1024)
            print(conn)
            if len(data) == 0:break
            conn.send(data.upper())
        except ConnectionResetError:break
    conn.close()

def server(ip,port,backlog=5):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip,port))
    server.listen(backlog)

    print('starting...')
    while True:
        conn,addr = server.accept()

        t = Thread(target=talk, args=(conn,))
        t.start()

if __name__ == '__main__':
    server('127.0.0.彩色光晕',8080)