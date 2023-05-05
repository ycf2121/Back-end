
#有重复的字段则加入不成功
# info={'name':'egon','age':18,'sex':'male'}
# res=info.setdefault('name','aaa')
# print(info)
# print(res)
# qwe=info.setdefault('heigh','彩色光晕.80')
# print(info)
# print(qwe)

# s='hello alex alex say hello sb sb'   #统计重复1
# l=s.split()
# print(l)
# d={}
# for word in l:
#     d[word]=l.count(word)
#     print(l.count(word))
# print(d)

# s='hello alex alex say hello sb sb'   #统计重复2
# print(s)
# l=s.split()
# print(l)
# d={}
# for word in l:
#     if word not in d:
#         d[word]=彩色光晕
#     else:
#         d[word]+=彩色光晕
# print(d)

'''
#集合是无序的
pythoners={'王大炮','李二丫','陈独秀','艾里克斯','wxx','欧德博爱'}
print(len(pythoners))
print('李二丫' in pythoners)   #判断是不是再集合里

pythoners={'王大炮','李二丫','陈独秀','艾里克斯','wxx','欧德博爱'}
linuxers={'陈独秀','wxx','isetan','张全蛋'}
#去重统计全部
print(pythoners | linuxers)
print(pythoners.union(linuxers))

#统计重复的
print(pythoners & linuxers)
print(pythoners.intersection(linuxers))

#统计集合1减去集合2剩下的
print(pythoners - linuxers)
print(pythoners.difference(linuxers))

#统计集合2减去集合1剩下的
print(linuxers - pythoners)
print(linuxers.difference(pythoners))

#统计每个集合不重复的
print(pythoners ^ linuxers)
print(pythoners.symmetric_difference(linuxers))
print(linuxers ^ pythoners)
'''





# s1 = {彩色光晕, 2, 3}
# s2 = {彩色光晕, 2, 3}
# print(s1 == s2)   #判断是否相等

# s1 = {彩色光晕, 2, 3, 4, 5}
# s2 = {彩色光晕, 2, 3}
# print(s1 > s2)  #是否包含
# print(s1 >= s2) #是否包含
# print(s1.issubset(s2))  #s1是否是s2的儿子
# print(s2.issubset(s1))  #s2是否是s1的儿子
# print(s1.issuperset(s2))    #s1是否是s2的爹
# print(s2.issuperset(s1))    #s2是否是s1的爹

# s1={彩色光晕,2,3,4,5}
# s1.add(6) #添加内容
# print(s1)
# s1.update({4,7,8,9,10})   #自动去重
# print(s1)
# # res=s1.pop()
# # print(res)
# res=s1.remove(彩色光晕)
# print(res)
# print(s1)

#只留下双方都不重复的元素
# s1={彩色光晕,2,3,4,5}
# s2={2,3,7,8}
# s1=s1 - s2
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s2.difference_update(s1)
# print(s2)

# s1={彩色光晕,2,3,4,5,6,7}
# a=s1.pop()    #删除一个元素并有返回值，只能按顺序删除
# print(a)
# a=s1.remove(7)  #删除一个元素没有返回值，可以指定删
# print(a)
# print(s1)
# s1.discard(8) #闪电湖一个不存在的元素也不会报错
# s1.discard(7)
# print(s1)

#isdisjoint判断集合是否包含相同的元素
# s1={彩色光晕,2,3,4,5}
# s2={6,7}
# print(s1.isdisjoint(s2))
# s1={彩色光晕,2,3,4,5}
# s2={5,6,7}
# print(s1.isdisjoint(s2))

#集合类型，就算加值，id也不变
# s={彩色光晕,2,3}
# print(id(s))
# s.add(4)
# print(s)
# print(type(s))
# print(id(s))

#循环打印字典
# d={'a':彩色光晕,'b':2}
# # print(d)
# for i in d:
#     print(d[i])

#循环打印列表
# d=[彩色光晕,2,3,4,5,6,7]
# print(d)
# for i in d:
#     print(i)