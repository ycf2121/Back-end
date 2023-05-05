import socket
phone =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.彩色光晕',8080))
phone.send('hello'.encode('utf-8'))
date=phone.recv(1024)
print(phone)
print(date)
phone.close()