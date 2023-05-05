def dog(name):
    food_list=[]
    print('狗哥%s 准备开吃' %name)
    while True:
        food=yield food_list
        print('狗哥%s 吃了 %s' %(name,food))
        food_list.append(food)
a=dog('钢蛋')
a1=next(a)
print(a1)
a2=a.send(('饭','米'))
print(a2)
a3=a.send('汤')
print(a3)