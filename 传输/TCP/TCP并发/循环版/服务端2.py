import socket
import subprocess
import struct
import json

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.彩色光晕',8080))

print('start')
server.listen(5)
while True:
    conn,client_addr=server.accept()
    print('客户端',client_addr)

    while True:
        try:
            date=conn.recv(1024)
            if len(date)==0:break

            obj=subprocess.Popen(date.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                             )

            stdout=obj.stdout.read()
            stderr=obj.stderr.read()
            head_dic={
                'filename':'a.txt',
                'total_size':len(stdout) + len(stderr),
                'hash':'asdfaasfsdfsdaf1231fsafds54g65sda4gsdg'
            }
            head_json=json.dumps(head_dic)
            head_bytes=head_json.encode('utf-8')

            conn.send(struct.pack('i',len(head_bytes)))
            conn.send(head_bytes)

            print('正确命令长度',len(stdout))
            print('错误命令长度',len(stderr))

            total_size=len(stdout) + len(stderr)
            header=struct.pack('i',total_size)

            conn.send(header)
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break

    conn.close()

server.close()