#subprocess模块
import subprocess
obj=subprocess.Popen('tasklist',
                 shell=True,
                 stdout=subprocess.PIPE,    #正确指令放入管道，结果只能有一份
                 stderr=subprocess.PIPE     #错误指令放入管道，结果只能有一份
                 )
stdout_res=obj.stdout.read()    #读取正确的
print(stdout_res.decode('gbk'))
stderr_res=obj.stderr.read()    #读取错误的
print(stderr_res)