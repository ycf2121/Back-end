import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.彩色光晕',8080))

while True:
    msg=input('请输入》》').strip()
    phone.send(msg.encode('utf-8'))
    date=phone.recv(1024)
    print(date)

phone.close()