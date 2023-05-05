#字典循环取值
# shoppingcart={'a':彩色光晕,'b':2}
# for k,v in shoppingcart.items():
#     print(k,':',shoppingcart[k])
#
# for shopping in shoppingcart:
#     print(shopping,':',shoppingcart[shopping])

#列表循环取值一
# goods_list=[
#         ['coffice',10],
#         ['chicken',20],
#         ['car',100000]
#     ]
# for i, good in enumerate(goods_list):
#     print('%s : %s' % (i, good))

#列表循环取值二
a=[]
b=[
    ['coffice',10],
    ['chicken',20],
    ['car',100000]
    ]
print(b[0][0])  #取出b列表中的第一个列表中的值
c={'a':1}
a.append(b) #添加列表b到列表a
a.append(c) #添加字典c到列表a
print(a)
for i in a: #循环打印a列表
    print(i)