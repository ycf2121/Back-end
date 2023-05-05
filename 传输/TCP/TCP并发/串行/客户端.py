import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.彩色光晕',8080))
while True:
    msg=input('>>').strip()
    client.send(msg.encode('utf-8'))
    date=client.recv(1024)
    print(date)

client.close()