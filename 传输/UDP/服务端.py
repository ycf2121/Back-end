import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.彩色光晕',8080))
while True:
    data,client_addr=server.recvfrom(1024)
    server.sendto(data.upper(),client_addr)

server.colse()