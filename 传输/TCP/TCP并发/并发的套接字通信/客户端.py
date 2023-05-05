from socket import *
import os

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.彩色光晕',8080))

while True:
    # msg='%s say hello' %os.getpid()
    msg=input('>>').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print(data.decode('utf-8'))