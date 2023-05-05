from socket import *
import time
import select

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.彩色光晕',8080))
server.listen(5)
server.setblocking(False)

data_dic={}
read_list=[server,]
write_list=[]
print('start...')
while True:
    rl,wl,xl=select.select(read_list,write_list,[])
    # print('read_list:%s rl:%s wl:%s xl:%s' %(len(read_list),len(rl),len(wl),len(xl)))
    for sk in rl:
        if sk == server:
            conn,addr=sk.accept()
            read_list.append(conn)
        else:
            try:
                data=sk.recv(1024)
                if len(data) == 0:continue
                write_list.append(sk)
                data_dic[sk]=data
            except ConnectionResetError:
                pass

    for sk in wl:
        sk.send(data_dic[sk].upper())
        data_dic.pop(sk)
        write_list.remove(sk)