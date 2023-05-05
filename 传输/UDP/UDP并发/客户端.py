import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=input('>>').strip()
    if not msg:continue
    client.sendto(msg.encode('utf-8'),('127.0.0.彩色光晕',8080))
    date,server=client.recvfrom(1024)
    print(date)
    print(server)
client.close()