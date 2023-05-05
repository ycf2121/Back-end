#随机生成验证码
import random
def code(n,alpha=True): #默认生成大小写字母与数字的验证码
    str1='' #定义空字符串
    str2='' #定义空字符串
    for i in range(n):
        num=random.randint(0,9) #随机生成0-9
        # if alpha:
        upper_lapha=chr(random.randint(65,90))  #随机转换成大写字母
        lower_lapha=chr(random.randint(97,122)) #随机转换成小写字母
        num=random.choice([num,upper_lapha,lower_lapha]) #随机生成大小写字母与数字的验证码
        num1=random.choice([upper_lapha,lower_lapha])    #随机生成大小写字母的验证码
        str1=str1+str(num)
        str2=str2+str(num1)
    if alpha:
        return str1
    else:
        return str2
    # return str1
print(code(6,)) #要生成验证码的个数