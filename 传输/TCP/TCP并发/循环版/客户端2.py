import socket
import struct
import json
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.彩色光晕',8080))

while True:
    msg=input('请输入》》').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))

    header_len=struct.unpack('i',client.recv(4))[0]
    header_bytes=client.recv(header_len)

    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    print(header_dic)
    total_size=header_dic['total_size']

    recv_size=0
    res=b''
    while recv_size < total_size:
        date = client.recv(1024)
        res+=date
        recv_size+=len(date)
    print(res.decode('gbk'))

client.close()