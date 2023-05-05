#打印进度条
import time
def make_progress(percent,widch=50):
    if percent > 1:percent=1
    show_str=('[%%-%ds]' % widch) % (int(percent*widch) * '#')
    print('\r%s %s%%' %(show_str,int(percent*100)),end='')

total_size=5201314
recv_size=0
while recv_size < total_size:
    time.sleep(0.001)
    recv_size+=2121
    percent=recv_size / total_size
    make_progress(percent)