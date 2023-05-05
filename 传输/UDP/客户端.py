import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input('>>').strip()
    client.sendto(msg.encode('utf-8'),('127.0.0.彩色光晕',8080))
    data,server_addr = client.recvfrom(1024)
    print(data)
client.close()
