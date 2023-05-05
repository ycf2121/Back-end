from threading import Thread,current_thread
from socket import *
import os

def task():
    client=socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.彩色光晕',8080))

    while True:
        msg='%s say hello' %current_thread().name
        # msg=input('>>').strip()
        # if not msg:continue
        client.send(msg.encode('utf-8'))
        data=client.recv(1024)
        print(data.decode('utf-8'))

if __name__ == '__main__':
    for i in range(50):
        t=Thread(target=task,)
        t.start()